"""
FAQ & Article Schema Engine — SyntaxCraft SEO Tools
Synthesizes Google Rich Result compliant FAQPage and Article
JSON-LD structured data blocks.

Usage:
    python faq_schema_generator.py --question "What is X?" --answer "X is..." \\
        --question "How does Y work?" --answer "Y works by..."
    python faq_schema_generator.py --file faq.csv
    python faq_schema_generator.py --file faq.csv --article-title "My Guide" --article-url "https://example.com/guide"
    python faq_schema_generator.py  (demo mode)

CSV format: columns question,answer  (header row required)
Google FAQ answer limit: 200 words per answer.

Author: SyntaxCraft Studio | contact@syntaxcraft.dev
"""

import json
import argparse
import csv
import sys
from typing import Optional

# Google FAQ Rich Result limit: 200 words per answer
GOOGLE_FAQ_MAX_WORDS = 200


def validate_answer_length(answer: str) -> Optional[str]:
    """Return a warning string if answer exceeds Google's word limit."""
    word_count = len(answer.strip().split())
    if word_count > GOOGLE_FAQ_MAX_WORDS:
        return (
            f"Answer exceeds Google FAQ limit ({word_count}/{GOOGLE_FAQ_MAX_WORDS} words): "
            f'"{answer[:60]}..."'
        )
    return None


def build_faq_schema(qa_pairs: list) -> dict:
    """Build a FAQPage JSON-LD schema from a list of question/answer pairs."""
    entities = []
    for qa in qa_pairs:
        entities.append({
            "@type": "Question",
            "name": qa["question"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": qa["answer"]
            }
        })
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities
    }
    return schema


def build_article_schema(title: str, url: str, qa_pairs: list) -> dict:
    """Build an Article JSON-LD schema optionally combined with FAQ data."""
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "url": url,
        "author": {
            "@type": "Organization",
            "name": "SyntaxCraft Studio",
            "url": "https://syntaxcraft.dev"
        },
        "mainEntity": {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": qa["question"],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": qa["answer"]
                    }
                }
                for qa in qa_pairs
            ]
        }
    }


def main():
    parser = argparse.ArgumentParser(
        description="SyntaxCraft FAQ Schema.org JSON-LD Generator",
        epilog="Run with no arguments for a built-in demo."
    )
    parser.add_argument(
        "--question", action="append", dest="questions", metavar="QUESTION",
        help="FAQ question (repeatable; must pair with --answer)"
    )
    parser.add_argument(
        "--answer", action="append", dest="answers", metavar="ANSWER",
        help="FAQ answer (repeatable; must pair with --question)"
    )
    parser.add_argument(
        "--file", help="CSV file with columns: question,answer"
    )
    parser.add_argument(
        "--article-title", dest="article_title",
        help="Generate Article schema wrapping the FAQ (requires --article-url)"
    )
    parser.add_argument(
        "--article-url", dest="article_url",
        help="Canonical URL for the Article schema"
    )
    args = parser.parse_args()

    qa_pairs = []
    warnings = []

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8", errors="replace") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    q = row.get("question", "").strip()
                    a = row.get("answer", "").strip()
                    if q and a:
                        qa_pairs.append({"question": q, "answer": a})
        except FileNotFoundError:
            print(f"[ERROR] File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
    elif args.questions and args.answers:
        if len(args.questions) != len(args.answers):
            print("[ERROR] Number of --question and --answer flags must match.", file=sys.stderr)
            sys.exit(1)
        for q, a in zip(args.questions, args.answers):
            qa_pairs.append({"question": q.strip(), "answer": a.strip()})
    else:
        # Demo mode
        print("[INFO] Running in demo mode. Use --question/--answer or --file for your data.\n")
        qa_pairs = [
            {
                "question": "What is included with each SEO utility license?",
                "answer": "Each license includes complete commented Python source code, documentation, test suites, and perpetual commercial rights."
            },
            {
                "question": "Are these SEO scripts search-engine compliant?",
                "answer": "Yes, all tools strictly adhere to Google Search Essentials and Schema.org standards without scraping or harvesting private data."
            }
        ]

    # Validate answer lengths
    for qa in qa_pairs:
        warn = validate_answer_length(qa["answer"])
        if warn:
            warnings.append(warn)
            print(f"[WARN] {warn}", file=sys.stderr)

    if not qa_pairs:
        print("[ERROR] No valid question/answer pairs found.", file=sys.stderr)
        sys.exit(1)

    # Choose schema type
    if args.article_title and args.article_url:
        schema = build_article_schema(args.article_title, args.article_url, qa_pairs)
    else:
        schema = build_faq_schema(qa_pairs)

    output = {
        "schema": schema,
        "qa_count": len(qa_pairs),
        "warnings": warnings,
        "json_ld_script": f'<script type="application/ld+json">\n{json.dumps(schema, indent=2, ensure_ascii=False)}\n</script>'
    }

    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
