#!/bin/bash

# Script to add language switcher links to English documentation files
# Only adds links if corresponding translated files exist

cd /Users/josh/Desktop/work/repos/docs

# Process English files in source/
for file in source/*.md; do
    filename=$(basename "$file")
    
    # Skip if already has language links
    if grep -q "Lire en français" "$file"; then
        continue
    fi
    
    # Check if translations exist
    has_es=false
    has_fr=false
    has_ar=false
    
    [ -f "locales/es/$filename" ] && has_es=true
    [ -f "locales/fr/$filename" ] && has_fr=true
    [ -f "locales/ar/$filename" ] && has_ar=true
    
    # Only add links if at least one translation exists
    if [ "$has_es" = true ] || [ "$has_fr" = true ] || [ "$has_ar" = true ]; then
        # Build the language links
        links=""
        
        [ "$has_fr" = true ] && links="<a href=\"fr/${filename%.md}.html\">Lire en français</a>"
        [ "$has_es" = true ] && { [ -n "$links" ] && links="$links | "; links="${links}<a href=\"es/${filename%.md}.html\">Leer en español</a>"; }
        [ "$has_ar" = true ] && { [ -n "$links" ] && links="$links | "; links="${links}<a href=\"ar/${filename%.md}.html\">اقرأ باللغة العربية</a>"; }
        
        # Add language switcher after the first line (title)
        sed -i '' "1 a\\
$links\\
" "$file"
        echo "Updated: $file"
    fi
done

echo "Done! Language switcher links added to English files with translations."
