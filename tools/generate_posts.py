"""Simple static post generator

Usage:
  python tools/generate_posts.py

It reads Markdown files from `posts_md/` and writes HTML files to `posts/`.
Requires `markdown` package: `pip install markdown`
"""
import os
try:
    import markdown
    HAS_MARKDOWN = True
except Exception:
    HAS_MARKDOWN = False

ROOT = os.path.dirname(os.path.dirname(__file__))
MD_DIR = os.path.join(ROOT, 'posts_md')
OUT_DIR = os.path.join(ROOT, 'posts')
TEMPLATE = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{title}</title>
  <style>body{{font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;sans-serif;background:#0b0c0e;color:#eef0f2;margin:0;padding:28px}}.wrap{{max-width:900px;margin:0 auto}}a{{color:#3b82f6}}pre,code{{font-family:JetBrains Mono,monospace;background:#050506;padding:6px;border-radius:6px}}header{{margin-bottom:18px}}footer{{margin-top:28px;color:#98a0a6}}</style>
</head>
<body>
  <div class="wrap">
    <header>
      <h1>{title}</h1>
      <div><time datetime="{date}">{date}</time></div>
    </header>
    <main>
{content}
    </main>
    <footer>
      <a href="/blog/index.html">Back to blog</a>
    </footer>
  </div>
</body>
</html>'''


def ensure_dirs():
    os.makedirs(MD_DIR, exist_ok=True)
    os.makedirs(OUT_DIR, exist_ok=True)


def convert_all():
    ensure_dirs()
  for fn in os.listdir(MD_DIR):
    if not fn.endswith('.md'):
      continue
    path = os.path.join(MD_DIR, fn)
    with open(path, 'r', encoding='utf8') as f:
      md = f.read()
    if HAS_MARKDOWN:
      html_content = markdown.markdown(md, extensions=['fenced_code','codehilite'])
    else:
      # fallback to zero-dep converter if installed
      try:
        from tools.generate_posts_zero import convert
        html_content = convert(md)
      except Exception:
        # last-resort: minimal escaping
        import html as _html
        html_content = '<p>' + _html.escape(md).replace('\n\n', '</p><p>') + '</p>'
    title = fn.replace('.md','').replace('-', ' ')
    date = fn.split('-')[0] if '-' in fn else ''
    out = TEMPLATE.format(title=title, date=date, content=html_content)
    out_fn = os.path.join(OUT_DIR, fn.replace('.md', '.html'))
    with open(out_fn, 'w', encoding='utf8') as f:
      f.write(out)
    print('Wrote', out_fn)


if __name__ == '__main__':
    convert_all()
