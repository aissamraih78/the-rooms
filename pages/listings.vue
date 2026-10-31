<script setup lang="ts">
import { ref } from 'vue'

useHead({
  title: 'Product Listings Hub — SyntaxCraft Studio',
  meta: [
    { name: 'description', content: 'Ready-to-copy product listings, descriptions, and file mapping for SyntaxCraft Lemon Squeezy store catalog.' }
  ]
})

const copiedField = ref<string | null>(null)

function copyToClipboard(text: string, id: string) {
  navigator.clipboard.writeText(text).then(() => {
    copiedField.value = id
    setTimeout(() => {
      if (copiedField.value === id) {
        copiedField.value = null
      }
    }, 2000)
  })
}

const products = [
  {
    id: 'p01',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/f1337fd3-de71-4da5-977e-06c0594fb8e8',
    price: '3.99',
    category: 'Micro-Utility',
    name: 'High-Performance SEO URL Slug Sanitizer',
    file: '01_URL_Slug_Sanitizer_EUR_3.99.zip',
    description: `A lightweight, high-performance Python utility that cleans and formats URL slugs for e-commerce stores and CMS publications.

Key Features:
• Removes stopwords and non-ASCII accents using Unicode NFKD normalization.
• Prevents search engine duplicate content penalties with clean kebab-case formatting.
• Hard character limit guard with smart word-boundary truncation.
• Bulk file processing support (handles 10,000+ titles in milliseconds).
• Zero external dependencies, pure Python 3.10+ execution.
• Perpetual commercial software license included.`
  },
  {
    id: 'p02',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/73ed05e5-cd80-4035-80ac-1ae36e104d91',
    price: '4.99',
    category: 'Webmaster Security',
    name: 'Robots.txt Security & Directive Generator',
    file: '02_Robots_Directive_Builder_EUR_4.99.zip',
    description: `Constructs, parses, and validates fine-grained robots.txt directives for website administrators and SEO specialists.

Key Features:
• Crawl budget preservation: Regulate crawl frequency and block aggressive scrapers.
• Search engine bot identification: Pre-configured rules for Googlebot, Bingbot, and social crawlers.
• Syntax verification parser: Detects accidental site-wide disallow rules and broken directives.
• Automated Sitemap index integration.
• Includes full source code and CLI usage documentation.
• Perpetual commercial license for unlimited client websites.`
  },
  {
    id: 'p03',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/98215071-4f68-40d9-92b9-b21d542ef110',
    price: '8.99',
    category: 'Titles & Content',
    name: 'E-Commerce SEO Title Generator Engine',
    file: '03_SEO_Title_Generator_EUR_8.99.zip',
    description: `Algorithmic product title optimization script engineered for high Click-Through-Rates (CTR) and Google SERP compliance. Includes search intent weighting, 60-character hard truncation guard, and bulk CSV batch processing. Perpetual commercial license included.`
  },
  {
    id: 'p04',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/2277ca6f-e811-4549-ab78-90848d95ef23',
    price: '8.99',
    category: 'Titles & Content',
    name: 'CTR Meta Description Synthesizer',
    file: '04_CTR_Meta_Description_Engine_EUR_8.99.zip',
    description: `Automates high-converting, persuasive meta descriptions calibrated to Google's 155-160 character snippet window. Includes 3-variant generation (CTA-led, keyword-first, and content-derived) with Arial SERP pixel measurement simulation.`
  },
  {
    id: 'p05',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/6caa2062-0e9c-4466-ba09-cbcae786a94e',
    price: '8.99',
    category: 'Site Structure',
    name: 'XML Sitemap Protocol 0.9 Validator',
    file: '05_XML_Sitemap_Validator_EUR_8.99.zip',
    description: `Parses and validates sitemap.xml files against the official Sitemaps.org 0.9 protocol standards. Detects broken links, missing lastmod dates, duplicate URLs, and 50,000-URL chunking limits with sitemapindex support.`
  },
  {
    id: 'p06',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/b8a331ae-ce24-40d0-9a2f-402e934724a6',
    price: '8.99',
    category: 'Metadata & Social',
    name: 'OpenGraph & Twitter Card Meta Synthesizer',
    file: '06_OpenGraph_Card_Generator_EUR_8.99.zip',
    description: `Generates flawless social sharing tags for Facebook, LinkedIn, Twitter/X, and WhatsApp with real-time 1200x630 dimension validation and summary_large_image Twitter card formatting.`
  },
  {
    id: 'p07',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/06e2d5cc-e784-4e18-bfe6-3371e1ea7c66',
    price: '8.99',
    category: 'Site Structure',
    name: 'H1-H6 Heading Hierarchy & Accessibility Auditor',
    file: '07_Heading_Structure_Auditor_EUR_8.99.zip',
    description: `Audits HTML heading structures for strict WCAG 2.1 accessibility compliance and logical search hierarchy. Detects skipped levels, missing H1s, and outputs an automated Markdown Table of Contents.`
  },
  {
    id: 'p08',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/51bdf402-96bc-4a9c-8d5a-71a9b483ecbe',
    price: '8.99',
    category: 'Image & Media SEO',
    name: 'Image Alt Tag & Filename SEO Optimizer',
    file: '08_Image_Alt_SEO_Formatter_EUR_8.99.zip',
    description: `Sanitizes image filenames into clean kebab-case and generates descriptive, keyword-targeted Alt attributes compliant with accessibility standards and Google Image search ranking.`
  },
  {
    id: 'p09',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/df59b79f-b15e-468b-94c0-7294eedb9254',
    price: '8.99',
    category: 'International SEO',
    name: 'Canonical & Multi-Lingual Hreflang Tag Manager',
    file: '09_Canonical_Hreflang_Manager_EUR_8.99.zip',
    description: `Validates reciprocal hreflang annotations across multi-language stores to eliminate duplicate content penalties. Features ISO 639-1 language validation and automated x-default fallback tag generation.`
  },
  {
    id: 'p10',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/5a182bc4-e72e-4bc5-8b87-046a017745cd',
    price: '11.99',
    category: 'Content Analysis',
    name: 'Keyword Density & TF-IDF Over-Optimization Guard',
    file: '10_Keyword_Density_Analyzer_EUR_11.99.zip',
    description: `Calculates term frequency and keyword density to protect website copy from search engine keyword-stuffing penalties. Features multi-word phrase matching and safe zone density detection (0.5% – 2.5%).`
  },
  {
    id: 'p11',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/3b4283d6-ea34-4e24-8cde-7783a3857b31',
    price: '11.99',
    category: 'Content Analysis',
    name: 'Content Readability & Paragraph Flow Optimizer',
    file: '11_Content_Readability_Optimizer_EUR_11.99.zip',
    description: `Analyzes body copy, formats paragraph lengths, and computes Flesch-Kincaid readability scores for optimal reader engagement. Automatically restructures dense text into 45-word optimal paragraphs.`
  },
  {
    id: 'p12',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/5bda11e7-6beb-4915-971e-046281c0612d',
    price: '11.99',
    category: 'Server & Redirects',
    name: '301/302 Redirect Rules & RegEx Builder',
    file: '12_Redirect_Rules_Builder_EUR_11.99.zip',
    description: `Transforms legacy URL paths into optimized server redirection rules for Nginx and Apache (.htaccess) configurations. Prevents redirect loops, preserves query strings, and handles trailing slash normalization.`
  },
  {
    id: 'p13',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/f26b61c5-9d11-4663-8d18-80ad5060423d',
    price: '14.99',
    category: 'Structured Data',
    name: 'Product Schema JSON-LD Structured Data Builder',
    file: '13_Product_Schema_Generator_EUR_14.99.zip',
    description: `Generates Schema.org Product, Offer, and AggregateRating JSON-LD structured data for Google Rich Results. Includes dynamic price, currency, SKU injection, and Search Console compliance verification.`
  },
  {
    id: 'p14',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/19e8a11e-2c55-4c70-b1e9-c6b34a619392',
    price: '14.99',
    category: 'Structured Data',
    name: 'FAQ & Article Rich Result Schema Engine',
    file: '14_FAQ_Article_Schema_Engine_EUR_14.99.zip',
    description: `Synthesizes Google-verified FAQPage and Article Schema.org structured data blocks to maximize search result visibility with expandable rich result accordions.`
  },
  {
    id: 'p15',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/7989362a-52ce-4fbe-8a13-6db37ff8f42e',
    price: '29.99',
    category: 'Developer CLI',
    name: 'Unified SEO Terminal CLI Manager',
    file: '15_Unified_SEO_Terminal_CLI_EUR_29.99.zip',
    description: `A unified terminal control center allowing webmasters to execute, test, and manage all specialized SEO utilities from a single CLI interface. Includes color-coded execution telemetry and isolated runtimes.`
  },
  {
    id: 'p16',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/c933f370-3cfd-4481-8685-66dfb26d6a34',
    price: '56.99',
    category: 'Complete Suite',
    name: 'All-in-One SEO & Webmaster Automation Suite',
    file: '16_All_In_One_SEO_Suite_EUR_56.99.zip',
    description: `The flagship comprehensive bundle containing all 15 specialized Python SEO and webmaster automation scripts. Includes 28 passing automated unit tests, unified CLI terminal dashboard, bulk CSV processing pipelines, and Docker container support.`
  },
  {
    id: 'p17',
    checkoutUrl: 'https://syntaxcraft2026dev.lemonsqueezy.com/checkout/buy/bea7e38c-05ef-47c0-853a-efd098ec33c7',
    price: '71.99',
    category: 'Full Platform',
    name: 'Complete SyntaxCraft Pro Web Platform & SEO Engine Suite',
    file: '17_SyntaxCraft_Pro_Web_Platform_EUR_71.99.zip',
    description: `Complete full-stack production web application codebase built with Nuxt 3, Vue 3, and TypeScript, integrated directly with our entire SEO automation pipeline. Includes client-side terminal simulation, Lemon Squeezy checkout webhook handlers, and full deployment documentation.`
  }
]
</script>

