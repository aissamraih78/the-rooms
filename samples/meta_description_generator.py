"""
Meta Description Generator — SyntaxCraft SEO Tools
Generates persuasive, click-optimized meta descriptions calibrated
to the 155-160 character Google SERP pixel limit.

Usage:
    python meta_description_generator.py --title "Best SEO Tools 2025" --keyword "seo tools"
    python meta_description_generator.py --content content.txt --keyword "keyword research"

Author: SyntaxCraft Studio | contact@syntaxcraft.dev
"""

import re
import argparse
import json
from typing import Optional


# CTA phrases that drive click-through rates
CTA_PHRASES = [
    "Learn how to",
    "Discover the",
    "Find out why",
    "Get started with",
    "See how",
    "Explore the best",
]

# Power words for emotional engagement
POWER_WORDS = [
    "proven", "instant", "essential", "ultimate", "complete",
    "powerful", "reliable", "professional", "trusted", "advanced",
]


def count_pixels(text: str, is_title: bool = False) -> int:
    """
    Estimate rendered pixel width using Arial character width averages.
    Google uses ~Arial 14px for descriptions (roughly 5.5px avg per char).
    """
    avg_px = 5.5 if not is_title else 8.5
    return int(len(text) * avg_px)


def truncate_to_serp_limit(text: str, max_chars: int = 158) -> str:
    """Truncate text to max_chars at a word boundary, appending ellipsis if needed."""
    if len(text) <= max_chars:
        return text
    truncated = text[:max_chars].rsplit(" ", 1)[0]
    return truncated.rstrip(".,;:") + "…"


def inject_keyword(template: str, keyword: str) -> str:
    """Ensure keyword appears naturally in the description."""
    if keyword.lower() not in template.lower():
        # Prepend keyword if not already present
        template = f"{keyword.capitalize()}: {template}"
    return template


def generate_meta_description(
    title: str,
    keyword: str,
    content_snippet: Optional[str] = None,
    include_cta: bool = True,
) -> dict:
    """
    Generate 3 candidate meta descriptions for A/B testing.

    Returns:
        {
            "candidates": [
                {"text": str, "char_count": int, "pixel_width": int, "status": str},
                ...
            ],
            "recommended": int  # index of best candidate
        }
    """
    candidates = []

    # Variant 1: CTA-led
    cta = CTA_PHRASES[len(title) % len(CTA_PHRASES)]
    v1 = f"{cta} {keyword} — {title.rstrip('.')}. Get instant access to our complete guide."
    v1 = truncate_to_serp_limit(v1)

    # Variant 2: Keyword-first informational
    v2 = f"{keyword.capitalize()} made simple. {title} — step-by-step tools, code examples, and proven strategies for webmasters."
    v2 = truncate_to_serp_limit(v2)

    # Variant 3: Content-derived (if snippet provided)
    if content_snippet:
        sentences = re.split(r"(?<=[.!?])\s+", content_snippet.strip())
        best_sent = max(sentences, key=lambda s: keyword.lower() in s.lower()) if sentences else ""
        v3 = truncate_to_serp_limit(f"{best_sent} {keyword.capitalize()} tools and utilities by SyntaxCraft.")
    else:
        v3 = f"Professional {keyword} utilities for webmasters. Download, run, and automate — 100% white-hat, source-code included."
        v3 = truncate_to_serp_limit(v3)

    for v in [v1, v2, v3]:
        char_count = len(v)
        px = count_pixels(v)
        if char_count <= 155:
            status = "OK"
        elif char_count <= 162:
            status = "BORDERLINE"
        else:
            status = "TOO_LONG"
        candidates.append({
            "text": v,
            "char_count": char_count,
            "pixel_estimate": px,
            "status": status,
        })

    # Recommend the one closest to 155 chars without going over
    ok_candidates = [(i, c) for i, c in enumerate(candidates) if c["status"] == "OK"]
    if ok_candidates:
        recommended_idx = max(ok_candidates, key=lambda x: x[1]["char_count"])[0]
    else:
        recommended_idx = 0

    return {
        "keyword": keyword,
        "title": title,
        "candidates": candidates,
        "recommended_index": recommended_idx,
        "recommended_text": candidates[recommended_idx]["text"],
    }


def main():
    parser = argparse.ArgumentParser(
        description="SyntaxCraft Meta Description Generator"
    )
    parser.add_argument("--title", required=True, help="Page or product title")
    parser.add_argument("--keyword", required=True, help="Target SEO keyword")
    parser.add_argument("--content", help="Path to .txt file for content-based generation")
    args = parser.parse_args()

    snippet = None
    if args.content:
        with open(args.content, "r", encoding="utf-8") as f:
            snippet = f.read()[:500]  # Use first 500 chars

    result = generate_meta_description(
        title=args.title,
        keyword=args.keyword,
        content_snippet=snippet,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
