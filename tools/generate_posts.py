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
  <title>{title} — Pranav Purwar</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
  <div class="container">
    <nav class="nav-header">
      <a href="/" class="nav-brand">
        <div class="avatar-box"><img src="https://avatars.githubusercontent.com/u/75154889?v=4" alt="Pranav Purwar"></div>
        <div>
          <div class="brand-title">Pranav Purwar</div>
          <div class="brand-handle">@invokevirtual</div>
        </div>
      </a>
      <div class="nav-links">
        <a href="/" class="nav-link">Home</a>
        <a href="/blog/index.html" class="nav-link">Blog</a>
        <a href="/cv.pdf" class="btn btn-outline" download>Download CV</a>
        <a href="/donate.html" class="btn btn-primary">Sponsor</a>
      </div>
    </nav>
    <main class="content">
      <article class="project-card">
        <header class="card-top">
          <div>
            <h1 style="font-size: 24px; margin-bottom: 6px;">{title}</h1>
            <div class="project-date"><time datetime="{date}">{date}</time></div>
          </div>
        </header>
        <section class="project-summary" style="margin-top: 16px;">
          {content}
        </section>
      </article>
      <div style="margin-top: 24px;">
        <a href="/blog/index.html" class="btn btn-outline">← Back to blog</a>
      </div>
    </main>
    <footer>
      <div>
        © <span id="year">2026</span> Pranav Purwar. Hosted on <a href="https://github.com/PranavPurwar" target="_blank">GitHub Pages</a>.
      </div>
      <div class="footer-links">
        <a href="/cv.pdf" download>Download CV (PDF)</a>
        <a href="/donate.html">Sponsor / Donate</a>
        <a href="mailto:purwarpranav80@gmail.com">Contact</a>
      </div>
    </footer>
  </div>
  <script>document.getElementById('year').textContent=new Date().getFullYear();</script>
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
