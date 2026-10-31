"""
Sitemap Validator — SyntaxCraft SEO Tools
Parses and validates sitemap.xml files against the Sitemaps.org 0.9 protocol.
Detects missing required fields, invalid dates, duplicate URLs, and
malformed XML — all on your own website's sitemap files.

Usage:
    python sitemap_validator.py --file sitemap.xml
    python sitemap_validator.py --url https://yourdomain.com/sitemap.xml

Author: SyntaxCraft Studio | contact@syntaxcraft.dev
"""

import argparse
import json
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Optional
from urllib import request as urllib_request


SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
IMAGE_NS = "http://www.google.com/schemas/sitemap-image/1.1"

VALID_CHANGEFREQS = {
    "always", "hourly", "daily", "weekly", "monthly", "yearly", "never"
}
ISO8601_PATTERN = re.compile(
    r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}(:\d{2})?(\.\d+)?(Z|[+-]\d{2}:\d{2})?)?$"
)


def fetch_sitemap(url: str) -> str:
    """Fetch sitemap XML from a URL."""
    with urllib_request.urlopen(url, timeout=15) as resp:
        return resp.read().decode("utf-8")


def load_sitemap(path: str) -> str:
    """Read sitemap XML from a local file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def validate_url(url: str) -> list[str]:
    """Basic URL format checks."""
    errors = []
    if not url.startswith(("http://", "https://")):
        errors.append(f"Invalid scheme in URL: {url}")
    if len(url) > 2048:
        errors.append(f"URL exceeds 2048 character limit: {url[:80]}...")
    return errors


def validate_lastmod(lastmod: str) -> Optional[str]:
    """Return error string if lastmod is not valid ISO 8601, else None."""
    if not ISO8601_PATTERN.match(lastmod.strip()):
        return f"Invalid lastmod date format: '{lastmod}' (must be ISO 8601, e.g. 2024-01-15)"
    try:
        datetime.fromisoformat(lastmod.strip().replace("Z", "+00:00"))
    except ValueError:
        return f"Unparseable date: '{lastmod}'"
    return None


def parse_and_validate(xml_content: str) -> dict:
    """
    Parse sitemap XML and return a validation report.

    Returns:
        {
            "url_count": int,
            "errors": [...],
            "warnings": [...],
            "duplicates": [...],
            "valid": bool,
            "urls_preview": [first 5 URLs]
        }
    """
    errors = []
    warnings = []
    seen_urls = set()
    duplicates = []
    url_entries = []

    try:
        root = ET.fromstring(xml_content)
    except ET.ParseError as e:
        return {
            "url_count": 0,
            "errors": [f"XML Parse Error: {e}"],
            "warnings": [],
            "duplicates": [],
            "valid": False,
            "urls_preview": [],
        }

    # Detect sitemap index vs urlset
    tag = root.tag.replace(f"{{{SITEMAP_NS}}}", "")
    if tag == "sitemapindex":
        warnings.append("This is a Sitemap Index file, not a URL sitemap. Contains pointers to child sitemaps.")
        for sitemap in root.findall(f"{{{SITEMAP_NS}}}sitemap"):
            loc = sitemap.findtext(f"{{{SITEMAP_NS}}}loc", "").strip()
            if loc:
                url_entries.append(loc)
    elif tag == "urlset":
        for url_elem in root.findall(f"{{{SITEMAP_NS}}}url"):
            loc = url_elem.findtext(f"{{{SITEMAP_NS}}}loc", "").strip()

            # Required: <loc>
            if not loc:
                errors.append("Found <url> element missing required <loc> tag")
                continue

            # Duplicate check
            if loc in seen_urls:
                duplicates.append(loc)
            else:
                seen_urls.add(loc)
                url_entries.append(loc)

            # URL format check
            url_errors = validate_url(loc)
            errors.extend(url_errors)

            # Optional: <lastmod>
            lastmod = url_elem.findtext(f"{{{SITEMAP_NS}}}lastmod", "")
            if lastmod:
                err = validate_lastmod(lastmod)
                if err:
                    errors.append(err)
            else:
                warnings.append(f"No <lastmod> on URL: {loc[:60]}")

            # Optional: <changefreq>
            changefreq = url_elem.findtext(f"{{{SITEMAP_NS}}}changefreq", "")
            if changefreq and changefreq.lower() not in VALID_CHANGEFREQS:
                errors.append(
                    f"Invalid <changefreq> '{changefreq}' on {loc[:60]} — "
                    f"valid values: {', '.join(sorted(VALID_CHANGEFREQS))}"
                )

            # Optional: <priority>
            priority = url_elem.findtext(f"{{{SITEMAP_NS}}}priority", "")
            if priority:
                try:
                    p = float(priority)
                    if not (0.0 <= p <= 1.0):
                        errors.append(f"Priority {p} out of range [0.0–1.0] on {loc[:60]}")
                except ValueError:
                    errors.append(f"Non-numeric <priority> '{priority}' on {loc[:60]}")
    else:
        errors.append(f"Unknown root element <{tag}>. Expected <urlset> or <sitemapindex>.")

    # Protocol limit check
    if len(url_entries) > 50000:
        errors.append(
            f"Sitemap contains {len(url_entries)} URLs — exceeds 50,000 URL limit. "
            "Split into multiple sitemaps using a sitemapindex."
        )

    valid = len(errors) == 0
    return {
        "url_count": len(url_entries),
        "errors": errors,
        "warnings": warnings[:10],  # cap warnings in output
        "duplicates": duplicates,
        "valid": valid,
        "status": "✅ VALID" if valid else "❌ INVALID — fix errors above",
        "urls_preview": url_entries[:5],
    }


def main():
    parser = argparse.ArgumentParser(
        description="SyntaxCraft Sitemap Validator (Sitemaps.org 0.9)"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="Local sitemap.xml path")
    group.add_argument("--url", help="Remote sitemap URL (your own domain)")
    args = parser.parse_args()

    if args.file:
        content = load_sitemap(args.file)
    else:
        print(f"Fetching sitemap from: {args.url}")
        content = fetch_sitemap(args.url)

    report = parse_and_validate(content)
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
