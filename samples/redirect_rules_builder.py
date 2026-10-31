"""
301/302 Redirect Rules & Loop Guard Builder — SyntaxCraft SEO Tools
Converts lists of legacy URLs into optimized redirect rules
for Nginx, Apache (.htaccess), and Cloudflare _redirects.
Includes automatic redirect loop and duplicate source detection.

Usage:
    python redirect_rules_builder.py --old "/products/old-bag" --new "/shop/leather-bag" --server nginx
    python redirect_rules_builder.py --file mappings.csv --server cloudflare
    python redirect_rules_builder.py --file mappings.csv --output redirects.conf
    python redirect_rules_builder.py  (built-in demo)

CSV format: columns 'from' and 'to' (or 'source' and 'destination', or 'old' and 'new').
Optional third column: 'status' (301 or 302).

Author: SyntaxCraft Studio | contact@syntaxcraft.dev
"""

import argparse
import csv
import json
import os
import sys
from typing import List, Tuple, Dict, Any, Optional


def generate_nginx_rule(old_path: str, new_path: str, status_code: int = 301) -> str:
    flag = "permanent" if status_code == 301 else "redirect"
    clean_old = old_path.strip().rstrip("/")
    return f"rewrite ^{clean_old}/?$ {new_path.strip()} {flag};"


def generate_apache_rule(old_path: str, new_path: str, status_code: int = 301) -> str:
    flag = f"R={status_code},L"
    clean_old = old_path.strip().lstrip("/")
    return f"RewriteRule ^{clean_old}$ {new_path.strip()} [{flag}]"


def generate_cloudflare_rule(old_path: str, new_path: str, status_code: int = 301) -> str:
    return f"{old_path.strip()} {new_path.strip()} {status_code}"


def detect_loops_and_duplicates(mappings: List[Tuple[str, str, int]]) -> Tuple[List[str], List[str]]:
    warnings = []
    errors = []
    sources = set()
    forward_map = {}

    for src, dst, _ in mappings:
        src_clean = src.strip().lower().rstrip("/")
        dst_clean = dst.strip().lower().rstrip("/")

        if src_clean == dst_clean:
            errors.append(f"Self-redirect loop: '{src}' redirects to itself.")

        if src_clean in sources:
            warnings.append(f"Duplicate source detected: '{src}' appears multiple times.")
        sources.add(src_clean)

        if dst_clean in forward_map:
            errors.append(
                f"Multi-hop or Circular redirect detected: '{forward_map[dst_clean]}' -> '{dst}' -> '{src}'."
            )
        forward_map[src_clean] = dst_clean

    return errors, warnings


def build_redirects(
    mappings: List[Tuple[str, str, int]],
    server: str = "nginx"
) -> Dict[str, Any]:
    errors, warnings = detect_loops_and_duplicates(mappings)
    rules = []

    for src, dst, code in mappings:
        if server == "nginx":
            rules.append(generate_nginx_rule(src, dst, code))
        elif server == "apache":
            rules.append(generate_apache_rule(src, dst, code))
        elif server == "cloudflare":
            rules.append(generate_cloudflare_rule(src, dst, code))

    header = ""
    if server == "apache":
        header = "# Apache .htaccess 301/302 Redirect Rules\nRewriteEngine On\nRewriteBase /\n\n"
    elif server == "nginx":
        header = "# Nginx Server Block 301/302 Redirect Rules\n"
    elif server == "cloudflare":
        header = "# Cloudflare Pages / Static _redirects format\n"

    output_content = header + "\n".join(rules)

    return {
        "server_type": server,
        "rules_count": len(rules),
        "errors": errors,
        "warnings": warnings,
        "valid": len(errors) == 0,
        "generated_config": output_content
    }


def parse_csv_mappings(file_path: str, default_status: int = 301) -> List[Tuple[str, str, int]]:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Mapping file not found: {file_path}")

    mappings = []
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        reader = csv.reader(f)
        header = [h.strip().lower() for h in next(reader, [])]

        src_idx, dst_idx, status_idx = -1, -1, -1
        for i, col in enumerate(header):
            if col in ("from", "old", "source", "old_url", "source_url"):
                src_idx = i
            elif col in ("to", "new", "destination", "new_url", "target_url"):
                dst_idx = i
            elif col in ("status", "status_code", "code"):
                status_idx = i

        if src_idx == -1 or dst_idx == -1:
            # Fallback to col 0 and 1
            src_idx = 0
            dst_idx = 1
            if len(header) > 2:
                status_idx = 2

        for row in reader:
            if len(row) <= max(src_idx, dst_idx):
                continue
            src = row[src_idx].strip()
            dst = row[dst_idx].strip()
            if not src or not dst:
                continue
            code = default_status
            if status_idx != -1 and len(row) > status_idx and row[status_idx].strip().isdigit():
                code = int(row[status_idx].strip())
            mappings.append((src, dst, code))

    return mappings


def main():
    parser = argparse.ArgumentParser(
        description="SyntaxCraft 301/302 Redirect Rules & Loop Guard Builder",
        epilog="Run without arguments for built-in demo."
    )
    parser.add_argument("--old", help="Old URL path e.g. /shop/item-123")
    parser.add_argument("--new", help="New target destination path e.g. /products/vintage-bag")
    parser.add_argument(
        "--server",
        default="nginx",
        choices=["nginx", "apache", "cloudflare"],
        help="Target server configuration format (default: nginx)"
    )
    parser.add_argument("--status", type=int, default=301, choices=[301, 302], help="HTTP status code (default: 301)")
    parser.add_argument("--file", help="Path to CSV file with redirect mappings")
    parser.add_argument("--output", help="Optional output file path to write generated config")
    args = parser.parse_args()

    if args.file:
        try:
            mappings = parse_csv_mappings(args.file, default_status=args.status)
        except Exception as e:
            print(f"[ERROR] Failed to read CSV: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.old and args.new:
        mappings = [(args.old, args.new, args.status)]
    else:
        print("[INFO] Running in demo mode. Use --file or --old/--new for custom redirects.\n")
        mappings = [
            ("/shop/item-1234", "/products/vintage-leather-bag", 301),
            ("/category/old-bags", "/collections/mens-briefcases", 301),
            ("/blog/2023/seo-tips", "/resources/white-hat-seo-guide", 301),
            ("/promo/spring-sale", "/promotions/current", 302),
        ]

    result = build_redirects(mappings, server=args.server)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result["generated_config"])
        print(f"✓ Configuration written to: {args.output}")

    print(json.dumps({
        "server_type": result["server_type"],
        "rules_count": result["rules_count"],
        "valid": result["valid"],
        "errors": result["errors"],
        "warnings": result["warnings"],
        "preview": result["generated_config"].splitlines()[:10]
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
