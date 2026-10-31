"""
Canonical & Multi-Lingual Hreflang Manager — SyntaxCraft SEO Tools
Validates and generates reciprocal hreflang annotations across
multi-regional and multi-language e-commerce websites.

Usage:
    python canonical_hreflang_manager.py --url https://example.com/en/page --lang en
    python canonical_hreflang_manager.py \\
        --url https://example.com/en/page --lang en \\
        --url https://example.com/es/page --lang es --region ES \\
        --url https://example.com/fr/page --lang fr --region FR
    python canonical_hreflang_manager.py --file hreflang.csv
    python canonical_hreflang_manager.py  (demo mode)

CSV format: columns url,lang,region  (header row required; region is optional)

Author: SyntaxCraft Studio | contact@syntaxcraft.dev
"""

import json
import argparse
import csv
import sys
from typing import Optional, List

# ISO 639-1 language codes (common subset)
VALID_LANG_CODES = {
    "af", "sq", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg",
    "ca", "zh", "hr", "cs", "da", "nl", "en", "et", "fi", "fr",
    "gl", "ka", "de", "el", "gu", "he", "hi", "hu", "is", "id",
    "ga", "it", "ja", "kn", "kk", "km", "ko", "lv", "lt", "mk",
    "ms", "ml", "mt", "mr", "ne", "no", "fa", "pl", "pt", "ro",
    "ru", "sr", "sk", "sl", "es", "sw", "sv", "ta", "te", "th",
    "tr", "uk", "ur", "vi", "cy", "xh", "zu",
}

# ISO 3166-1 alpha-2 country codes (common subset)
VALID_REGION_CODES = {
    "AF", "AL", "DZ", "AR", "AU", "AT", "AZ", "BE", "BD", "BG",
    "BR", "CA", "CL", "CN", "CO", "HR", "CZ", "DK", "EG", "FI",
    "FR", "DE", "GH", "GR", "HK", "HU", "IN", "ID", "IE", "IL",
    "IT", "JP", "KZ", "KE", "KR", "MY", "MX", "MA", "NL", "NZ",
    "NG", "NO", "PK", "PH", "PL", "PT", "RO", "RU", "SA", "RS",
    "SG", "SK", "ZA", "ES", "SE", "CH", "TW", "TH", "TR", "UA",
    "AE", "GB", "US", "UZ", "VN",
}


def validate_lang(lang: str) -> Optional[str]:
    """Return error string if lang code is not valid ISO 639-1."""
    if lang.lower() not in VALID_LANG_CODES:
        return f"Unknown ISO 639-1 language code: '{lang}'. Check https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes"
    return None


def validate_region(region: str) -> Optional[str]:
    """Return error string if region code is not valid ISO 3166-1 alpha-2."""
    if region.upper() not in VALID_REGION_CODES:
        return f"Unknown ISO 3166-1 region code: '{region}'. Check https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2"
    return None


def build_hreflang_value(lang: str, region: Optional[str] = None) -> str:
    """Construct a hreflang attribute value like 'en', 'en-US', etc."""
    lang = lang.lower()
    if region:
        return f"{lang}-{region.upper()}"
    return lang


