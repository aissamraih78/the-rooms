"""
Schema.org JSON-LD Structured Data Builder — SyntaxCraft SEO Tools
Part of SyntaxCraft SEO & Webmaster Automation Utilities.
100% Google Rich Results Compliant.

Usage:
    python schema_builder.py --name "My Product" --description "A great tool" \\
        --sku "PROD-001" --price "9.99" --currency EUR
    python schema_builder.py --type article --name "SEO Guide" --description "Full guide"
    python schema_builder.py --rating 4.7 --review-count 23  (user-supplied ratings only)
    python schema_builder.py  (demo mode — no ratings included)

IMPORTANT: Do NOT supply --rating and --review-count unless you have real, verified reviews.
Fabricating review data violates Google's Rich Results policies.

Author: SyntaxCraft Studio | contact@syntaxcraft.dev
"""

import json
import argparse
import sys
from typing import Optional, List


def build_product_schema(
    name: str,
    description: str,
    sku: str,
    price: str,
    currency: str = "EUR",
    brand: str = "SyntaxCraft",
    in_stock: bool = True,
    images: Optional[List[str]] = None,
    rating: Optional[float] = None,
    review_count: Optional[int] = None,
    price_valid_until: Optional[str] = None,
) -> dict:
    """
    Build a Product JSON-LD schema.

    NOTE: aggregateRating is only included when the caller explicitly provides
    rating AND review_count. Never use hardcoded or fabricated review data —
    doing so violates Google Search Essentials and may result in manual actions.
    """
    images = images or ["https://syntaxcraft.dev/images/product-default.jpg"]

    offer = {
        "@type": "Offer",
        "url": f"https://syntaxcraft.dev/tools/{sku.lower()}",
        "priceCurrency": currency,
        "price": price,
        "availability": "https://schema.org/InStock" if in_stock else "https://schema.org/OutOfStock",
        "itemCondition": "https://schema.org/NewCondition"
    }
    # Only add priceValidUntil when explicitly supplied by the user
    if price_valid_until:
        offer["priceValidUntil"] = price_valid_until

    schema = {
        "@context": "https://schema.org/",
        "@type": "Product",
        "name": name,
        "image": images,
        "description": description,
        "sku": sku,
        "brand": {
            "@type": "Brand",
            "name": brand
        },
        "offers": offer
    }

    # Only include aggregateRating when user provides real data
    if rating is not None and review_count is not None:
        schema["aggregateRating"] = {
            "@type": "AggregateRating",
            "ratingValue": str(round(rating, 1)),
            "reviewCount": str(review_count),
            "bestRating": "5",
            "worstRating": "1"
        }

    return schema


def build_article_schema(name: str, description: str, url: Optional[str] = None) -> dict:
    """Build an Article JSON-LD schema."""
    return {
        "@context": "https://schema.org/",
        "@type": "Article",
        "headline": name,
        "description": description,
        "url": url or "https://syntaxcraft.dev/",
        "author": {
            "@type": "Organization",
            "name": "SyntaxCraft Studio",
            "url": "https://syntaxcraft.dev"
        },
        "publisher": {
            "@type": "Organization",
            "name": "SyntaxCraft Studio",
            "url": "https://syntaxcraft.dev"
        }
    }


def build_breadcrumb_schema(items: List[dict]) -> dict:
    """
    Build a BreadcrumbList JSON-LD schema.
    items: list of {"name": str, "url": str}
    """
    list_items = [
        {
            "@type": "ListItem",
            "position": i + 1,
            "name": item["name"],
            "item": item["url"]
        }
        for i, item in enumerate(items)
    ]
    return {
        "@context": "https://schema.org/",
        "@type": "BreadcrumbList",
        "itemListElement": list_items
    }


def main():
    parser = argparse.ArgumentParser(
        description="SyntaxCraft Schema.org JSON-LD Builder",
        epilog="Run with no arguments for a built-in demo."
    )
    parser.add_argument("--type", choices=["product", "article", "breadcrumb"], default="product",
                        help="Schema type to generate (default: product)")
    parser.add_argument("--name", help="Product name or article headline")
    parser.add_argument("--description", help="Product or article description")
    parser.add_argument("--sku", default="UTIL-001", help="Product SKU")
    parser.add_argument("--price", default="9.99", help="Product price (numeric string)")
    parser.add_argument("--currency", default="EUR", help="ISO 4217 currency code (default: EUR)")
    parser.add_argument("--brand", default="SyntaxCraft", help="Brand name")
    parser.add_argument("--url", help="Canonical URL for article/product page")
    parser.add_argument("--image", action="append", dest="images",
                        help="Product image URL (repeatable)")
    parser.add_argument(
        "--rating", type=float, default=None,
        help="Aggregate rating value (user-supplied real data only; do NOT fabricate)"
    )
    parser.add_argument(
        "--review-count", type=int, default=None, dest="review_count",
        help="Number of real reviews (user-supplied only; do NOT fabricate)"
    )
    parser.add_argument(
        "--price-valid-until", dest="price_valid_until", default=None,
        help="priceValidUntil date in YYYY-MM-DD format (e.g. 2027-12-31)"
    )
    parser.add_argument("--out-of-stock", action="store_true", dest="out_of_stock",
                        help="Mark product as OutOfStock")
    args = parser.parse_args()

    # Validate: both rating and review_count must be provided together
    if (args.rating is None) != (args.review_count is None):
        print("[ERROR] --rating and --review-count must be used together.", file=sys.stderr)
        sys.exit(1)

    demo = not args.name

    if demo:
        print("[INFO] Running in demo mode. Use --name and --description for your product.\n")

    if args.type == "product":
        name = args.name or "SEO Title Generator Utility"
        description = args.description or "High-CTR algorithmic product title optimizer with character limits and batch CSV support."
        schema = build_product_schema(
            name=name,
            description=description,
            sku=args.sku,
            price=args.price,
            currency=args.currency,
            brand=args.brand,
            in_stock=not args.out_of_stock,
            images=args.images,
            rating=args.rating,
            review_count=args.review_count,
            price_valid_until=args.price_valid_until,
        )
    elif args.type == "article":
        name = args.name or "Complete Guide to SEO Automation"
        description = args.description or "A comprehensive guide to automating SEO workflows with Python."
        schema = build_article_schema(name=name, description=description, url=args.url)
    elif args.type == "breadcrumb":
        # Demo breadcrumb
        schema = build_breadcrumb_schema([
            {"name": "Home", "url": "https://syntaxcraft.dev/"},
            {"name": "Tools", "url": "https://syntaxcraft.dev/tools/"},
            {"name": "SEO Title Generator", "url": "https://syntaxcraft.dev/tools/seo-title-generator"},
        ])
    else:
        print(f"[ERROR] Unknown schema type: {args.type}", file=sys.stderr)
        sys.exit(1)

    json_ld = f'<script type="application/ld+json">\n{json.dumps(schema, indent=2, ensure_ascii=False)}\n</script>'
    print(json_ld)


if __name__ == "__main__":
    main()
