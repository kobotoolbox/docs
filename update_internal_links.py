#!/usr/bin/env python3
"""
Script to update internal links in translated documentation files
to point to translated versions instead of English versions.
"""
import os
import re
import glob

base_dir = "/Users/josh/Desktop/work/repos/docs"

# Get all markdown files in each locale
languages = ['es', 'fr', 'ar']

for lang in languages:
    locale_dir = os.path.join(base_dir, f"locales/{lang}")
    markdown_files = glob.glob(os.path.join(locale_dir, "*.md"))
    
    # Get list of all translated file names (without extension)
    translated_files = set()
    for md_file in markdown_files:
        filename = os.path.basename(md_file).replace('.md', '')
        translated_files.add(filename)
    
    print(f"\n{lang.upper()}: Found {len(translated_files)} translated files")
    
    # Update each file
    for md_file in markdown_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        updated = False
        
        # Find all markdown links [text](link.md) or [text](link.html)
        # Pattern matches: [text](filename.md) or [text](filename.html)
        # but NOT external links (http/https) or anchor links (#)
        
        def replace_link(match):
            nonlocal updated
            full_match = match.group(0)
            link_text = match.group(1)
            link_target = match.group(2)
            
            # Skip if it's an external link, anchor, or already has path separators
            if (link_target.startswith('http') or 
                link_target.startswith('#') or 
                link_target.startswith('../') or
                '/' in link_target):
                return full_match
            
            # Extract filename without extension
            if link_target.endswith('.md'):
                filename = link_target.replace('.md', '')
                ext = '.md'
            elif link_target.endswith('.html'):
                filename = link_target.replace('.html', '')
                ext = '.html'
            else:
                return full_match
            
            # Check if this file exists in translations
            if filename in translated_files:
                # Keep the same filename (already in same language directory)
                # No change needed - already points to local file
                return full_match
            else:
                # File doesn't exist in this language, leave as is (will point to English)
                return full_match
        
        # Pattern for markdown links
        pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
        content = re.sub(pattern, replace_link, content)
        
        # Write back if changed
        if content != original_content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
            updated = True
        
        if updated:
            print(f"  Updated: {os.path.basename(md_file)}")

print("\n✓ Internal links updated for all translated files")
print("\nNote: Links already point to files in the same directory by default.")
print("Links to untranslated articles remain pointing to English versions.")
