#!/usr/bin/env python3

# TODO: please describe what this file does :)

import argparse
import os
import re
import subprocess
import sys
from datetime import datetime
from glob import glob


GLOB_PATTERN = 'source/*.md'
COMMIT_PATTERN = (
    r'([a-z0-9]{40}),\s[\w]+,\s([0-9]{1,2}\s[\w]{3}\s[0-9]{4}).*,\s(.*)'
)
GIT_CMD = ['git', 'log', '-100', '--pretty=%H, %cD, %s']
GIT_IGNORE_HASHES = [
    '74dc12829b7ae2ce0c6c36364c5791b9f94d489d',
    'bd2708397b2a21ea9fd7699ff0e50cbc3899ad63',
    'dead802312349a42727c6f3339d45892db4cabce',
    '150a514b59fe22d6efd5c4c83960ecad1e69424b',
    '050dcc9c8bfb4c528208bbe886979999037f1554',
    '9a0c5d15e0df2e44e1583add28ca880be7a7014e',
    '01270a828ec846731411368326ba58114adda98e',
    '0050a936217ec4b5b9cf44a66826778898ed29d5',
    'c8c238efa59b04f403f13c150b018e1807c66d5c',
]
GIT_IGNORE_MSG = 'last updated'
RECENTLY_UPDATED_FILE = 'source/recently_updated.md'
FILES_IGNORE = [RECENTLY_UPDATED_FILE]
DATE_STRING_IN_FMT = '%d %b %Y'
DATE_STRING_OUT_FMT = '%-d %b %Y'


files_by_date = []


def get_link(_hash, path):
    return f'https://github.com/kobotoolbox/docs/blob/{_hash}/{path}'


def get_git_data(path):
    # Run git and get output lines. Use splitlines() to be robust.
    proc = subprocess.run(GIT_CMD + [path], capture_output=True)
    stdout = proc.stdout.decode().splitlines()

    # Iterate lines instead of recursive calls. Be defensive: strip quotes
    # (the pretty format used to include quotes in some environments) and
    # skip empty or non-matching lines.
    for line in stdout:
        if not line or not line.strip():
            continue
        # Remove surrounding double-quotes if present
        line = line.strip().strip('"')
        m = re.search(COMMIT_PATTERN, line)
        if not m:
            continue
        _hash, date, msg = m.groups()
        if any(_hash.startswith(h) for h in GIT_IGNORE_HASHES) or msg.startswith(GIT_IGNORE_MSG):
            continue
        return _hash, date

    # If nothing matched, return (None, None) so caller can skip updating.
    return None, None


def get_text(date, link):
    return f'**Last updated:** <a href="{link}" class="reference">{date}</a>\n'


def update_file(path):
    # Only operate on markdown source files
    if not path.endswith('.md'):
        sys.stdout.write(f'Skipping non-markdown file: {path}\n')
        return
    
    _hash, date = get_git_data(path)

    # If git returned nothing suitable, skip the file instead of crashing
    if not _hash or not date:
        sys.stdout.write(f'No git data for {path}, skipping\n')
        return

    files_by_date.append(
        {
            'path': path,
            'date': datetime.strptime(date, DATE_STRING_IN_FMT),
        }
    )

    link = get_link(_hash, path)
    text = get_text(date, link)

    with open(path, 'r') as f:
        fs = f.readlines()

    # if `prettier` has been used, just remove the three lines
    if 'Last updated' in fs[2]:
        # if the link is up-to-date, carry on
        if link in fs[3]:
            return
        fs = [fs[0]] + fs[5:]

    if 'Last updated' in fs[1]:
        if fs[1] == text:
            return
        fs[1] = text
    else:
        fs.insert(1, text)

    with open(path, 'w') as f:
        sys.stdout.write(f'Updating: {path}\n')
        f.write(''.join(fs))


def get_title(path):
    with open(path, 'r') as f:
        first = f.readline()
    return first.replace('# ', '').strip()


def get_recently_updated_item(file):
    return '1. [{title}]({filename}) ({date})\n'.format(
        title=get_title(file['path']),
        filename=os.path.basename(file['path']),
        date=datetime.strftime(file['date'], DATE_STRING_OUT_FMT),
    )


def create_recently_updated():
    files_by_date.sort(key=lambda x: x['date'], reverse=True)
    top_ten = files_by_date[:10]
    with open(RECENTLY_UPDATED_FILE, 'r') as f:
        preamble = f.readlines()[:3]

    for file in top_ten:
        preamble.append(get_recently_updated_item(file))

    with open(RECENTLY_UPDATED_FILE, 'w') as f:
        f.write(''.join(preamble))


def main():
    parser = argparse.ArgumentParser(
        description='A CLI tool to update article "Last updated" dates.'
    )
    parser.add_argument('--file-path', '-f', type=str, help='Path to file')
    args = parser.parse_args()

    path = args.file_path
    if path:
        if not os.path.exists(path):
            os.sys.exit()
        # ensure we only handle markdown files when a single file is passed
        if not path.endswith('.md'):
            sys.stdout.write(f'Skipping non-markdown file: {path}\n')
            os.sys.exit()
        update_file(path)
    else:
        for path in glob(GLOB_PATTERN):
            if path not in FILES_IGNORE:
                update_file(path)
        create_recently_updated()
    sys.stdout.write('Done 🎉\n')


if __name__ == '__main__':
    main()
