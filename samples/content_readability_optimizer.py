"""
Paragraph Structure & Content Readability Optimizer — SyntaxCraft SEO Tools
Part of SyntaxCraft SEO & Webmaster Automation Utilities.
Computes Flesch-Kincaid readability, Gunning Fog Index, and optimizes paragraph distribution.

Usage:
    python content_readability_optimizer.py --text "Your content here..."
    python content_readability_optimizer.py --file article.txt
    python content_readability_optimizer.py --file article.txt --output report.json
    python content_readability_optimizer.py  (demo mode)

Author: SyntaxCraft Studio | contact@syntaxcraft.dev
"""

import re
import argparse
import json
import sys
from typing import Dict, Any, List

# Lookup table for common irregular English words (syllable overrides)
SYLLABLE_OVERRIDES = {
    "the": 1, "a": 1, "an": 1, "are": 1, "were": 1, "was": 1,
    "is": 1, "be": 1, "been": 1, "being": 2, "have": 2, "has": 1,
    "had": 1, "do": 1, "does": 1, "did": 1, "will": 1, "would": 1,
    "could": 1, "should": 1, "can": 1, "may": 1, "might": 1,
    "shall": 1, "must": 1, "ought": 1, "and": 1, "or": 1, "but": 1,
    "for": 1, "nor": 1, "so": 1, "yet": 1, "with": 1, "at": 1,
    "by": 1, "from": 1, "into": 2, "through": 1, "during": 2,
    "each": 1, "every": 3, "people": 2, "asked": 1, "used": 1,
    "based": 1, "named": 1, "called": 1, "places": 2, "business": 3,
    "important": 3, "different": 3, "company": 3, "because": 2,
    "between": 2, "example": 3, "however": 3, "interest": 3,
    "likely": 2, "major": 2, "minutes": 2, "money": 2, "nothing": 2,
    "number": 2, "often": 2, "personal": 3, "process": 2, "public": 2,
    "real": 1, "service": 2, "simple": 2, "single": 2, "special": 2,
    "taken": 2, "together": 3, "those": 1, "these": 1, "while": 1,
    "whole": 1, "whose": 1, "always": 2, "around": 2,
}


def count_syllables(word: str) -> int:
    """Count syllables using lookup table for common words, then regex fallback."""
    word_lower = word.lower().strip(".,!?;:\"'()-")
    if word_lower in SYLLABLE_OVERRIDES:
        return SYLLABLE_OVERRIDES[word_lower]
    if len(word_lower) <= 2:
        return 1
    # Strip silent 'e' at end, certain suffixes
    w = re.sub(r"(?:[^laeiouy]|ed|es|e)$", "", word_lower)
    w = re.sub(r"^y", "", w)
    syllables = len(re.findall(r"[aeiouy]{1,2}", w))
    return max(1, syllables)


def count_complex_words(words: List[str]) -> int:
    """Count words with 3 or more syllables (used in Gunning Fog index)."""
    return sum(1 for w in words if count_syllables(w) >= 3)


def audit_readability(text: str) -> Dict[str, Any]:
    """
    Compute Flesch Reading Ease, Flesch-Kincaid Grade Level, and Gunning Fog Index.
    """
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    words = [w.strip() for w in re.split(r"\s+", re.sub(r"[^\w\s]", "", text)) if w.strip()]

    total_sentences = max(1, len(sentences))
    total_words = max(1, len(words))
    total_syllables = sum(count_syllables(w) for w in words)
    complex_word_count = count_complex_words(words)

    # Standard Flesch Reading Ease Formula
    flesch = 206.835 - (1.015 * (total_words / total_sentences)) - (84.6 * (total_syllables / total_words))
    flesch = max(0.0, min(100.0, round(flesch, 1)))

    # Flesch-Kincaid Grade Level
    grade_level = (0.39 * (total_words / total_sentences)) + (11.8 * (total_syllables / total_words)) - 15.59
    grade_level = max(1.0, round(grade_level, 1))

    # Gunning Fog Index
    fog_index = 0.4 * ((total_words / total_sentences) + 100 * (complex_word_count / total_words))
    fog_index = round(fog_index, 1)

    # Human-readable interpretation
    if flesch >= 70:
        readability_label = "Easy (suitable for broad audiences)"
    elif flesch >= 50:
        readability_label = "Standard (suitable for most adults)"
    elif flesch >= 30:
        readability_label = "Difficult (college level)"
    else:
        readability_label = "Very Difficult (specialist/academic)"

    return {
        "flesch_reading_ease": flesch,
        "flesch_kincaid_grade": grade_level,
        "gunning_fog_index": fog_index,
        "readability_label": readability_label,
        "total_words": total_words,
        "total_sentences": total_sentences,
        "total_syllables": total_syllables,
        "complex_word_count": complex_word_count,
        "avg_sentence_length": round(total_words / total_sentences, 1),
        "avg_syllables_per_word": round(total_syllables / total_words, 2),
        "is_optimal": flesch >= 60.0,
        "recommendation": (
            "Good readability for online content." if flesch >= 60
            else "Consider shorter sentences and simpler vocabulary to improve readability."
        )
    }


def format_paragraphs(text: str, target_words_per_para: int = 45) -> List[str]:
    """
    Splits long monolithic text walls into readable, high-retention paragraphs.
    """
    sentences = [s.strip() + "." for s in re.split(r"[.!?]+", text) if s.strip()]
    paragraphs = []
    current_para = []
    current_words = 0

    for sentence in sentences:
        words_in_s = len(sentence.split())
        current_para.append(sentence)
        current_words += words_in_s

        if current_words >= target_words_per_para:
            paragraphs.append(" ".join(current_para))
            current_para = []
            current_words = 0

    if current_para:
        paragraphs.append(" ".join(current_para))

    return paragraphs


def main():
    parser = argparse.ArgumentParser(
        description="SyntaxCraft Content Readability Optimizer",
        epilog="Run with no arguments for a built-in demo."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--text", help="Raw text string to analyze")
    group.add_argument("--file", help="Path to a .txt file to analyze")
    parser.add_argument("--output", help="Save readability report to this JSON file")
    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            print(f"[ERROR] File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
    elif args.text:
        text = args.text
    else:
        print("[INFO] Running in demo mode. Use --text or --file for your content.\n")
        text = (
            "Modern digital business operations depend on concise communication and fast indexing. "
            "When visitors arrive on a product page they scan headings and bullet points rather than "
            "reading continuous walls of text. Clean paragraph structure and search intent optimization "
            "guarantee better engagement metrics and higher search rankings across competitive niches."
        )

    stats = audit_readability(text)
    paragraphs = format_paragraphs(text, target_words_per_para=45)
    report = {
        "readability": stats,
        "paragraph_count": len(paragraphs),
        "reformatted_paragraphs": paragraphs,
    }

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"[OK] Report saved to {args.output}")
    else:
        print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
