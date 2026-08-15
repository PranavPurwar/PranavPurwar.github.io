#!/usr/bin/env python3
"""Build site helper: convert Markdown posts, regenerate blog index and RSS.
"""
import os
import re
from datetime import datetime, timezone
ROOT = os.path.dirname(os.path.dirname(__file__))
POSTS_DIR = os.path.join(ROOT, 'posts')
POSTS_MD = os.path.join(ROOT, 'posts_md')
BLOG_INDEX = os.path.join(ROOT, 'blog', 'index.html')
RSS_OUT = os.path.join(ROOT, 'blog', 'rss.xml')


def list_posts():
    posts = []
    if not os.path.isdir(POSTS_DIR):
        return posts
    for fn in os.listdir(POSTS_DIR):
        if not fn.endswith('.html'):
            continue
        path = os.path.join(POSTS_DIR, fn)
        # read title and date from file (title in <title>)
        try:
            with open(path, 'r', encoding='utf8') as f:
                txt = f.read()
            m = re.search(r'<title>(.*?)</title>', txt, re.I)
            title = m.group(1) if m else fn.replace('.html','')
        except Exception:
            title = fn.replace('.html','')
        # date from filename if present
        date = fn.split('-')[0] if '-' in fn else ''
        posts.append({'file': '/posts/' + fn, 'title': title, 'date': date})
    posts.sort(key=lambda p: p.get('date',''), reverse=True)
    return posts


def regen_index(posts):
    os.makedirs(os.path.dirname(BLOG_INDEX), exist_ok=True)
    lines = [
        '<!doctype html>',
        '<html lang="en">',
        '<head>',
        '  <meta charset="utf-8">',
        '  <meta name="viewport" content="width=device-width,initial-scale=1">',
        '  <title>Blog — Pranav Purwar</title>',
        '  <link rel="preconnect" href="https://fonts.googleapis.com">',
        '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">',
        '  <link rel="stylesheet" href="/styles.css">',
        '</head>',
        '<body>',
        '  <div class="container">',
        '    <nav class="nav-header">',
        '      <a href="/" class="nav-brand">',
        '        <div class="avatar-box"><img src="https://avatars.githubusercontent.com/u/75154889?v=4" alt="Pranav Purwar"></div>',
        '        <div class="brand-meta">',
        '          <span class="brand-title">Pranav Purwar</span>',
        '          <span class="brand-handle">@invokevirtual</span>',
        '        </div>',
        '      </a>',
        '      <div class="nav-links">',
        '        <a href="/" class="nav-link">Home</a>',
        '        <a href="/blog/index.html" class="nav-link">Blog</a>',
        '        <a href="/cv.pdf" class="btn" download>CV</a>',
        '        <a href="/donate.html" class="btn btn-primary">Sponsor</a>',
        '      </div>',
        '    </nav>',
        '    <div class="hero-section">',
        '      <h1 class="hero-title">Blog</h1>',
        '      <p class="hero-subtitle">Notes and technical writings on JVM internals, compiler toolchains, ART runtime mechanics, and Android virtualization.</p>',
        '    </div>',
        '    <section id="posts" class="section">',
        '      <div class="section-header">',
        '        <h2 class="section-title">All Posts</h2>',
        '      </div>',
        '      <div class="projects-feed">'
    ]
    for p in posts:
        date_str = p.get('date', '')
        lines.append(f'        <a href="{p["file"]}" class="project-item">')
        lines.append('          <div class="project-header">')
        lines.append(f'            <span class="project-name">{p["title"]} <span class="arrow-icon">↗</span></span>')
        if date_str:
            lines.append(f'            <span class="project-date">{date_str}</span>')
        lines.append('          </div>')
        lines.append('          <p class="project-desc">Notes on Android, JVM internals, and systems development.</p>')
        lines.append('        </a>')
    lines.extend([
        '      </div>',
        '    </section>',
        '    <footer>',
        '      <div>',
        '        © <span id="year">2026</span> Pranav Purwar. Hosted on <a href="https://github.com/PranavPurwar" target="_blank">GitHub Pages</a>.',
        '      </div>',
        '      <div class="footer-links">',
        '        <a href="/cv.pdf" download>CV</a>',
        '        <a href="/donate.html">Sponsor</a>',
        '        <a href="mailto:purwarpranav80@gmail.com">Contact</a>',
        '      </div>',
        '    </footer>',
        '  </div>',
        '  <script>document.getElementById(\'year\').textContent=new Date().getFullYear();</script>',
        '</body>',
        '</html>'
    ])
    with open(BLOG_INDEX, 'w', encoding='utf8') as f:
        f.write('\n'.join(lines))
    print('Wrote', BLOG_INDEX)


def regen_rss(posts):
    os.makedirs(os.path.dirname(RSS_OUT), exist_ok=True)
    now = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S +0000')
    lines = [
        '<?xml version="1.0" encoding="UTF-8" ?>',
        '<rss version="2.0"><channel>',
        '<title>Pranav Purwar — Blog</title>',
        '<link>https://pranavpurwar.github.io/blog/</link>',
        '<description>Technical posts and updates</description>',
        f'<lastBuildDate>{now}</lastBuildDate>'
    ]
    for p in posts:
        item = f'<item><title>{escape_xml(p["title"])}</title><link>https://pranavpurwar.github.io{p["file"]}</link>'
        if p.get('date'):
            item += f'<pubDate>{p["date"]}</pubDate>'
        item += '</item>'
        lines.append(item)
    lines.append('</channel></rss>')
    with open(RSS_OUT, 'w', encoding='utf8') as f:
        f.write('\n'.join(lines))
    print('Wrote', RSS_OUT)


def escape_xml(s):
    return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')


if __name__ == '__main__':
    # Prefer the installed markdown generator; fallback to zero-dep
    try:
        from tools import generate_posts as gen
        gen.convert_all()
    except Exception:
        try:
            from tools import generate_posts_zero as gen0
            gen0.convert_all()
        except Exception:
            # try to import as script
            import importlib.util
            spec = importlib.util.spec_from_file_location('gp0', os.path.join(ROOT, 'tools', 'generate_posts_zero.py'))
            gp0 = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(gp0)
            gp0.convert_all()

    posts = list_posts()
    regen_index(posts)
    regen_rss(posts)
    print('Build complete')
