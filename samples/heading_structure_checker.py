"""
Heading Structure Checker — SyntaxCraft SEO Tools
Validates H1-H6 hierarchy in HTML content for strict WCAG 2.1 accessibility
and logical SEO heading structure. Operates on your own website's HTML files.

Usage:
    python heading_structure_checker.py --file page.html
    python heading_structure_checker.py --html "<h1>Title</h1><h3>Skipped H2!</h3>"
    python heading_structure_checker.py --file page.html --output report.json
    python heading_structure_checker.py  (demo mode)

Author: SyntaxCraft Studio | contact@syntaxcraft.dev
"""

import argparse
import json
import re
import sys
from typing import Optional


def extract_headings(html: str) -> list:
    """
    Extract all heading tags (H1-H6) from raw HTML in document order.
    Returns list of {"level": int, "text": str, "position": int}
    """
    pattern = re.compile(r"<(h[1-6])[^>]*>(.*?)</\1>", re.IGNORECASE | re.DOTALL)
    headings = []
    for i, match in enumerate(pattern.finditer(html)):
        tag = match.group(1).lower()
        level = int(tag[1])
        # Strip inner tags to get plain text
        text = re.sub(r"<[^>]+>", "", match.group(2)).strip()
        headings.append({"level": level, "text": text, "position": i + 1})
    return headings


def audit_headings(headings: list) -> dict:
    """
    Audit a list of heading entries for structural issues.

    Checks:
    - Exactly one H1
    - No skipped heading levels (e.g., H1 → H3 without H2)
    - H1 should appear before all other headings
    - No empty heading text
    - Recommend keyword placement

    Returns a full audit report dict.
    """
    errors = []
    warnings = []
    suggestions = []

    if not headings:
        return {
            "heading_count": 0,
            "errors": ["No headings found in the provided HTML."],
            "warnings": [],
            "suggestions": [],
            "headings": [],
            "score": 0,
            "status": "NO HEADINGS",
        }

    # H1 count check
    h1s = [h for h in headings if h["level"] == 1]
    if len(h1s) == 0:
        errors.append("Missing H1 tag. Every page must have exactly one H1 as the primary topic signal.")
    elif len(h1s) > 1:
        errors.append(
            f"Multiple H1 tags found ({len(h1s)}): {[h['text'][:40] for h in h1s]}. "
            "Use only one H1 per page."
        )

    # H1 should come first
    if h1s and headings[0]["level"] != 1:
        warnings.append(
            f"First heading is H{headings[0]['level']} ('{headings[0]['text'][:40]}') — "
            "H1 should be the very first heading on the page."
        )

    # Hierarchy jump detection
    prev_level = 0
    for h in headings:
        if prev_level > 0 and h["level"] > prev_level + 1:
            errors.append(
                f"Heading hierarchy skip: H{prev_level} → H{h['level']} "
                f"('{h['text'][:50]}') — H{prev_level + 1} expected between them."
            )
        prev_level = h["level"]

    # Empty headings
    for h in headings:
        if not h["text"].strip():
            errors.append(f"Empty H{h['level']} tag found at position {h['position']}.")

    # Very long headings
    for h in headings:
        if len(h["text"]) > 70 and h["level"] == 1:
            warnings.append(
                f"H1 is {len(h['text'])} chars long: '{h['text'][:60]}...' — "
                "Keep H1 under 60 characters for optimal SERP display."
            )
        elif len(h["text"]) > 100:
            warnings.append(
                f"H{h['level']} at position {h['position']} is very long ({len(h['text'])} chars). "
                "Consider splitting or shortening."
            )

    # Suggestions
    h2s = [h for h in headings if h["level"] == 2]
    if len(h2s) < 2:
        suggestions.append(
            "Add at least 2-3 H2 subheadings to clearly structure content topics "
            "and improve search engine topic comprehension."
        )
    if not any(h["level"] == 3 for h in headings) and len(headings) > 4:
        suggestions.append(
            "Consider adding H3 subheadings under each H2 section for detailed topic coverage."
        )

    # Score
    score = 100
    score -= len(errors) * 20
    score -= len(warnings) * 5
    score = max(0, min(100, score))

    return {
        "heading_count": len(headings),
        "h1_count": len(h1s),
        "h2_count": len(h2s),
        "errors": errors,
        "warnings": warnings,
        "suggestions": suggestions,
        "structure_score": score,
        "status": "VALID STRUCTURE" if score >= 80 else "REVIEW NEEDED" if score >= 50 else "CRITICAL ERRORS",
        "headings": headings,
    }


def generate_toc(headings: list) -> str:
    """Generate a Markdown Table of Contents from heading list."""
    lines = []
    for h in headings:
        indent = "  " * (h["level"] - 1)
        slug = re.sub(r"[^a-z0-9\-]", "", h["text"].lower().replace(" ", "-"))
        lines.append(f"{indent}- [{h['text']}](#{slug})")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="SyntaxCraft H1-H6 Heading Structure Checker",
        epilog="Run with no arguments for a built-in demo."
    )
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--file", help="Path to HTML file to audit")
    group.add_argument("--html", help="Raw HTML string to audit")
    parser.add_argument("--toc", action="store_true", help="Also output a Table of Contents")
    parser.add_argument("--output", help="Save report to this JSON file")
    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                html = f.read()
        except FileNotFoundError:
            print(f"[ERROR] File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
    elif args.html:
        html = args.html
    else:
        print("[INFO] Running in demo mode. Use --file or --html for your content.\n")
        html = """
        <h1>SyntaxCraft Production SEO Automation Tools</h1>
        <h2>Core Architecture &amp; Modular Scripts</h2>
        <h3>Intent-Weighted Title Generator</h3>
        <h3>Schema.org Rich Snippet Builder</h3>
        <h2>Webmaster Verification Utilities</h2>
        <h3>Robots.txt &amp; Sitemap Validators</h3>
        """

    headings = extract_headings(html)
    report = audit_headings(headings)

    if args.toc and headings:
        report["table_of_contents"] = generate_toc(headings)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"[OK] Report saved to {args.output}")
    else:
        print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
