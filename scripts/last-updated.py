#!/usr/bin/env python3

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
GIT_CMD = ['git', 'log', '-2', '--oneline', '--pretty="%H, %cD, %s"']
GIT_IGNORE_HASH = '74dc12829b7ae2ce0c6c36364c5791b9f94d489d'
GIT_IGNORE_MSG = 'last updated'
RECENTLY_UPDATED_FILE = 'source/recently_updated.md'
FILES_IGNORE = [RECENTLY_UPDATED_FILE]
DATE_STRING_FMT = '%d %b %Y'


files_by_date = []


def get_link(_hash, path):
    return f'https://github.com/kobotoolbox/docs/blob/{_hash}/{path}'


def get_git_data(path):
    stdout = (
        subprocess.run(GIT_CMD + [path], capture_output=True)
        .stdout.decode()
        .split('\n')[:-1]
    )
    if len(stdout) == 1:
        latest, _next = stdout[0], ''
    else:
        latest, _next = stdout

    _hash, date, msg = re.search(COMMIT_PATTERN, latest).groups()
    if not _hash.startswith(GIT_IGNORE_HASH) and not msg.startswith(
        GIT_IGNORE_MSG
    ):
        return _hash, date
    return re.search(COMMIT_PATTERN, _next).groups()[:2]


def get_text(date, link):
    return f'**Last updated:** <a href="{link}" class="reference">{date}</a>\n'


def update_file(path):
    _hash, date = get_git_data(path)

    files_by_date.append(
        {
            'path': path,
            'date': datetime.strptime(date, DATE_STRING_FMT),
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
        date=datetime.strftime(file['date'], DATE_STRING_FMT),
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
        update_file(path)
    else:
        for path in glob(GLOB_PATTERN):
            if path not in FILES_IGNORE:
                update_file(path)
        create_recently_updated()
    sys.stdout.write('Done 🎉\n')


if __name__ == '__main__':
    main()
