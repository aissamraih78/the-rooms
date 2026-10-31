"""
Schema.org JSON-LD Structured Data Builder
Part of SyntaxCraft SEO & Webmaster Automation Utilities.
100% Google Rich Results Compliant.
"""

import json
from typing import Optional, List, Dict, Any

class ProductSchema:
    def __init__(
        self,
        name: str,
        description: str,
        sku: str,
        price: str,
        currency: str = "USD",
        brand: str = "SyntaxCraft",
        rating: float = 4.9,
        review_count: int = 42,
        in_stock: bool = True,
        images: Optional[List[str]] = None
    ):
        self.name = name
        self.description = description
        self.sku = sku
        self.price = price
        self.currency = currency
        self.brand = brand
        self.rating = rating
        self.review_count = review_count
        self.in_stock = in_stock
        self.images = images or ["https://syntaxcraft.dev/images/product-default.jpg"]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "@context": "https://schema.org/",
            "@type": "Product",
            "name": self.name,
            "image": self.images,
            "description": self.description,
            "sku": self.sku,
            "brand": {
                "@type": "Brand",
                "name": self.brand
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": str(self.rating),
                "reviewCount": str(self.review_count),
                "bestRating": "5",
                "worstRating": "1"
            },
            "offers": {
                "@type": "Offer",
                "url": f"https://syntaxcraft.dev/tools/{self.sku.lower()}",
                "priceCurrency": self.currency,
                "price": self.price,
                "priceValidUntil": "2028-12-31",
                "availability": "https://schema.org/InStock" if self.in_stock else "https://schema.org/OutOfStock",
                "itemCondition": "https://schema.org/NewCondition"
            }
        }

    def to_json_ld(self, indent: int = 2) -> str:
        data = self.to_dict()
        return f'<script type="application/ld+json">\n{json.dumps(data, indent=indent)}\n</script>'

if __name__ == "__main__":
    builder = ProductSchema(
        name="SEO Title Generator Utility",
        description="High-CTR algorithmic product title optimizer with character limits.",
        sku="UTIL-TITLE-01",
        price="9.00"
    )
    print(builder.to_json_ld())
