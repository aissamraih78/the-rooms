"""
OpenGraph & Twitter Card Meta Synthesizer — SyntaxCraft SEO Tools
Generates complete Open Graph (og:*) and Twitter Card meta tags
for maximum social sharing visibility across Facebook, LinkedIn, Twitter/X,
and WhatsApp — on your own website pages.

Usage:
    python opengraph_generator.py --title "My Product" --description "Best SEO tool" \
        --url "https://syntaxcraft.dev/tools/seo-title" --image "https://syntaxcraft.dev/og.jpg"

Author: SyntaxCraft Studio | contact@syntaxcraft.dev
"""

import argparse
import json
from typing import Optional


OG_IMAGE_MIN_WIDTH = 1200
OG_IMAGE_MIN_HEIGHT = 630
OG_IMAGE_RECOMMENDED = "1200x630"
TWITTER_CARD_TYPES = {"summary", "summary_large_image", "app", "player"}


def validate_og_image(width: Optional[int], height: Optional[int]) -> list[str]:
    """Validate og:image dimensions."""
    warnings = []
    if width and height:
        if width < OG_IMAGE_MIN_WIDTH or height < OG_IMAGE_MIN_HEIGHT:
            warnings.append(
                f"Image {width}x{height} is below the recommended {OG_IMAGE_RECOMMENDED}. "
                "Facebook may not display it. Use at least 1200x630 pixels."
            )
        ratio = width / height
        if not (1.85 <= ratio <= 2.0):
            warnings.append(
                f"Image aspect ratio {ratio:.2f}:1 deviates from ideal 1.91:1 (1200x630). "
                "Facebook may crop your image unexpectedly."
            )
    else:
        warnings.append(
            "No image dimensions provided. Verify your og:image is at least 1200x630px."
        )
    return warnings


def generate_og_tags(
    title: str,
    description: str,
    url: str,
    image_url: str,
    site_name: str = "SyntaxCraft",
    og_type: str = "website",
    twitter_card: str = "summary_large_image",
    twitter_site: Optional[str] = None,
    locale: str = "en_US",
    image_width: Optional[int] = None,
    image_height: Optional[int] = None,
) -> dict:
    """
    Generate complete OG + Twitter Card meta tag set.

    Returns:
        {
            "html_tags": str,           # Ready-to-paste HTML snippet
            "json_structured": dict,    # Structured representation
            "warnings": list[str],
            "char_counts": dict
        }
    """
    warnings = []

    # Validation
    if len(title) > 60:
        warnings.append(
            f"og:title is {len(title)} chars. Facebook truncates after ~60 chars in some placements."
        )
    if len(description) > 200:
        warnings.append(
            f"og:description is {len(description)} chars. Keep under 200 for best display."
        )
    if not image_url.startswith("https://"):
        warnings.append(
            "og:image URL uses HTTP instead of HTTPS. Facebook requires HTTPS images for secure pages."
        )
    if twitter_card not in TWITTER_CARD_TYPES:
        warnings.append(
            f"Invalid twitter:card type '{twitter_card}'. Valid: {', '.join(TWITTER_CARD_TYPES)}"
        )
        twitter_card = "summary_large_image"

    image_warnings = validate_og_image(image_width, image_height)
    warnings.extend(image_warnings)

    # Build tag set
    tags = {
        "og:type": og_type,
        "og:url": url,
        "og:title": title,
        "og:description": description,
        "og:image": image_url,
        "og:site_name": site_name,
        "og:locale": locale,
    }
    if image_width:
        tags["og:image:width"] = str(image_width)
    if image_height:
        tags["og:image:height"] = str(image_height)
    tags["og:image:alt"] = title  # Accessibility best practice

    twitter_tags = {
        "twitter:card": twitter_card,
        "twitter:title": title[:70],
        "twitter:description": description[:200],
        "twitter:image": image_url,
        "twitter:image:alt": title[:420],
    }
    if twitter_site:
        twitter_tags["twitter:site"] = twitter_site if twitter_site.startswith("@") else f"@{twitter_site}"

    # Generate HTML
    html_lines = ["<!-- Open Graph / Facebook / LinkedIn / WhatsApp -->"]
    for prop, content in tags.items():
        html_lines.append(f'<meta property="{prop}" content="{content}" />')

    html_lines.append("")
    html_lines.append("<!-- Twitter / X Card -->")
    for name, content in twitter_tags.items():
        html_lines.append(f'<meta name="{name}" content="{content}" />')

    html_output = "\n".join(html_lines)

    return {
        "html_tags": html_output,
        "json_structured": {
            "open_graph": tags,
            "twitter_card": twitter_tags,
        },
        "warnings": warnings,
        "char_counts": {
            "title": len(title),
            "description": len(description),
            "image_url": len(image_url),
        },
        "validation_status": "✅ READY" if not warnings else f"⚠️ {len(warnings)} warning(s) — review before publishing",
    }


def main():
    parser = argparse.ArgumentParser(
        description="SyntaxCraft OpenGraph & Twitter Card Generator"
    )
    parser.add_argument("--title", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--url", required=True, help="Canonical page URL")
    parser.add_argument("--image", required=True, help="og:image URL (HTTPS, 1200x630 recommended)")
    parser.add_argument("--site-name", default="SyntaxCraft")
    parser.add_argument("--type", default="website", dest="og_type")
    parser.add_argument("--twitter-card", default="summary_large_image")
    parser.add_argument("--twitter-site", default=None, help="@handle for Twitter")
    parser.add_argument("--locale", default="en_US")
    parser.add_argument("--image-width", type=int, default=None)
    parser.add_argument("--image-height", type=int, default=None)
    args = parser.parse_args()

    result = generate_og_tags(
        title=args.title,
        description=args.description,
        url=args.url,
        image_url=args.image,
        site_name=args.site_name,
        og_type=args.og_type,
        twitter_card=args.twitter_card,
        twitter_site=args.twitter_site,
        locale=args.locale,
        image_width=args.image_width,
        image_height=args.image_height,
    )

    print("\n=== Generated Meta Tags ===")
    print(result["html_tags"])
    print("\n=== Validation Report ===")
    print(json.dumps({
        "char_counts": result["char_counts"],
        "warnings": result["warnings"],
        "status": result["validation_status"],
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
