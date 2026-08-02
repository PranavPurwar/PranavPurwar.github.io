#!/usr/bin/env python3
"""Build site helper: convert Markdown posts, regenerate blog index and RSS.
"""
import os
import re
from datetime import datetime
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
        '<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Blog — Pranav Purwar</title><style>body{font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;sans-serif;background:#0b0c0e;color:#eef0f2;margin:0;padding:28px}.wrap{max-width:880px;margin:0 auto}a{color:#3b82f6;text-decoration:none}header{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px}.post{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.03);padding:18px;border-radius:10px;margin-bottom:12px}time{color:#98a0a6;font-family:JetBrains Mono}</style></head>',
        '<body><div class="wrap">',
        '<header><h1>Blog</h1><nav><a href="/index.html">Back</a></nav></header>',
        '<section>'
    ]
    for p in posts:
        lines.append('<article class="post">')
        lines.append(f'<h2><a href="{p["file"]}">{p["title"]}</a></h2>')
        if p.get('date'):
            lines.append(f'<div><time datetime="{p["date"]}">{p["date"]}</time></div>')
        lines.append('</article>')
    lines.append('</section></div></body></html>')
    with open(BLOG_INDEX, 'w', encoding='utf8') as f:
        f.write('\n'.join(lines))
    print('Wrote', BLOG_INDEX)


def regen_rss(posts):
    os.makedirs(os.path.dirname(RSS_OUT), exist_ok=True)
    now = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S +0000')
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
