import os
import re
import json

SITE_TS = r"C:\Users\Alone\Desktop\syntaxcraft.dev\data\site.ts"
LISTINGS_VUE = r"C:\Users\Alone\Desktop\syntaxcraft.dev\pages\listings.vue"
INDEX_VUE = r"C:\Users\Alone\Desktop\syntaxcraft.dev\pages\index.vue"

# 17 Products with exact Lemon Squeezy checkout URLs
CHECKOUT_MAP = {
    "slug": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/f1337fd3-de71-4da5-977e-06c0594fb8e8",
    "robots": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/73ed05e5-cd80-4035-80ac-1ae36e104d91",
    "title": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/98215071-4f68-40d9-92b9-b21d542ef110",
    "meta_desc": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/2277ca6f-e811-4549-ab78-90848d95ef23",
    "sitemap": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/6caa2062-0e9c-4466-ba09-cbcae786a94e",
    "opengraph": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/b8a331ae-ce24-40d0-9a2f-402e934724a6",
    "headings": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/06e2d5cc-e784-4e18-bfe6-3371e1ea7c66",
    "image_alt": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/51bdf402-96bc-4a9c-8d5a-71a9b483ecbe",
    "hreflang": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/df59b79f-b15e-468b-94c0-7294eedb9254",
    "keyword_density": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/5a182bc4-e72e-4bc5-8b87-046a017745cd",
    "readability": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/3b4283d6-ea34-4e24-8cde-7783a3857b31",
    "redirects": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/5bda11e7-6beb-4915-971e-046281c0612d",
    "schema": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/f26b61c5-9d11-4663-8d18-80ad5060423d",
    "faq_schema": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/19e8a11e-2c55-4c70-b1e9-c6b34a619392",
    "cli": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/7989362a-52ce-4fbe-8a13-6db37ff8f42e",
    "all_in_one": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/c933f370-3cfd-4481-8685-66dfb26d6a34",
    "pro_suite": "https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/bea7e38c-05ef-47c0-853a-efd098ec33c7"
}

print("1. Updating site.ts...")
with open(SITE_TS, "r", encoding="utf-8") as f:
    site_content = f.read()

# Replace pricing CTAs with direct checkout links
site_content = site_content.replace(
    "id: 'all-in-one-toolkit',\n      name: 'All-in-One SEO & Webmaster Suite',",
    "id: 'all-in-one-toolkit',\n      name: 'All-in-One SEO & Webmaster Suite',\n      checkoutUrl: '" + CHECKOUT_MAP["all_in_one"] + "',"
)
site_content = site_content.replace(
    "id: 'pro-web-suite',\n      name: 'Pro Web Platform & SEO Suite',",
    "id: 'pro-web-suite',\n      name: 'Pro Web Platform & SEO Suite',\n      checkoutUrl: '" + CHECKOUT_MAP["pro_suite"] + "',"
)

# Tool checkouts
tool_replacements = [
    ("id: 'bulk-slug-formatter'", CHECKOUT_MAP["slug"]),
    ("id: 'robots-directive-builder'", CHECKOUT_MAP["robots"]),
    ("id: 'seo-title-generator'", CHECKOUT_MAP["title"]),
    ("id: 'meta-description-engine'", CHECKOUT_MAP["meta_desc"]),
    ("id: 'xml-sitemap-generator'", CHECKOUT_MAP["sitemap"]),
    ("id: 'opengraph-card-generator'", CHECKOUT_MAP["opengraph"]),
    ("id: 'heading-structure-auditor'", CHECKOUT_MAP["headings"]),
    ("id: 'image-alt-optimizer'", CHECKOUT_MAP["image_alt"]),
    ("id: 'canonical-hreflang-manager'", CHECKOUT_MAP["hreflang"]),
    ("id: 'keyword-density-analyzer'", CHECKOUT_MAP["keyword_density"]),
    ("id: 'content-readability-optimizer'", CHECKOUT_MAP["readability"]),
    ("id: 'redirect-rules-builder'", CHECKOUT_MAP["redirects"]),
    ("id: 'product-schema-generator'", CHECKOUT_MAP["schema"]),
    ("id: 'faq-article-schema-engine'", CHECKOUT_MAP["faq_schema"]),
    ("id: 'internal-link-optimizer'", CHECKOUT_MAP["cli"]),
]

for t_id, url in tool_replacements:
    if f"checkoutUrl: '{url}'" not in site_content:
        site_content = site_content.replace(
            f"{t_id},",
            f"{t_id},\n      checkoutUrl: '{url}',"
        )

