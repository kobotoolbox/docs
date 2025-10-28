#!/usr/bin/env python3
import os
import glob

base_dir = "/Users/josh/Desktop/work/repos/docs"
source_dir = os.path.join(base_dir, "source")

# Get all English markdown files
english_files = glob.glob(os.path.join(source_dir, "*.md"))

for eng_file in english_files:
    filename = os.path.basename(eng_file)
    
    # Read the file
    with open(eng_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has language links
    if "Lire en français" in content or "Leer en español" in content:
        continue
    
    # Check if translations exist
    has_es = os.path.exists(os.path.join(base_dir, "locales/es", filename))
    has_fr = os.path.exists(os.path.join(base_dir, "locales/fr", filename))
    has_ar = os.path.exists(os.path.join(base_dir, "locales/ar", filename))
    
    # Only add links if at least one translation exists
    if not (has_es or has_fr or has_ar):
        continue
    
    # Build the language links
    links = []
    base_name = filename.replace('.md', '.html')
    
    if has_fr:
        links.append(f'<a href="fr/{base_name}">Lire en français</a>')
    if has_es:
        links.append(f'<a href="es/{base_name}">Leer en español</a>')
    if has_ar:
        links.append(f'<a href="ar/{base_name}">اقرأ باللغة العربية</a>')
    
    language_line = " | ".join(links)
    
    # Split content into lines
    lines = content.split('\n')
    
    # Insert language switcher after the first line (title)
    if len(lines) > 0:
        lines.insert(1, language_line)
        new_content = '\n'.join(lines)
        
        # Write back to file
        with open(eng_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated: {filename}")

print("Done! Language switcher links added to English files with translations.")
