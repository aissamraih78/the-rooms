"""
Robots.txt Auditor — SyntaxCraft SEO Tools
Parses, validates, and audits robots.txt directives for crawl budget
optimization and security on your own website.

Usage:
    python robots_txt_auditor.py --file robots.txt
    python robots_txt_auditor.py --url https://yourdomain.com/robots.txt
    python robots_txt_auditor.py --file robots.txt --output report.json
    python robots_txt_auditor.py  (demo mode)

Author: SyntaxCraft Studio | contact@syntaxcraft.dev
"""

import argparse
import json
import re
import sys
from urllib import request as urllib_request
from typing import Optional


KNOWN_BOTS = {
    "Googlebot", "Googlebot-Image", "Googlebot-Video", "Googlebot-News",
    "Bingbot", "Slurp", "DuckDuckBot", "Baiduspider", "YandexBot",
    "facebot", "facebookexternalhit", "Twitterbot", "LinkedInBot",
    "AhrefsBot", "SemrushBot", "MJ12bot", "DotBot",
}

SUSPICIOUS_BOTS = {
    "AhrefsBot", "SemrushBot", "MJ12bot", "DotBot", "BLEXBot",
    "MegaIndex", "AspiegelBot", "PetalBot"
}


def fetch_robots(url: str) -> str:
    """Fetch robots.txt from your domain URL."""
    if not url.endswith("/robots.txt"):
        url = url.rstrip("/") + "/robots.txt"
    with urllib_request.urlopen(url, timeout=15) as resp:
        return resp.read().decode("utf-8", errors="replace")


def load_robots(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def parse_robots(content: str) -> list:
    """
    Parse robots.txt into a list of agent blocks.
    Each block: {"agent": str, "rules": [{"directive": str, "value": str}]}
    """
    blocks = []
    current_agents = []
    current_rules = []

    for raw_line in content.splitlines():
        line = raw_line.strip()
        # Strip inline comments
        if "#" in line:
            line = line[: line.index("#")].strip()
        if not line:
            if current_agents and current_rules:
                for agent in current_agents:
                    blocks.append({"agent": agent, "rules": list(current_rules)})
                current_agents = []
                current_rules = []
            continue

        if ":" in line:
            directive, _, value = line.partition(":")
            directive = directive.strip()
            value = value.strip()
            d_lower = directive.lower()
            if d_lower == "user-agent":
                if current_rules:
                    for agent in current_agents:
                        blocks.append({"agent": agent, "rules": list(current_rules)})
                    current_agents = []
                    current_rules = []
                current_agents.append(value)
            elif d_lower in ("allow", "disallow", "crawl-delay", "sitemap", "host"):
                current_rules.append({"directive": directive, "value": value})
            else:
                current_rules.append({"directive": directive, "value": value, "unknown": True})

    # Final block
    if current_agents and current_rules:
        for agent in current_agents:
            blocks.append({"agent": agent, "rules": list(current_rules)})

    return blocks


def audit(content: str) -> dict:
    """
    Full robots.txt audit returning:
    - parsed blocks
    - errors / warnings
    - coverage score
    - recommendations
    """
    errors = []
    warnings = []
    recommendations = []
    blocks = parse_robots(content)

    # Check for wildcard agent
    all_agents = [b["agent"] for b in blocks]
    has_wildcard = "*" in all_agents

    if not has_wildcard:
        errors.append(
            "Missing 'User-agent: *' block. All robots.txt files should have a "
            "wildcard block as fallback for unspecified crawlers."
        )

    # Check for Sitemap declaration
    all_rules = [r for b in blocks for r in b["rules"]]
    sitemap_entries = [r["value"] for r in all_rules if r["directive"].lower() == "sitemap"]
    if not sitemap_entries:
        warnings.append(
            "No Sitemap: declaration found. Add 'Sitemap: https://yourdomain.com/sitemap.xml' "
            "to help crawlers discover your content."
        )
        recommendations.append("Add: Sitemap: https://yourdomain.com/sitemap.xml")
    else:
        for s in sitemap_entries:
            if not s.startswith("https://"):
                warnings.append(f"Sitemap URL uses HTTP instead of HTTPS: {s}")

    # Check for crawl-delay on Googlebot (Google ignores it, but flag it)
    for block in blocks:
        if block["agent"].lower() in ("googlebot", "*"):
            for rule in block["rules"]:
                if rule["directive"].lower() == "crawl-delay":
                    warnings.append(
                        f"'Crawl-delay' directive on User-agent: {block['agent']} — "
                        "Googlebot ignores Crawl-delay. Use Google Search Console crawl rate settings instead."
                    )

    # Check for suspicious bots being explicitly allowed
    for block in blocks:
        if block["agent"] in SUSPICIOUS_BOTS:
            for rule in block["rules"]:
                if rule["directive"].lower() == "allow" and rule["value"] == "/":
                    warnings.append(
                        f"Bot '{block['agent']}' is explicitly allowed to crawl everything. "
                        "Consider restricting aggressive SEO scrapers."
                    )

    # Detect overly broad disallows
    for block in blocks:
        if block["agent"] == "*":
            for rule in block["rules"]:
                if rule["directive"].lower() == "disallow" and rule["value"] == "/":
                    errors.append(
                        "CRITICAL: 'Disallow: /' under User-agent: * blocks ALL crawlers from your entire site! "
                        "This will de-index your website from all search engines."
                    )

    # Unknown directives
    for block in blocks:
        for rule in block["rules"]:
            if rule.get("unknown"):
                warnings.append(f"Unknown directive '{rule['directive']}' — not part of Robots Exclusion Protocol.")

    # Compute a simple coverage score
    score = 100
    score -= len(errors) * 25
    score -= len(warnings) * 5
    score = max(0, min(100, score))

    return {
        "blocks_found": len(blocks),
        "agents_covered": list(set(all_agents)),
        "sitemap_declarations": sitemap_entries,
        "errors": errors,
        "warnings": warnings,
        "recommendations": recommendations,
        "coverage_score": score,
        "status": "HEALTHY" if score >= 80 else "NEEDS REVIEW" if score >= 50 else "CRITICAL ISSUES",
        "parsed_blocks": blocks,
    }


def main():
    parser = argparse.ArgumentParser(
        description="SyntaxCraft Robots.txt Auditor",
        epilog="Run with no arguments for a built-in demo."
    )
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--file", help="Path to local robots.txt")
    group.add_argument("--url", help="Your domain URL to fetch robots.txt from")
    parser.add_argument("--output", help="Save audit report to this JSON file")
    args = parser.parse_args()

    if args.file:
        try:
            content = load_robots(args.file)
        except FileNotFoundError:
            print(f"[ERROR] File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
    elif args.url:
        print(f"Fetching robots.txt from: {args.url}")
        content = fetch_robots(args.url)
    else:
        print("[INFO] Running in demo mode. Use --file or --url for your robots.txt.\n")
        content = """User-agent: *
Disallow: /admin/
Disallow: /private/
Allow: /

Sitemap: https://syntaxcraft.dev/sitemap.xml
"""

    report = audit(content)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"[OK] Report saved to {args.output}")
    else:
        print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
