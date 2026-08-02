#!/usr/bin/env python3
"""Zero-dependency minimal Markdown -> HTML converter for posts.
Supports headings (#), fenced code (```), lists (-, *), paragraphs, inline code (`), and links [text](url).
Not a full Markdown implementation—sufficient for simple posts.
"""
import os
import re
import html

ROOT = os.path.dirname(os.path.dirname(__file__))
MD_DIR = os.path.join(ROOT, 'posts_md')
OUT_DIR = os.path.join(ROOT, 'posts')


def slug_to_title(slug):
    return slug.replace('-', ' ').capitalize()


def convert(md):
    lines = md.splitlines()
    out = []
    i = 0
    in_code = False
    code_buf = []
    list_buf = []

    def flush_list():
        nonlocal list_buf
        if list_buf:
            out.append('<ul>')
            for item in list_buf:
                out.append('<li>%s</li>' % item)
            out.append('</ul>')
            list_buf = []

    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('```'):
            if not in_code:
                in_code = True
                code_buf = []
            else:
                # end code
                out.append('<pre><code>%s</code></pre>' % html.escape('\n'.join(code_buf)))
                in_code = False
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue
        # headings
        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            flush_list()
            level = len(m.group(1))
            text = inline_markup(m.group(2))
            out.append(f'<h{level}>{text}</h{level}>')
            i += 1
            continue
        # list item
        m = re.match(r'^[\-\*]\s+(.*)$', line)
        if m:
            list_buf.append(inline_markup(m.group(1)))
            i += 1
            # consume following list items
            while i < len(lines) and re.match(r'^[\-\*]\s+(.*)$', lines[i]):
                list_buf.append(inline_markup(re.match(r'^[\-\*]\s+(.*)$', lines[i]).group(1)))
                i += 1
            flush_list()
            continue
        # blank line
        if line.strip() == '':
            i += 1
            continue
        # paragraph (gobble consecutive lines)
        para_lines = [line]
        i += 1
        while i < len(lines) and lines[i].strip() != '':
            para_lines.append(lines[i])
            i += 1
        para = ' '.join(para_lines)
        out.append('<p>%s</p>' % inline_markup(para))
    return '\n'.join(out)


def inline_markup(text):
    # escape HTML
    text = html.escape(text)
    # links [text](url)
    text = re.sub(r'\\[([^\]]+)\\]\(([^)]+)\\)', r'<a href="\2">\1</a>', text)
    # inline code `code`
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text


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
        html_body = convert(md)
        title = fn.replace('.md','').replace('-', ' ')
        date = fn.split('-')[0] if '-' in fn else ''
        out = TEMPLATE.format(title=html.escape(title), date=html.escape(date), content=html_body)
        out_fn = os.path.join(OUT_DIR, fn.replace('.md', '.html'))
        with open(out_fn, 'w', encoding='utf8') as f:
            f.write(out)
        print('Wrote', out_fn)

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

if __name__ == '__main__':
    convert_all()
