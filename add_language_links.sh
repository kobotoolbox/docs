#!/bin/bash

# Script to add language switcher links to translated documentation files

# Process Spanish files
for file in locales/es/*.md; do
    filename=$(basename "$file")
    # Skip if already has language links
    if ! grep -q "Read in English" "$file"; then
        # Add language switcher after the first line (title) if it exists
        sed -i '' '1 a\
<a href="../'"${filename%.md}.html"'">Read in English</a> | <a href="../fr/'"${filename%.md}.html"'">Lire en français</a> | <a href="../ar/'"${filename%.md}.html"'">اقرأ باللغة العربية</a>\
' "$file"
        echo "Updated: $file"
    fi
done

# Process French files
for file in locales/fr/*.md; do
    filename=$(basename "$file")
    # Skip if already has language links
    if ! grep -q "Read in English" "$file"; then
        sed -i '' '1 a\
<a href="../'"${filename%.md}.html"'">Read in English</a> | <a href="../es/'"${filename%.md}.html"'">Leer en español</a> | <a href="../ar/'"${filename%.md}.html"'">اقرأ باللغة العربية</a>\
' "$file"
        echo "Updated: $file"
    fi
done

# Process Arabic files
for file in locales/ar/*.md; do
    filename=$(basename "$file")
    # Skip if already has language links
    if ! grep -q "Read in English" "$file"; then
        sed -i '' '1 a\
<a href="../'"${filename%.md}.html"'">Read in English</a> | <a href="../fr/'"${filename%.md}.html"'">Lire en français</a> | <a href="../es/'"${filename%.md}.html"'">Leer en español</a>\
' "$file"
        echo "Updated: $file"
    fi
done

echo "Done! Language switcher links added to all translated files."
