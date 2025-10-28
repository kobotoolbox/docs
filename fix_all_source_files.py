#!/usr/bin/env python3
"""
Fix all English source files to have proper formatting:
1. Move existing language links to after Last updated
2. Replace with proper English language switcher  
3. Ensure blank lines for readability
"""
import os
import re
from pathlib import Path

SOURCE_DIR = Path("/Users/josh/Desktop/work/repos/docs/source")
LOCALES_DIR = Path("/Users/josh/Desktop/work/repos/docs/locales")

# English language switcher template
LANG_LINKS_EN = '<a href="es/{filename}.html">Leer en español</a> | <a href="fr/{filename}.html">Lire en français</a> | <a href="ar/{filename}.html">اقرأ باللغة العربية</a>'

def file_has_translations(filename):
    """Check if a file exists in all three locale directories."""
    es_exists = (LOCALES_DIR / "es" / filename).exists()
    fr_exists = (LOCALES_DIR / "fr" / filename).exists()
    ar_exists = (LOCALES_DIR / "ar" / filename).exists()
    return es_exists and fr_exists and ar_exists

def fix_file(filepath):
    """Fix the formatting of an English source file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    if len(lines) < 3:
        print(f"⚠️  Skipping {filepath.name} (too short)")
        return False
    
    # Expected structure from commit 050dcc9:
    # Line 0: # Title
    # Line 1: <a href="fr/...> (old language links on same line as Last updated)
    # Line 2: **Last updated:**... (or may be merged with line 1)
    # Line 3: blank or content
    
    base_filename = filepath.stem
    
    # Check if already has the correct English format (English links should have es/ first)
    if '<a href="es/' in lines[1] if len(lines) > 1 else False:
        # Already in correct format
        print(f"⏭️  {filepath.name} already in correct format")
        return False
    
    new_lines = []
    i = 0
    
    # Line 0: Keep title as is
    new_lines.append(lines[i])
    i += 1
    
    # Find and process the Last updated line (might be on line 1 or 2)
    last_updated_line = None
    content_start_idx = None
    
    for j in range(i, min(i + 3, len(lines))):
        if '**Last updated:**' in lines[j]:
            # Extract just the Last updated part
            last_updated_match = re.search(r'\*\*Last updated:\*\*.*?</a>', lines[j])
            if last_updated_match:
                last_updated_line = last_updated_match.group(0)
                # Update the date and commit hash to latest
                last_updated_line = re.sub(
                    r'blob/[a-f0-9]+/',
                    'blob/050dcc9c8bfb4c528208bbe886979999037f1554/',
                    last_updated_line
                )
                last_updated_line = re.sub(
                    r'>\d{1,2} \w+ \d{4}</a>',
                    '>28 Oct 2025</a>',
                    last_updated_line
                )
            content_start_idx = j + 1
            break
    
    if not last_updated_line:
        print(f"⚠️  No Last updated found in {filepath.name}")
        return False
    
    # Add Last updated line
    new_lines.append(last_updated_line)
    new_lines.append('')  # Blank line
    
    # Add English language switcher
    lang_links = LANG_LINKS_EN.format(filename=base_filename)
    new_lines.append(lang_links)
    new_lines.append('')  # Blank line before content
    
    # Add remaining content (skip old language links and empty lines)
    for j in range(content_start_idx, len(lines)):
        line = lines[j]
        # Skip old language links
        if '<a href="fr/' in line or '<a href="es/' in line or '<a href="ar/' in line:
            if 'Lire en français' in line or 'Leer en español' in line or 'اقرأ باللغة العربية' in line:
                continue
        # Skip duplicate blank lines at start of content
        if j == content_start_idx and line.strip() == '':
            continue
        new_lines.append(line)
    
    # Write back
    new_content = '\n'.join(new_lines)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Fixed {filepath.name}")
    return True

def main():
    """Process all markdown files in the source directory."""
    md_files = list(SOURCE_DIR.glob("*.md"))
    
    print(f"Found {len(md_files)} markdown files in source/")
    print(f"Fixing files that have translations...\n")
    
    fixed_count = 0
    skipped_count = 0
    
    for md_file in sorted(md_files):
        # Check if this file has translations
        if not file_has_translations(md_file.name):
            skipped_count += 1
            continue
        
        if fix_file(md_file):
            fixed_count += 1
        else:
            skipped_count += 1
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  ✅ Fixed: {fixed_count} files")
    print(f"  ⏭️  Skipped: {skipped_count} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