with open(SITE_TS, "w", encoding="utf-8") as f:
    f.write(site_content)
print("✓ site.ts updated!")

print("2. Updating listings.vue...")
with open(LISTINGS_VUE, "r", encoding="utf-8") as f:
    list_content = f.read()

# Add checkoutUrl to all 17 listings products
listings_map = [
    ("id: 'p01',", CHECKOUT_MAP["slug"]),
    ("id: 'p02',", CHECKOUT_MAP["robots"]),
    ("id: 'p03',", CHECKOUT_MAP["title"]),
    ("id: 'p04',", CHECKOUT_MAP["meta_desc"]),
    ("id: 'p05',", CHECKOUT_MAP["sitemap"]),
    ("id: 'p06',", CHECKOUT_MAP["opengraph"]),
    ("id: 'p07',", CHECKOUT_MAP["headings"]),
    ("id: 'p08',", CHECKOUT_MAP["image_alt"]),
    ("id: 'p09',", CHECKOUT_MAP["hreflang"]),
    ("id: 'p10',", CHECKOUT_MAP["keyword_density"]),
    ("id: 'p11',", CHECKOUT_MAP["readability"]),
    ("id: 'p12',", CHECKOUT_MAP["redirects"]),
    ("id: 'p13',", CHECKOUT_MAP["schema"]),
    ("id: 'p14',", CHECKOUT_MAP["faq_schema"]),
    ("id: 'p15',", CHECKOUT_MAP["cli"]),
    ("id: 'p16',", CHECKOUT_MAP["all_in_one"]),
    ("id: 'p17',", CHECKOUT_MAP["pro_suite"]),
]

for p_id, url in listings_map:
    if f"checkoutUrl: '{url}'" not in list_content:
        list_content = list_content.replace(
            f"{p_id}\n    price:",
            f"{p_id}\n    checkoutUrl: '{url}',\n    price:"
        )

with open(LISTINGS_VUE, "w", encoding="utf-8") as f:
    f.write(list_content)
print("✓ listings.vue updated!")

print("3. Updating index.vue buttons...")
with open(INDEX_VUE, "r", encoding="utf-8") as f:
    index_content = f.read()

# Update tool cards to link directly to checkoutUrl
old_tool_btn = """              <NuxtLink
                :to="'/contact?tool=' + tool.id"
                class="btn btn-secondary btn-sm"
                style="width: 100%; text-align: center; justify-content: center; font-size: 0.84rem;"
              >
                License Utility ({{ tool.price }})"""

new_tool_btn = """              <a
                :href="tool.checkoutUrl || ('/contact?tool=' + tool.id)"
                target="_blank"
                class="btn btn-primary btn-sm"
                style="width: 100%; text-align: center; justify-content: center; font-size: 0.84rem; text-decoration: none;"
              >
                Instant Buy ({{ tool.price }}) &rarr;"""

if old_tool_btn in index_content:
    index_content = index_content.replace(old_tool_btn, new_tool_btn)

# Update pricing cards
old_pricing_btn = """              <NuxtLink
                :to="plan.id === 'single-tool' ? '/#tools' : '/contact?plan=' + plan.id"
                :class="['btn', plan.popular ? 'btn-primary' : 'btn-secondary']"
                style="width: 100%; text-align: center; justify-content: center; margin-top: 24px;"
              >
                {{ plan.cta }}"""

new_pricing_btn = """              <a
                v-if="plan.checkoutUrl"
                :href="plan.checkoutUrl"
                target="_blank"
                :class="['btn', plan.popular ? 'btn-primary' : 'btn-secondary']"
                style="width: 100%; text-align: center; justify-content: center; margin-top: 24px; text-decoration: none;"
              >
                {{ plan.cta }} (Instant Checkout) &rarr;
              </a>
              <NuxtLink
                v-else
                :to="plan.id === 'single-tool' ? '/#tools' : '/contact?plan=' + plan.id"
                :class="['btn', plan.popular ? 'btn-primary' : 'btn-secondary']"
                style="width: 100%; text-align: center; justify-content: center; margin-top: 24px;"
              >
                {{ plan.cta }}"""

if old_pricing_btn in index_content:
    index_content = index_content.replace(old_pricing_btn, new_pricing_btn)

with open(INDEX_VUE, "w", encoding="utf-8") as f:
    f.write(index_content)
print("✓ index.vue updated!")
print("\n✅ All checkout URLs linked into website codebase!")

