#!/usr/bin/env python3
"""
Add language switcher links to English source files that have translations.
"""
import os
from pathlib import Path

# Base directories
SOURCE_DIR = Path("/Users/josh/Desktop/work/repos/docs/source")
LOCALES_DIR = Path("/Users/josh/Desktop/work/repos/docs/locales")

# Language switcher template for English files
# Format: <a href="es/filename.html">Leer en español</a> | <a href="fr/filename.html">Lire en français</a> | <a href="ar/filename.html">اقرأ باللغة العربية</a>
LANG_LINKS_TEMPLATE = '<a href="es/{filename}.html">Leer en español</a> | <a href="fr/{filename}.html">Lire en français</a> | <a href="ar/{filename}.html">اقرأ باللغة العربية</a>'

def file_has_translations(filename):
    """Check if a file exists in all three locale directories."""
    es_exists = (LOCALES_DIR / "es" / filename).exists()
    fr_exists = (LOCALES_DIR / "fr" / filename).exists()
    ar_exists = (LOCALES_DIR / "ar" / filename).exists()
    return es_exists and fr_exists and ar_exists

def has_language_links(content):
    """Check if the file already has language switcher links."""
    return 'Leer en español' in content or 'href="es/' in content

def add_language_links(filepath):
    """Add language switcher links to an English source file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has language links
    if has_language_links(content):
        print(f"⏭️  Skipping {filepath.name} (already has language links)")
        return False
    
    lines = content.split('\n')
    
    # Find the line with "Last updated:" and insert language links after it
    for i, line in enumerate(lines):
        if '**Last updated:**' in line:
            # Get the base filename without extension
            base_filename = filepath.stem
            
            # Create the language links
            lang_links = LANG_LINKS_TEMPLATE.format(filename=base_filename)
            
            # Insert a blank line and the language links after the "Last updated" line
            lines.insert(i + 1, '')
            lines.insert(i + 2, lang_links)
            
            # Write back to file
            new_content = '\n'.join(lines)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Added language links to {filepath.name}")
            return True
    
    print(f"⚠️  Could not find 'Last updated:' in {filepath.name}")
    return False

def main():
    """Process all markdown files in the source directory."""
    md_files = list(SOURCE_DIR.glob("*.md"))
    
    print(f"Found {len(md_files)} markdown files in source/")
    print(f"Processing files that have translations in all three locales...\n")
    
    updated_count = 0
    skipped_count = 0
    no_translations_count = 0
    
    for md_file in sorted(md_files):
        # Check if this file has translations in all three locales
        if not file_has_translations(md_file.name):
            no_translations_count += 1
            continue
        
        if add_language_links(md_file):
            updated_count += 1
        else:
            skipped_count += 1
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  ✅ Updated: {updated_count} files")
    print(f"  ⏭️  Skipped: {skipped_count} files (already had links)")
    print(f"  ⊘  No translations: {no_translations_count} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
