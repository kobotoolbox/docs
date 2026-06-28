#!/usr/bin/env python3
"""Compile the articles linked from a quicklinks markdown file into one PDF.

A "quicklinks" file (e.g. quicklinks_venezuela_terremoto.md) is a curated,
ordered list of links to support.kobotoolbox.org articles. This script resolves
each link to its local source markdown, stitches them together — preserving the
quicklinks intro text, section headings, and per-link notes — and renders a
single distributable PDF.

Link resolution
---------------
  https://support.kobotoolbox.org/es/welcome.html  -> locales/es/welcome.html
  https://support.kobotoolbox.org/welcome.html      -> source/welcome.html (English)

Pipeline
--------
  quicklinks.md  ->  combined markdown  ->  pandoc (standalone HTML, images
  embedded as base64)  ->  Chrome headless  ->  PDF

Requirements
------------
  - pandoc            (brew install pandoc)
  - Google Chrome     (headless --print-to-pdf); override with --chrome

Usage
-----
  python scripts/quicklinks_to_pdf.py quicklinks_venezuela_terremoto.md
  python scripts/quicklinks_to_pdf.py quicklinks_venezuela_terremoto.md -o out.pdf
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Matches links to support articles, with or without a two-letter locale prefix.
ARTICLE_RE = re.compile(
    r'https://support\.kobotoolbox\.org/(?:(?P<lang>[a-z]{2})/)?(?P<slug>[a-z0-9_-]+)\.html'
)

# Common Chrome locations on macOS / Linux, tried when --chrome isn't given.
CHROME_CANDIDATES = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    'google-chrome',
    'chromium',
    'chromium-browser',
]


def find_chrome(explicit):
    if explicit:
        return explicit
    for candidate in CHROME_CANDIDATES:
        if os.path.isabs(candidate):
            if os.path.exists(candidate):
                return candidate
        elif shutil.which(candidate):
            return candidate
    return None


def source_dir_for_lang(lang):
    """Return the local directory that holds articles for a given locale."""
    if lang is None:
        return os.path.join(REPO_ROOT, 'source')
    return os.path.join(REPO_ROOT, 'locales', lang)


def parse_quicklinks(path):
    """Yield ('text', line) for prose/headings and ('article', meta) for links.

    Each line is classified so we can keep the quicklinks structure (intro,
    section headings, trailing notes) around the resolved article bodies.
    """
    with open(path, encoding='utf-8') as fh:
        for raw in fh:
            line = raw.rstrip('\n')
            match = ARTICLE_RE.search(line)
            if match and line.lstrip().startswith('-'):
                lang = match.group('lang')
                slug = match.group('slug')
                src = os.path.join(source_dir_for_lang(lang), slug + '.md')
                yield 'article', {
                    'lang': lang,
                    'slug': slug,
                    'src': src,
                }
            else:
                yield 'text', line


def rewrite_image_paths(md_text):
    """Make `/images/...` references resolvable via --resource-path=source."""
    md_text = re.sub(r'(\]\()\s*/images/', r'\1images/', md_text)
    md_text = re.sub(r'(src=")\s*/images/', r'\1images/', md_text)
    return md_text


SUPPORT_BASE = 'https://support.kobotoolbox.org'


def rewrite_relative_md_links(md_text, lang):
    """Point in-article `foo.md` links at the public support site.

    Articles cross-link each other with relative paths like `(question_types.md)`
    that only resolve inside the live docs site. In a standalone PDF those are
    dead, so rewrite them to absolute support URLs (locale-aware) ending in .html.
    """
    prefix = f'/{lang}' if lang else ''

    def repl(match):
        slug = match.group('slug')
        anchor = match.group('anchor') or ''
        return f'({SUPPORT_BASE}{prefix}/{slug}.html{anchor})'

    return re.sub(
        r'\((?P<slug>[a-z0-9_-]+)\.md(?P<anchor>#[^)]*)?\)',
        repl,
        md_text,
    )


def strip_video_iframes(md_text):
    """Replace YouTube/video <iframe> embeds with a plain Markdown link.

    Iframes render as blank black boxes in a printed PDF, so swap each one for a
    readable link to the video that works on paper.
    """
    iframe_re = re.compile(r'<iframe\b[^>]*?\bsrc="(?P<src>[^"]+)"[^>]*?>\s*</iframe>',
                           re.IGNORECASE | re.DOTALL)

    def repl(match):
        src = match.group('src')
        # Normalize a YouTube embed URL to a regular watch URL.
        embed = re.search(r'youtube(?:-nocookie)?\.com/embed/([\w-]+)', src)
        if embed:
            url = f'https://www.youtube.com/watch?v={embed.group(1)}'
            return f'\n\n[▶ Ver el video en YouTube]({url})\n\n'
        return f'\n\n[▶ Ver el video]({src})\n\n'

    return iframe_re.sub(repl, md_text)


def demote_headings(md_text, levels=1):
    """Add `levels` `#` to every ATX heading so article H1s sit under sections.

    Fenced code blocks are left untouched.
    """
    out = []
    in_fence = False
    for line in md_text.split('\n'):
        stripped = line.lstrip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence and re.match(r'#{1,6}\s', line):
            out.append('#' * levels + line)
        else:
            out.append(line)
    return '\n'.join(out)


def build_combined_markdown(quicklinks_path):
    """Stitch the quicklinks structure and resolved article bodies together.

    Returns (combined_markdown, missing_slugs, doc_title). The title is taken
    from the quicklinks file's first H1; that H1 is dropped from the body so it
    isn't repeated below the cover.
    """
    parts = []
    missing = []
    doc_title = None
    for kind, payload in parse_quicklinks(quicklinks_path):
        if kind == 'text':
            if doc_title is None and payload.startswith('# '):
                doc_title = payload[2:].strip()
                continue  # promoted to the cover title; don't repeat it
            parts.append(payload)
            continue

        src = payload['src']
        if not os.path.exists(src):
            missing.append(payload['slug'] + (f" ({payload['lang']})" if payload['lang'] else ''))
            parts.append(f"> _[Artículo no encontrado localmente: {payload['slug']}]_")
            continue

        with open(src, encoding='utf-8') as fh:
            body = fh.read()
        body = rewrite_image_paths(body)
        body = strip_video_iframes(body)
        body = rewrite_relative_md_links(body, payload['lang'])
        # Article H1 -> H2 etc. so it nests beneath the quicklinks section heading.
        body = demote_headings(body, levels=1)

        parts.append('')
        parts.append(body)
        parts.append('\n<div style="page-break-after: always;"></div>\n')

    return '\n'.join(parts), missing, doc_title


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('quicklinks', help='Path to a quicklinks_*.md file')
    ap.add_argument('-o', '--output', help='Output PDF path (default: <quicklinks>.pdf)')
    ap.add_argument('--chrome', help='Path to the Chrome/Chromium binary')
    ap.add_argument('--keep-html', action='store_true',
                    help='Also write the intermediate standalone HTML next to the PDF')
    args = ap.parse_args()

    quicklinks_path = os.path.abspath(args.quicklinks)
    if not os.path.exists(quicklinks_path):
        sys.exit(f"error: quicklinks file not found: {quicklinks_path}")

    if not shutil.which('pandoc'):
        sys.exit("error: pandoc not found on PATH (try: brew install pandoc)")

    chrome = find_chrome(args.chrome)
    if not chrome:
        sys.exit("error: Chrome/Chromium not found; pass --chrome /path/to/chrome")

    output = args.output or os.path.splitext(quicklinks_path)[0] + '.pdf'
    output = os.path.abspath(output)

    combined_md, missing, doc_title = build_combined_markdown(quicklinks_path)
    title = doc_title or os.path.splitext(os.path.basename(quicklinks_path))[0]

    with tempfile.TemporaryDirectory() as tmp:
        md_path = os.path.join(tmp, 'combined.md')
        with open(md_path, 'w', encoding='utf-8') as fh:
            fh.write(combined_md)

        html_path = os.path.join(tmp, 'combined.html')
        subprocess.run(
            [
                'pandoc', md_path,
                '--from=markdown+raw_html',
                '--standalone',
                '--embed-resources',
                '--toc', '--toc-depth=2',
                '--metadata', f'title={title}',
                '--resource-path', os.path.join(REPO_ROOT, 'source'),
                '-o', html_path,
            ],
            check=True,
        )

        if args.keep_html:
            shutil.copy(html_path, os.path.splitext(output)[0] + '.html')

        subprocess.run(
            [
                chrome,
                '--headless',
                '--disable-gpu',
                '--no-pdf-header-footer',
                f'--print-to-pdf={output}',
                'file://' + html_path,
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    if missing:
        print("warning: these linked articles were not found locally and were "
              "skipped:\n  - " + "\n  - ".join(missing), file=sys.stderr)

    print(f"Wrote {output}")


if __name__ == '__main__':
    main()
