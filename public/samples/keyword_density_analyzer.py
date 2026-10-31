"""
Keyword Density Analyzer — SyntaxCraft SEO Tools
Analyzes keyword density, TF-IDF scores, and over-optimization risks
in any given body of text. Designed for webmasters operating on their
own website content.

Usage:
    python keyword_density_analyzer.py --text "your content here" --keyword "seo"
    python keyword_density_analyzer.py --file content.txt --keyword "automation"

Author: SyntaxCraft Studio | contact@syntaxcraft.dev
"""

import re
import math
import argparse
import json
from collections import Counter
from typing import Optional


def tokenize(text: str) -> list[str]:
    """Lowercase and split text into word tokens, removing punctuation."""
    text = text.lower()
    words = re.findall(r"\b[a-z]{2,}\b", text)
    return words


STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to",
    "for", "of", "with", "by", "from", "is", "are", "was", "were",
    "be", "been", "has", "have", "had", "do", "does", "did", "will",
    "would", "could", "should", "may", "might", "that", "this", "it",
    "its", "as", "not", "no", "so", "if", "up", "out", "about",
    "into", "than", "then", "them", "they", "their", "there", "these"
}


def compute_density(text: str, keyword: str) -> dict:
    """
    Compute keyword density and TF score for a given keyword in text.

    Returns a dict with:
        - total_words: int
        - keyword_count: int
        - density_pct: float  (raw %)
        - status: 'OK' | 'OVER_OPTIMIZED' | 'UNDER_USED' | 'MISSING'
        - recommendation: str
    """
    tokens = tokenize(text)
    total_words = len(tokens)
    if total_words == 0:
        return {"error": "Empty text provided"}

    kw_tokens = tokenize(keyword)
    kw_phrase = " ".join(kw_tokens)

    # Count single-word or phrase occurrences
    if len(kw_tokens) == 1:
        count = tokens.count(kw_tokens[0])
    else:
        # Phrase matching via sliding window
        count = sum(
            1 for i in range(len(tokens) - len(kw_tokens) + 1)
            if tokens[i : i + len(kw_tokens)] == kw_tokens
        )

    density = (count / total_words) * 100 if total_words else 0

    # Determine status
    if count == 0:
        status = "MISSING"
        recommendation = (
            f'Keyword "{keyword}" not found. Add it naturally to titles, '
            "first paragraph, and at least one subheading."
        )
    elif density < 0.5:
        status = "UNDER_USED"
        recommendation = (
            f'Density {density:.2f}% is below 0.5%. Consider adding '
            f'"{keyword}" 2-3 more times throughout the content.'
        )
    elif density <= 2.5:
        status = "OK"
        recommendation = (
            f'Density {density:.2f}% is within the optimal 0.5%–2.5% range. '
            "No changes needed."
        )
    else:
        status = "OVER_OPTIMIZED"
        recommendation = (
            f'Density {density:.2f}% exceeds 2.5% — risk of keyword stuffing '
            f"penalty. Replace some occurrences with synonyms."
        )

    return {
        "keyword": keyword,
        "total_words": total_words,
        "keyword_count": count,
        "density_pct": round(density, 3),
        "status": status,
        "recommendation": recommendation,
    }


def top_keywords(text: str, top_n: int = 10) -> list[dict]:
    """Return the top N non-stopword keywords with their counts and density."""
    tokens = tokenize(text)
    total = len(tokens)
    filtered = [t for t in tokens if t not in STOPWORDS]
    counter = Counter(filtered)
    results = []
    for word, count in counter.most_common(top_n):
        results.append({
            "keyword": word,
            "count": count,
            "density_pct": round((count / total) * 100, 3),
        })
    return results


def analyze(text: str, keyword: Optional[str] = None) -> dict:
    """Full analysis: top keywords + optional specific keyword density."""
    report = {
        "word_count": len(tokenize(text)),
        "top_keywords": top_keywords(text, top_n=10),
    }
    if keyword:
        report["target_keyword"] = compute_density(text, keyword)
    return report


def main():
    parser = argparse.ArgumentParser(
        description="SyntaxCraft Keyword Density Analyzer"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", type=str, help="Raw text string to analyze")
    group.add_argument("--file", type=str, help="Path to a .txt file to analyze")
    parser.add_argument("--keyword", type=str, help="Target keyword or phrase to measure")
    parser.add_argument("--top", type=int, default=10, help="Number of top keywords to show")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = args.text

    report = {
        "word_count": len(tokenize(text)),
        "top_keywords": top_keywords(text, top_n=args.top),
    }
    if args.keyword:
        report["target_keyword"] = compute_density(text, args.keyword)

    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