def generate_hreflang_tags(
    entries: List[dict],
    canonical_url: str,
    add_x_default: bool = True
) -> dict:
    """
    Generate hreflang HTML link tags and canonical tag.

    entries: list of {"url": str, "lang": str, "region": str or None}
    canonical_url: the self-referencing canonical URL
    """
    errors = []
    warnings = []
    tags = []

    # Canonical tag
    tags.append(f'<link rel="canonical" href="{canonical_url}" />')

    # Check self-referencing canonical: canonical should match one of the entries
    entry_urls = [e["url"] for e in entries]
    if canonical_url not in entry_urls:
        warnings.append(
            f"Canonical URL '{canonical_url}' is not present in the hreflang entries. "
            "Best practice: include a self-referencing hreflang entry matching the canonical."
        )

    # Generate hreflang tags
    hreflang_values_seen = set()
    for entry in entries:
        url = entry["url"]
        lang = entry.get("lang", "").strip().lower()
        region = entry.get("region", "").strip().upper() if entry.get("region") else None

        # Validate lang
        lang_err = validate_lang(lang)
        if lang_err:
            errors.append(lang_err)
            continue

        # Validate region (if provided)
        if region:
            region_err = validate_region(region)
            if region_err:
                errors.append(region_err)
                continue

        hreflang_val = build_hreflang_value(lang, region)

        # Duplicate hreflang value detection
        if hreflang_val in hreflang_values_seen:
            warnings.append(f"Duplicate hreflang value '{hreflang_val}' found — each language-region pair must be unique.")
        hreflang_values_seen.add(hreflang_val)

        tags.append(f'<link rel="alternate" hreflang="{hreflang_val}" href="{url}" />')

    # x-default fallback
    if add_x_default:
        tags.append(f'<link rel="alternate" hreflang="x-default" href="{canonical_url}" />')

    languages_covered = list(hreflang_values_seen)

    return {
        "canonical": canonical_url,
        "languages_covered": languages_covered,
        "html_tags": "\n".join(tags),
        "total_tags": len(tags),
        "errors": errors,
        "warnings": warnings,
        "valid": len(errors) == 0,
    }


def main():
    parser = argparse.ArgumentParser(
        description="SyntaxCraft Canonical & Hreflang Manager",
        epilog="Run with no arguments for a built-in demo."
    )
    parser.add_argument(
        "--url", action="append", dest="urls", metavar="URL",
        help="Page URL (repeatable; pairs with --lang and optionally --region)"
    )
    parser.add_argument(
        "--lang", action="append", dest="langs", metavar="LANG",
        help="ISO 639-1 language code e.g. en, fr, de (repeatable)"
    )
    parser.add_argument(
        "--region", action="append", dest="regions", metavar="REGION",
        help="ISO 3166-1 alpha-2 region code e.g. US, GB, DE (repeatable; use '' to skip)"
    )
    parser.add_argument(
        "--canonical", help="Override canonical URL (default: first --url provided)"
    )
    parser.add_argument(
        "--file", help="CSV file with columns: url,lang,region"
    )
    parser.add_argument(
        "--no-x-default", action="store_true",
        help="Omit the x-default hreflang entry"
    )
    args = parser.parse_args()

    entries = []

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8", errors="replace") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    url = row.get("url", "").strip()
                    lang = row.get("lang", "").strip()
                    region = row.get("region", "").strip() or None
                    if url and lang:
                        entries.append({"url": url, "lang": lang, "region": region})
        except FileNotFoundError:
            print(f"[ERROR] File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
    elif args.urls and args.langs:
        if len(args.urls) != len(args.langs):
            print("[ERROR] Number of --url and --lang flags must match.", file=sys.stderr)
            sys.exit(1)
        regions = args.regions or []
        for i, (url, lang) in enumerate(zip(args.urls, args.langs)):
            region = regions[i] if i < len(regions) else None
            entries.append({"url": url, "lang": lang, "region": region or None})
    else:
        # Demo mode
        print("[INFO] Running in demo mode. Use --url/--lang or --file for your data.\n")
        entries = [
            {"url": "https://syntaxcraft.dev/tools/title-optimizer", "lang": "en", "region": None},
            {"url": "https://syntaxcraft.dev/es/tools/title-optimizer", "lang": "es", "region": None},
            {"url": "https://syntaxcraft.dev/fr/tools/title-optimizer", "lang": "fr", "region": None},
            {"url": "https://syntaxcraft.dev/de/tools/title-optimizer", "lang": "de", "region": None},
        ]

    if not entries:
        print("[ERROR] No valid URL/lang entries found.", file=sys.stderr)
        sys.exit(1)

    canonical_url = args.canonical if args.canonical else entries[0]["url"]
    add_x_default = not args.no_x_default

    result = generate_hreflang_tags(entries, canonical_url, add_x_default)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
