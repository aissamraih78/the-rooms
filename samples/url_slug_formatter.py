"""
High-Performance SEO URL Slug Formatter — SyntaxCraft SEO Tools
Transforms raw product titles or article headings into clean,
search-engine-optimized URL slugs without stopwords, special characters,
or accents. Operates locally on your own store URLs.

Usage:
    python url_slug_formatter.py --title "Men's Vintage Leather Briefcase & Messenger Bag!"
    python url_slug_formatter.py --file titles.csv
    python url_slug_formatter.py  (demo mode with built-in sample)

Author: SyntaxCraft Studio | contact@syntaxcraft.dev
"""

import re
import unicodedata
import argparse
import json
import sys

STOPWORDS = {
    'a', 'an', 'and', 'the', 'in', 'on', 'at', 'to', 'for', 'of', 'with',
    'by', 'from', 'is', 'are', 'was', 'were', 'it', 'its', 'as', 'that'
}

def clean_slug(title: str, remove_stopwords: bool = True, max_length: int = 70) -> dict:
    original = title.strip()
    # Normalize unicode (accents -> ascii)
    normalized = unicodedata.normalize('NFKD', original)
    ascii_text = normalized.encode('ascii', errors='replace').decode('utf-8')

    # Replace replacement bytes/question marks from encoding
    ascii_text = ascii_text.replace('?', '')

    # Lowercase & remove non-alphanumeric except spaces and hyphens
    clean = re.sub(r'[^a-zA-Z0-9\s\-]', '', ascii_text).lower()
    words = clean.split()

    if remove_stopwords:
        filtered = [w for w in words if w not in STOPWORDS]
        if filtered:
            words = filtered

    slug = '-'.join(words)
    slug = re.sub(r'\-+', '-', slug).strip('-')

    if len(slug) > max_length:
        slug = slug[:max_length].rsplit('-', 1)[0]

    return {
        "original_title": original,
        "optimized_slug": slug,
        "char_count": len(slug),
        "word_count": len(slug.split('-')) if slug else 0,
        "is_seo_optimal": len(slug) <= 60
    }

def main():
    parser = argparse.ArgumentParser(
        description="SyntaxCraft URL Slug Formatter — Converts titles to SEO-friendly slugs.",
        epilog="Run with no arguments for a built-in demo."
    )
    parser.add_argument("--title", help="Single product title to slugify")
    parser.add_argument("--file", help="CSV or TXT file with titles (one per line; CSV: first column used)")
    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"[ERROR] File not found: {args.file}", file=sys.stderr)
            sys.exit(1)

        titles = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            # If CSV, use the first column (strip quotes)
            first_col = line.split(',')[0].strip().strip('"').strip("'")
            if first_col:
                titles.append(first_col)

        results = [clean_slug(t) for t in titles]
        print(json.dumps(results, indent=2, ensure_ascii=False))

    elif args.title:
        print(json.dumps(clean_slug(args.title), indent=2, ensure_ascii=False))

    else:
        # Demo mode — runs with no arguments
        print("[INFO] Running in demo mode. Use --title or --file to process your data.\n")
        sample = "Handcrafted Vintage Leather Messenger Bag for Men (Brown, 15-inch Laptop)!"
        result = clean_slug(sample)
        print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
