#!/usr/bin/env python3
"""
Script to replace absolute support.kobotoolbox.org URLs with relative links
when the target file exists in the same language directory.
"""
import os
import re
import glob

base_dir = "/Users/josh/Desktop/work/repos/docs"

languages = ['es', 'fr', 'ar']

for lang in languages:
    locale_dir = os.path.join(base_dir, f"locales/{lang}")
    markdown_files = glob.glob(os.path.join(locale_dir, "*.md"))
    
    # Get list of all translated file names (without extension)
    translated_files = set()
    for md_file in markdown_files:
        filename = os.path.basename(md_file).replace('.md', '')
        translated_files.add(filename)
    
    print(f"\n{lang.upper()}: Processing {len(markdown_files)} files...")
    updated_count = 0
    
    for md_file in markdown_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern 1: Match absolute URLs in markdown links [text](https://support.kobotoolbox.org/lang/article.html)
        def replace_absolute_md_link(match):
            link_text = match.group(1)
            article_name = match.group(2)
            
            # Check if this article exists in current language
            if article_name in translated_files:
                # Replace with relative link
                return f'[{link_text}]({article_name}.md)'
            else:
                # Keep absolute URL but ensure it has language code
                return match.group(0)
        
        # Pattern for markdown links: [text](https://support.kobotoolbox.org/lang/article.html)
        pattern1 = r'\[([^\]]+)\]\(https://support\.kobotoolbox\.org/(?:es|fr|ar)/([a-zA-Z0-9_-]+)\.html\)'
        content = re.sub(pattern1, replace_absolute_md_link, content)
        
        # Pattern 2: Match absolute URLs in HTML links <a href="https://support.kobotoolbox.org/lang/article.html">
        def replace_absolute_html_link(match):
            article_name = match.group(1)
            link_text = match.group(2)
            
            # Check if this article exists in current language
            if article_name in translated_files:
                # Replace with relative link
                return f'<a href="{article_name}.html">{link_text}</a>'
            else:
                # Keep absolute URL but ensure it has language code
                return match.group(0)
        
        # Pattern for HTML links
        pattern2 = r'<a href="https://support\.kobotoolbox\.org/(?:es|fr|ar)/([a-zA-Z0-9_-]+)\.html">([^<]+)</a>'
        content = re.sub(pattern2, replace_absolute_html_link, content)
        
        # Write back if changed
        if content != original_content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            print(f"  ✓ Updated: {os.path.basename(md_file)}")
    
    print(f"  Total updated: {updated_count} files")

print("\n✓ Absolute URLs replaced with relative links where possible")
