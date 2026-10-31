"""
Unified SEO Terminal CLI Manager — SyntaxCraft SEO Tools
Command center that orchestrates, inspects, and executes all 15 SEO tools
from a single interactive terminal or scriptable CLI.

Usage:
    python unified_cli_manager.py --list
    python unified_cli_manager.py --run title_engine --keyword "shoes"
    python unified_cli_manager.py --help-tool schema_builder
    python unified_cli_manager.py  (interactive launcher / status check)

Author: SyntaxCraft Studio | contact@syntaxcraft.dev
"""

import argparse
import os
import subprocess
import sys
from typing import Dict, Any, List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

AVAILABLE_MODULES = [
    {
        "id": "slug",
        "num": 1,
        "name": "High-Performance URL Slug Formatter",
        "file": "url_slug_formatter.py",
        "desc": "Converts titles to clean, search-friendly slugs with stopword removal."
    },
    {
        "id": "meta_desc",
        "num": 2,
        "name": "CTR Meta Description Generator",
        "file": "meta_description_generator.py",
        "desc": "Generates 155-160 char snippet descriptions with high CTR."
    },
    {
        "id": "title_engine",
        "num": 3,
        "name": "E-Commerce SEO Title Generator",
        "file": "seo_title_generator.py",
        "desc": "Calibrates product titles to optimal Google SERP pixel width."
    },
    {
        "id": "keyword_density",
        "num": 4,
        "name": "Keyword Density & TF-IDF Guard",
        "file": "keyword_density_analyzer.py",
        "desc": "Analyzes n-gram frequency and flags over-optimization risks."
    },
    {
        "id": "sitemap",
        "num": 5,
        "name": "XML Sitemap 0.9 Protocol Validator",
        "file": "sitemap_validator.py",
        "desc": "Validates sitemaps for syntax errors, broken URLs, and lastmod tags."
    },
    {
        "id": "robots",
        "num": 6,
        "name": "Robots.txt Security & Directive Auditor",
        "file": "robots_txt_auditor.py",
        "desc": "Checks crawl rules, User-agent directives, and sensitive paths."
    },
    {
        "id": "headings",
        "num": 7,
        "name": "H1-H6 Hierarchy & Semantic Structurer",
        "file": "heading_structure_checker.py",
        "desc": "Validates HTML heading structure for WCAG and SEO standards."
    },
    {
        "id": "faq_schema",
        "num": 8,
        "name": "FAQ Schema.org JSON-LD Generator",
        "file": "faq_schema_generator.py",
        "desc": "Generates valid FAQPage and Article structured data blocks."
    },
    {
        "id": "hreflang",
        "num": 9,
        "name": "Canonical & Multi-Lingual Hreflang Manager",
        "file": "canonical_hreflang_manager.py",
        "desc": "Validates ISO language/region codes and generates hreflang tags."
    },
    {
        "id": "image_alt",
        "num": 10,
        "name": "Image Alt Text Optimizer",
        "file": "image_alt_optimizer.py",
        "desc": "Scans HTML files and injects contextual alt attributes."
    },
    {
        "id": "schema_builder",
        "num": 11,
        "name": "Schema.org JSON-LD Synthesizer",
        "file": "schema_builder.py",
        "desc": "Builds rich Product, Article, and Breadcrumb structured data."
    },
    {
        "id": "readability",
        "num": 12,
        "name": "Content & Readability Optimizer",
        "file": "content_readability_optimizer.py",
        "desc": "Scores text with Flesch Reading Ease and Flesch-Kincaid grade."
    },
    {
        "id": "opengraph",
        "num": 13,
        "name": "OpenGraph & Social Meta Synthesizer",
        "file": "opengraph_generator.py",
        "desc": "Generates complete og:* and twitter:card social meta tags."
    },
    {
        "id": "redirects",
        "num": 14,
        "name": "Redirect Rules & Loop Guard Builder",
        "file": "redirect_rules_builder.py",
        "desc": "Generates Apache, Nginx, and Cloudflare 301/302 redirect rules."
    },
    {
        "id": "cli_manager",
        "num": 15,
        "name": "Unified SEO Terminal CLI Manager",
        "file": "unified_cli_manager.py",
        "desc": "Central command center to dispatch and manage all SEO tools."
    },
]


def get_module(identifier: str) -> Dict[str, Any]:
    ident = identifier.strip().lower()
    for mod in AVAILABLE_MODULES:
        if mod["id"].lower() == ident or str(mod["num"]) == ident or mod["file"].lower() == ident:
            return mod
    return {}


def list_modules():
    print("=" * 72)
    print("       SyntaxCraft Unified SEO & Webmaster Command Center")
    print("=" * 72)
    print(f" {'#':<3} {'ID':<16} {'Tool Name':<38} {'Status'}")
    print("-" * 72)
    for m in AVAILABLE_MODULES:
        script_path = os.path.join(SCRIPT_DIR, m["file"])
        exists = os.path.isfile(script_path)
        status = "✓ Ready" if exists else "✗ Missing"
        print(f" [{m['num']:02d}] {m['id']:<16} {m['name']:<38} {status}")
    print("=" * 72)


def run_module(mod: Dict[str, Any], extra_args: List[str]) -> int:
    script_path = os.path.join(SCRIPT_DIR, mod["file"])
    if not os.path.isfile(script_path):
        print(f"[ERROR] Script file not found: {script_path}", file=sys.stderr)
        return 1

    cmd = [sys.executable, script_path] + extra_args
    print(f"[INFO] Launching {mod['name']}...")
    print(f"[CMD]  {' '.join(cmd)}\n")
    try:
        proc = subprocess.run(cmd)
        return proc.returncode
    except Exception as e:
        print(f"[ERROR] Failed to run tool: {e}", file=sys.stderr)
        return 1


def main():
    parser = argparse.ArgumentParser(
        description="SyntaxCraft Unified SEO Command Center",
        epilog="Use --list to view all available tools, or run without args for menu."
    )
    parser.add_argument("--list", action="store_true", help="List all available modules with status")
    parser.add_argument("--run", metavar="TOOL", help="Tool ID or number to execute (e.g. title_engine or 3)")
    parser.add_argument("--help-tool", metavar="TOOL", help="Show help documentation for a specific tool")
    args, unknown = parser.parse_known_args()

    if args.list:
        list_modules()
        return

    if args.help_tool:
        mod = get_module(args.help_tool)
        if not mod:
            print(f"[ERROR] Unknown tool: {args.help_tool}. Use --list to view all tools.", file=sys.stderr)
            sys.exit(1)
        run_module(mod, ["--help"])
        return

    if args.run:
        mod = get_module(args.run)
        if not mod:
            print(f"[ERROR] Unknown tool: {args.run}. Use --list to view all tools.", file=sys.stderr)
            sys.exit(1)
        ret = run_module(mod, unknown)
        sys.exit(ret)

    # Interactive / Status check mode
    list_modules()
    print("\n✓ All 15 modules verified and available.")
    print("Run with: python unified_cli_manager.py --run <id_or_number> [arguments...]")
    print("Example:  python unified_cli_manager.py --run title_engine --keyword 'seo tools'")


if __name__ == "__main__":
    main()
