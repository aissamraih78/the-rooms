"""
Image Alt Text Optimizer — SyntaxCraft SEO Tools
Sanitizes image filenames and generates descriptive, keyword-targeted
Alt attributes compliant with WCAG accessibility and Google Image search.

Usage:
    python image_alt_optimizer.py --html page.html --keyword "leather bag" --format html
    python image_alt_optimizer.py --html page.html --keyword "bag" --output modified.html
    python image_alt_optimizer.py --dir ./pages/ --keyword "product" --format json
    python image_alt_optimizer.py  (demo mode)

Author: SyntaxCraft Studio | contact@syntaxcraft.dev
"""

import re
import json
import argparse
import sys
import os
from pathlib import Path
from typing import Optional

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".avif"}


def slugify_filename(filename: str) -> str:
    """Convert an image filename to a clean, SEO-friendly slug."""
    # Remove extension temporarily
    stem = Path(filename).stem
    clean = re.sub(r"[^a-zA-Z0-9\s\-_]", " ", stem).strip().lower()
    slug = re.sub(r"[\s_]+", "-", clean)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug


def generate_alt_text(filename: str, keyword: str) -> str:
    """Generate contextual alt text from filename and keyword."""
    stem = slugify_filename(filename)
    # Remove numeric tokens that are clearly camera-generated (e.g. IMG_2026)
    stem_clean = re.sub(r"\b(img|image|photo|pic|dsc|dsc\d+|p\d+|\d{4,})\b", "", stem)
    stem_clean = re.sub(r"-+", "-", stem_clean).strip("-")

    if stem_clean and len(stem_clean) > 3:
        context = stem_clean.replace("-", " ").title()
        return f"{keyword.title()} — {context}"
    else:
        return f"{keyword.title()} — product image"


def format_image_metadata(raw_filename: str, keyword: str) -> dict:
    """Build full metadata record for a single image filename."""
    ext = Path(raw_filename).suffix.lower()
    slug = slugify_filename(raw_filename)
    optimized_filename = slug + ".webp"  # recommend conversion to webp
    alt_text = generate_alt_text(raw_filename, keyword)

    return {
        "original_filename": raw_filename,
        "optimized_filename": optimized_filename,
        "alt_attribute": alt_text,
        "html_tag": f'<img src="/images/{optimized_filename}" alt="{alt_text}" loading="lazy" />'
    }


def process_html(html_content: str, keyword: str) -> tuple:
    """
    Find all <img> tags in HTML, inject/replace alt attributes using keyword + filename context.
    Returns (modified_html, list_of_changes).
    """
    changes = []
    img_pattern = re.compile(
        r'(<img\s[^>]*?)(?:\s+alt="[^"]*")?([^>]*>)',
        re.IGNORECASE | re.DOTALL
    )
    src_pattern = re.compile(r'src=["\']([^"\']+)["\']', re.IGNORECASE)

    def replace_img(match):
        full_tag = match.group(0)
        src_match = src_pattern.search(full_tag)
        if not src_match:
            return full_tag

        src = src_match.group(1)
        filename = Path(src).name
        ext = Path(filename).suffix.lower()

        if ext not in IMAGE_EXTENSIONS:
            return full_tag

        alt_text = generate_alt_text(filename, keyword)

        # Remove existing alt attribute
        new_tag = re.sub(r'\s+alt="[^"]*"', "", full_tag, flags=re.IGNORECASE)
        # Inject new alt before closing >
        new_tag = re.sub(r'\s*/?>$', f' alt="{alt_text}" />', new_tag.rstrip())

        changes.append({
            "src": src,
            "generated_alt": alt_text,
            "original_tag": full_tag[:100],
        })
        return new_tag

    modified = img_pattern.sub(replace_img, html_content)
    return modified, changes


def main():
    parser = argparse.ArgumentParser(
        description="SyntaxCraft Image Alt Text Optimizer",
        epilog="Run with no arguments for a built-in demo."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--html", help="Path to an HTML file to process")
    group.add_argument("--dir", help="Directory to scan for all .html files (batch mode)")
    parser.add_argument("--keyword", default="product", help="Primary SEO keyword for alt text context")
    parser.add_argument("--format", choices=["html", "json"], default="json",
                        help="Output format: 'html' prints modified HTML, 'json' prints change report")
    parser.add_argument("--output", help="Write modified HTML to this file (use with --html and --format html)")
    args = parser.parse_args()

    if args.dir:
        # Batch mode: process all HTML files in directory
        html_dir = Path(args.dir)
        if not html_dir.is_dir():
            print(f"[ERROR] Directory not found: {args.dir}", file=sys.stderr)
            sys.exit(1)

        all_results = []
        for html_file in html_dir.glob("**/*.html"):
            content = html_file.read_text(encoding="utf-8", errors="replace")
            modified, changes = process_html(content, args.keyword)
            html_file.write_text(modified, encoding="utf-8")
            all_results.append({
                "file": str(html_file),
                "images_updated": len(changes),
                "changes": changes
            })

        print(json.dumps(all_results, indent=2, ensure_ascii=False))

    elif args.html:
        try:
            content = Path(args.html).read_text(encoding="utf-8", errors="replace")
        except FileNotFoundError:
            print(f"[ERROR] File not found: {args.html}", file=sys.stderr)
            sys.exit(1)

        modified, changes = process_html(content, args.keyword)

        if args.format == "html":
            if args.output:
                Path(args.output).write_text(modified, encoding="utf-8")
                print(f"[OK] Modified HTML saved to {args.output}")
            else:
                print(modified)
        else:
            report = {
                "file": args.html,
                "keyword": args.keyword,
                "images_updated": len(changes),
                "changes": changes
            }
            if args.output:
                Path(args.output).write_text(modified, encoding="utf-8")
                print(f"[OK] Modified HTML saved to {args.output}")
            print(json.dumps(report, indent=2, ensure_ascii=False))

    else:
        # Demo mode — operate on a sample filename only
        print("[INFO] Running in demo mode. Use --html or --dir for your files.\n")
        sample_files = [
            "IMG_2026_04_leather bag preview final.png",
            "vintage-briefcase_hero.jpg",
            "product_photo_webp.webp",
            "handmade-bag-detail.jpeg",
        ]
        keyword = args.keyword
        results = [format_image_metadata(f, keyword) for f in sample_files]
        print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