<template>
  <div class="container" style="padding: 50px 0 100px; max-width: 960px;">
    <!-- Top Bar -->
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
      <NuxtLink to="/" class="btn btn-secondary btn-sm">
        &larr; Back to Home
      </NuxtLink>
      <span class="badge" style="background: #10b981; color: white;">
        ✓ 17 Ready-to-Publish Listings
      </span>
    </div>

    <!-- Header Banner -->
    <div style="background: white; border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: 32px; margin-bottom: 36px; box-shadow: 0 4px 20px rgba(0,0,0,0.03);">
      <h1 style="font-size: 2.2rem; margin-bottom: 12px; color: var(--text-primary);">
        ⚡ Lemon Squeezy Fast Copy & Paste Hub
      </h1>
      <p style="color: var(--text-secondary); font-size: 1.05rem; line-height: 1.6; margin-bottom: 18px;">
        Use this dedicated dashboard to rapidly copy product titles, prices, and descriptions straight into your Lemon Squeezy control panel. Corresponding ZIP files are located in:
      </p>
      <div style="background: #f1f5f9; padding: 10px 16px; border-radius: 6px; font-family: var(--font-mono); font-size: 0.88rem; color: #0f172a; word-break: break-all;">
        📁 C:\Users\Alone\Desktop\LemonSqueezy_Products\
      </div>
    </div>

    <!-- Products Grid -->
    <div style="display: grid; gap: 28px;">
      <div
        v-for="(p, index) in products"
        :key="p.id"
        style="background: white; border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: 28px; box-shadow: 0 2px 12px rgba(0,0,0,0.02); transition: border-color 0.2s ease;"
      >
        <!-- Product Header Bar -->
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 18px; border-bottom: 1px solid #f1f5f9; padding-bottom: 14px;">
          <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-weight: 800; font-size: 1.1rem; color: #64748b; font-family: var(--font-mono);">
              #{{ String(index + 1).padStart(2, '0') }}
            </span>
            <span class="badge" style="font-size: 0.75rem; padding: 3px 10px;">
              {{ p.category }}
            </span>
          </div>

          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 1.4rem; font-weight: 800; color: #0284c7; font-family: var(--font-mono);">
              €{{ p.price }}
            </span>
            <button
              class="btn btn-secondary btn-sm"
              style="padding: 4px 10px; font-size: 0.78rem;"
              @click="copyToClipboard(p.price, p.id + '_price')"
            >
              {{ copiedField === p.id + '_price' ? '✓ Copied' : 'Copy Price' }}
            </button>
          </div>
        </div>

        <!-- Product Name Section -->
        <div style="margin-bottom: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <label style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b;">
              Product Name
            </label>
            <button
              class="btn btn-secondary btn-sm"
              style="padding: 4px 12px; font-size: 0.8rem;"
              @click="copyToClipboard(p.name, p.id + '_name')"
            >
              {{ copiedField === p.id + '_name' ? '✓ Copied Name' : 'Copy Name' }}
            </button>
          </div>
          <div
            style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 12px 14px; font-size: 1.05rem; font-weight: 600; color: #0f172a; cursor: pointer;"
            @click="copyToClipboard(p.name, p.id + '_name')"
            title="Click to copy name"
          >
            {{ p.name }}
          </div>
        </div>

        <!-- Description Section -->
        <div style="margin-bottom: 18px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <label style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b;">
              Description (Paste into Lemon Squeezy Description)
            </label>
            <button
              class="btn btn-primary btn-sm"
              style="padding: 4px 14px; font-size: 0.8rem;"
              @click="copyToClipboard(p.description, p.id + '_desc')"
            >
              {{ copiedField === p.id + '_desc' ? '✓ Copied Description' : 'Copy Description' }}
            </button>
          </div>
          <textarea
            readonly
            rows="5"
            style="width: 100%; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 12px 14px; font-size: 0.88rem; line-height: 1.6; color: #334155; resize: vertical; font-family: inherit;"
            @click="copyToClipboard(p.description, p.id + '_desc')"
          >{{ p.description }}</textarea>
        </div>

        <!-- Direct Lemon Squeezy Checkout Button -->
        <div style="display: flex; justify-content: space-between; align-items: center; background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 6px; padding: 10px 14px; margin-bottom: 12px;">
          <span style="font-size: 0.85rem; color: #6b21a8; font-weight: 600;">
            ⚡ Verified Digital License & Instant Download
          </span>
          <a
            v-if="p.checkoutUrl"
            :href="p.checkoutUrl"
            target="_blank"
            class="btn btn-primary btn-sm"
            style="text-decoration: none; padding: 6px 16px; font-weight: 700; background: #7c3aed; border-color: #6d28d9;"
          >
            Buy on Lemon Squeezy (€{{ p.price }}) &rarr;
          </a>
        </div>

        <!-- File Attachment Section -->
        <div style="display: flex; justify-content: space-between; align-items: center; background: #eff6ff; border: 1px dashed #bfdbfe; border-radius: 6px; padding: 10px 14px;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 1.1rem;">📦</span>
            <span style="font-size: 0.86rem; color: #1e40af; font-weight: 600; font-family: var(--font-mono);">
              {{ p.file }}
            </span>
          </div>
          <button
            class="btn btn-secondary btn-sm"
            style="padding: 4px 10px; font-size: 0.78rem;"
            @click="copyToClipboard(p.file, p.id + '_file')"
          >
            {{ copiedField === p.id + '_file' ? '✓ Copied File' : 'Copy Filename' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

