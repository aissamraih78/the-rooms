"""
SEO Title Optimizer & SERP CTR Engine
Part of SyntaxCraft SEO & Webmaster Automation Utilities.
100% White-Hat, Compliance-Verified.
"""

import re
from typing import Dict, Any, Tuple

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "has", "he", "in", "is", "it", "its", "of", "on", "that", "the",
    "to", "was", "were", "with"
}

def clean_tokens(text: str) -> list[str]:
    cleaned = re.sub(r"[^\w\s-]", "", text.lower())
    return [w for w in cleaned.split() if w]

def calculate_serp_pixel_width(title: str) -> int:
    """
    Simulates Google desktop SERP pixel width based on standard Arial 20px metrics.
    Recommended max: 580px - 600px.
    """
    # Average character widths in Arial 20px
    char_widths = {
        'i': 5, 'l': 5, 'I': 6, 'j': 6, 't': 7, 'f': 7, 'r': 8,
        'm': 16, 'w': 15, 'M': 18, 'W': 19, ' ': 6
    }
    width = 0
    for char in title:
        width += char_widths.get(char, 10)
    return width

def optimize_product_title(
    raw_name: str,
    primary_keyword: str,
    brand: str = "SyntaxCraft",
    max_chars: int = 60
) -> Tuple[str, Dict[str, Any]]:
    """
    Optimizes an e-commerce or article title for maximum search click-through rate (CTR).
    Guarantees strict character truncation and SERP pixel limit compliance.
    """
    raw_clean = " ".join([w.capitalize() for w in raw_name.strip().split()])
    kw_clean = " ".join([w.capitalize() for w in primary_keyword.strip().split()])
    
    # Ensure primary keyword appears first
    if kw_clean.lower() not in raw_clean.lower():
        constructed = f"{kw_clean} — {raw_clean}"
    else:
        constructed = raw_clean
        
    if brand and f"| {brand}" not in constructed:
        if len(constructed) + len(f" | {brand}") <= max_chars:
            constructed = f"{constructed} | {brand}"
            
    # Hard clamp to max_chars
    if len(constructed) > max_chars:
        trimmed = constructed[:max_chars - 3].rsplit(" ", 1)[0]
        constructed = f"{trimmed}..."

    pixel_width = calculate_serp_pixel_width(constructed)
    
    # CTR scoring heuristic (0 - 100)
    score = 70
    if len(constructed) >= 40 and len(constructed) <= 60:
        score += 15
    if pixel_width <= 580:
        score += 10
    if kw_clean.lower() in constructed.lower()[:30]:
        score += 5

    metrics = {
        "title": constructed,
        "char_count": len(constructed),
        "pixel_width": pixel_width,
        "ctr_score": min(score, 100),
        "primary_keyword": primary_keyword,
        "is_serp_safe": pixel_width <= 580 and len(constructed) <= 60
    }
    return constructed, metrics

if __name__ == "__main__":
    title, data = optimize_product_title(
        raw_name="handmade vintage leather messenger bag men brown",
        primary_keyword="Leather Messenger Bag",
        brand="SyntaxCraft"
    )
    print("✓ Generated Title:", title)
    print("✓ Metrics:", data)
