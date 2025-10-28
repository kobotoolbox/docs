#!/usr/bin/env python3
"""
Script to update absolute support.kobotoolbox.org URLs in translated files
to include the language code in the path.
"""
import os
import re
import glob

base_dir = "/Users/josh/Desktop/work/repos/docs"

# Language mappings
languages = {
    'es': 'es',
    'fr': 'fr',
    'ar': 'ar'
}

for lang_code, lang_path in languages.items():
    locale_dir = os.path.join(base_dir, f"locales/{lang_code}")
    markdown_files = glob.glob(os.path.join(locale_dir, "*.md"))
    
    print(f"\n{lang_code.upper()}: Processing {len(markdown_files)} files...")
    updated_count = 0
    
    for md_file in markdown_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match: https://support.kobotoolbox.org/article_name.html
        # Replace with: https://support.kobotoolbox.org/lang/article_name.html
        # But NOT if it already has a language code
        
        pattern = r'https://support\.kobotoolbox\.org/(?!es/|fr/|ar/)([a-zA-Z0-9_-]+\.html)'
        replacement = f'https://support.kobotoolbox.org/{lang_path}/\\1'
        
        content = re.sub(pattern, replacement, content)
        
        # Write back if changed
        if content != original_content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            print(f"  ✓ Updated: {os.path.basename(md_file)}")
    
    print(f"  Total updated: {updated_count} files")

print("\n✓ All absolute support.kobotoolbox.org URLs updated with language paths")
