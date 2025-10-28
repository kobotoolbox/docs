#!/usr/bin/env python3
"""
Fix all English source files - transform from old format to new format:
OLD (from 050dcc9):
  Line 1: # Title
  Line 2: <a href="fr/...>...<a href="es/...>...<a href="ar/...>
  Line 3: **Last updated:**...
  Line 4+: content

NEW (target):
  Line 1: # Title
  Line 2: **Last updated:** (with updated date)
  Line 3: (blank)
  Line 4: <a href="es/...>Leer en español</a> | <a href="fr/...>Lire en français</a> | <a href="ar/...>اقرأ باللغة العربية</a>
  Line 5: (blank)
  Line 6+: content
"""
import os
import re
from pathlib import Path

SOURCE_DIR = Path("/Users/josh/Desktop/work/repos/docs/source")
LOCALES_DIR = Path("/Users/josh/Desktop/work/repos/docs/locales")

def file_has_translations(filename):
    """Check if a file exists in all three locale directories."""
    return (LOCALES_DIR / "es" / filename).exists() and \
           (LOCALES_DIR / "fr" / filename).exists() and \
           (LOCALES_DIR / "ar" / filename).exists()

def fix_file(filepath):
    """Transform file from old to new format."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    base_filename = filepath.stem
    
    # Check if already in new format (English links first: es/ fr/ ar/)
    if len(lines) > 3 and '<a href="es/' in lines[3]:
        print(f"⏭️  {filepath.name} already in new format")
        return False
    
    # Check for old format (translation links: fr/ es/ ar/)
    if len(lines) < 3 or not ('<a href="fr/' in lines[1] or '<a href="es/' in lines[1]):
        print(f"⚠️  {filepath.name} has unexpected format")
        return False
    
    # Build new content
    new_lines = []
    
    # Line 1: Title (keep as is)
    new_lines.append(lines[0])
    
    # Line 2: Last updated (extract from line 2 or 3, update date)
    last_updated = None
    for i in [1, 2]:
        if i < len(lines) and '**Last updated:**' in lines[i]:
            # Extract and update
            match = re.search(r'\*\*Last updated:\*\*\s*<a href="[^"]+"\s+class="reference">[^<]+</a>', lines[i])
            if match:
                last_updated = match.group(0)
                # Update to latest
                last_updated = re.sub(
                    r'blob/[a-f0-9]+/',
                    'blob/050dcc9c8bfb4c528208bbe886979999037f1554/',
                    last_updated
                )
                last_updated = re.sub(
                    r'>\d{1,2} \w+ \d{4}</a>',
                    '>28 Oct 2025</a>',
                    last_updated
                )
                break
    
    if not last_updated:
        # Create new one
        last_updated = f'**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/050dcc9c8bfb4c528208bbe886979999037f1554/source/{base_filename}.md" class="reference">28 Oct 2025</a>'
    
    new_lines.append(last_updated)
    new_lines.append('')  # Blank line
    
    # Line 4: English language switcher
    lang_links = f'<a href="es/{base_filename}.html">Leer en español</a> | <a href="fr/{base_filename}.html">Lire en français</a> | <a href="ar/{base_filename}.html">اقرأ باللغة العربية</a>'
    new_lines.append(lang_links)
    new_lines.append('')  # Blank line
    
    # Rest: content (start from first non-meta line)
    content_start = 3
    if content_start < len(lines):
        # Skip any blank lines at start of content
        while content_start < len(lines) and lines[content_start].strip() == '':
            content_start += 1
        # Add all remaining content
        new_lines.extend(lines[content_start:])
    
    # Write back
    new_content = '\n'.join(new_lines)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Fixed {filepath.name}")
    return True

def main():
    """Process all markdown files."""
    md_files = list(SOURCE_DIR.glob("*.md"))
    
    print(f"Found {len(md_files)} markdown files")
    print(f"Fixing files with translations...\n")
    
    fixed = 0
    skipped = 0
    
    for md_file in sorted(md_files):
        if not file_has_translations(md_file.name):
            skipped += 1
            continue
        
        if fix_file(md_file):
            fixed += 1
        else:
            skipped += 1
    
    print(f"\n{'='*60}")
    print(f"✅ Fixed: {fixed} | ⏭️  Skipped: {skipped}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
