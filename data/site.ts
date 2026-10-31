export const site = {
  name: 'SyntaxCraft',
  brand: 'SyntaxCraft Studio',
  tagline: 'Production-Grade SEO Automation Tools, Title Engines & Website Management Utilities',
  description: 'We develop and license specialized, 100% compliant SEO automation scripts, product title generators, metadata synthesizers, and webmaster administration utilities.',
  email: 'contact@syntaxcraft.dev',
  domain: 'https://syntaxcraft.dev',
  github: 'https://github.com/syntaxcraft2026',
  location: 'Douar Ait Ouaarab, Ghassate, Ouarzazate 45000, Morocco',
  city: 'Ouarzazate, Morocco',
  availability: 'Available for Instant Digital Delivery',
  responseSla: 'Guaranteed response within 12 hours',
  stats: [
    { label: 'SEO & Webmaster Tools Developed', value: '15+ Utilities' },
    { label: 'Digital Fulfillment Time', value: 'Instant Download' },
    { label: 'Search Engine Guideline Compliance', value: '100% White-Hat' },
    { label: 'Full Source Code Ownership', value: 'Perpetual' }
  ],
  nav: [
    { label: 'SEO Tools Catalog', href: '/#tools' },
    { label: 'Live Sandbox', href: '/#showcase' },
    { label: 'Pricing & Bundles', href: '/#pricing' },
    { label: 'Fulfillment', href: '/#process' },
    { label: 'FAQ', href: '/#faq' },
    { label: 'Support', href: '/contact' }
  ],
  tools: [
    {
      id: 'seo-title-generator',
      name: 'E-Commerce SEO Title Generator',
      category: 'Content & Titles',
      price: '$9',
      deck: 'Generates high-CTR, intent-optimized product titles based on character limits and search engine ranking factors.',
      features: ['Search intent weighting', '60-character hard truncation guard', 'Primary & secondary keyword injection', 'Bulk CSV input/output']
    },
    {
      id: 'meta-description-engine',
      name: 'CTR Meta Description Synthesizer',
      category: 'Content & Titles',
      price: '$9',
      deck: 'Automates persuasive, high-converting meta descriptions calibrated for 155-160 character Google SERP snippets.',
      features: ['Call-To-Action (CTA) formulation', 'SERP pixel-width measurement', 'Keyword highlighting preview', 'Zero boilerplate duplication']
    },
    {
      id: 'keyword-cluster-builder',
      name: 'Semantic Keyword Cluster Engine',
      category: 'Keyword Research',
      price: '$19',
      deck: 'Clusters raw keyword lists into topical silos and content categories using semantic similarity algorithms.',
      features: ['Levenshtein & TF-IDF clustering', 'Search intent classification', 'Parent-topic mapping', 'Clean JSON/Excel exports']
    },
    {
      id: 'product-schema-generator',
      name: 'Product Schema JSON-LD Generator',
      category: 'Metadata & Schema',
      price: '$14',
      deck: 'Instantly builds Google Rich Result compliant Schema.org JSON-LD structured data for products, offers, and reviews.',
      features: ['Schema.org Product & AggregateRating', 'Google Search Console verified format', 'Automated currency & price injection', 'One-click copy or injection script']
    },
    {
      id: 'content-readability-optimizer',
      name: 'Content & Paragraph Structure Optimizer',
      category: 'Content & Titles',
      price: '$12',
      deck: 'Analyzes body copy, formats paragraph lengths, and computes Flesch-Kincaid readability scores for optimal user retention.',
      features: ['Flesch-Kincaid score calculator', 'Passive voice detection & fixers', 'Sentence length distribution analyzer', 'Smart H2/H3 transition points']
    },
    {
      id: 'heading-structure-auditor',
      name: 'H1-H6 Hierarchy & Semantic Structurer',
      category: 'Site Structure',
      price: '$9',
      deck: 'Scans and reorganizes HTML heading structures to guarantee strict WCAG accessibility and logical search hierarchy.',
      features: ['Missing H1/H2 hierarchy alerts', 'Keyword placement in subheadings', 'HTML semantic validation', 'Automated Table of Contents generator']
    },
    {
      id: 'internal-link-optimizer',
      name: 'Internal Link & Anchor Text Recommender',
      category: 'Site Structure',
      price: '$19',
      deck: 'Analyzes page text and suggests contextually relevant internal links with non-spammy anchor texts.',
      features: ['Page relevance matching', 'Anchor text diversity control', 'Orphan page connection engine', 'Silo architecture enforcement']
    },
    {
      id: 'xml-sitemap-generator',
      name: 'Automated XML & Image Sitemap Builder',
      category: 'Site Structure',
      price: '$9',
      deck: 'Builds, splits, and compresses Google-compliant sitemap.xml files with proper lastmod timestamps and priorities.',
      features: ['50,000 URL chunking support', 'Image sitemap tag integration', 'Automatic gzip compression', 'Valid sitemaps.org protocol 0.9']
    },
    {
      id: 'robots-directive-builder',
      name: 'Robots.txt Security & Directive Generator',
      category: 'Webmaster Utilities',
      price: '$5',
      deck: 'Constructs fine-grained robots.txt directives, blocks unwanted crawling agents, and regulates crawl budget.',
      features: ['User-agent blocklist management', 'Crawl-delay & Disallow rules', 'Sitemap index declaration', 'Syntax verification parser']
    },
    {
      id: 'canonical-hreflang-manager',
      name: 'Canonical & Multi-Lingual Hreflang Manager',
      category: 'Metadata & Schema',
      price: '$9',
      deck: 'Validates reciprocal hreflang annotations across multi-language stores to eliminate duplicate content penalties.',
      features: ['ISO 639-1 & ISO 3166-1 validation', 'Reciprocal link verification', 'Self-referencing canonical generator', 'Multi-regional e-commerce support']
    },
    {
      id: 'image-alt-optimizer',
      name: 'Image Alt Tag & SEO Slug Formatter',
      category: 'Content & Titles',
      price: '$9',
      deck: 'Standardizes image filenames and generates descriptive, keyword-rich Alt attributes compliant with accessibility standards.',
      features: ['Accessibility WCAG 2.1 compliance', 'Kebab-case URL slugification', 'Exif metadata stripper for speed', 'Bulk image processing script']
    },
    {
      id: 'serp-snippet-previewer',
      name: 'SERP Snippet & Pixel Truncation Previewer',
      category: 'Webmaster Utilities',
      price: '$5',
      deck: 'Accurately previews desktop and mobile Google search snippets with real font rendering to prevent ugly "..." truncations.',
      features: ['Arial 18px / 20px pixel calculation', 'Mobile vs Desktop view toggling', 'Rich snippet badge simulation', 'Instant character count telemetry']
    },
    {
      id: 'bulk-slug-formatter',
      name: 'High-Performance SEO URL Slug Formatter',
      category: 'Webmaster Utilities',
      price: '$5',
      deck: 'Sanitizes special characters, accents, and stopwords to output clean, concise, keyword-focused URL slugs.',
      features: ['Accented character transliteration', 'Stopword elimination list', 'Trailing slash & case standardizer', 'Zero redirect loop output']
    },
    {
      id: 'redirect-rules-builder',
      name: '301/302 Redirect Mapping & RegEx Builder',
      category: 'Site Structure',
      price: '$12',
      deck: 'Transforms old URL lists into optimized Nginx, Apache (.htaccess), or Cloudflare redirect rules without query string loss.',
      features: ['Regex URL wildcard matching', 'Duplicate rule detector', 'Status code 301 vs 302 selector', 'Instant server config export']
    },
    {
      id: 'opengraph-card-generator',
      name: 'OpenGraph & Twitter Card Meta Synthesizer',
      category: 'Metadata & Schema',
      price: '$5',
      deck: 'Generates flawless social sharing tags for Facebook, LinkedIn, Twitter/X, and WhatsApp with image aspect ratio guides.',
      features: ['og:image 1200x630 validation', 'summary_large_image Twitter cards', 'Fallback tag hierarchy', 'Instant HTML snippet injection']
    }
  ],
  services: [
    {
      id: 'seo-content-automation',
      icon: 'terminal',
      title: 'SEO Content & Title Engines',
      deck: 'Python algorithms to generate high-CTR titles, optimize paragraph flow, and eliminate duplicate product descriptions.',
      features: [
        'Automated product title optimization with search intent weighting',
        'Flesch-Kincaid readability scoring and sentence structure formatting',
        'Bulk CSV meta description generator with strict SERP pixel guards',
        'Keyword density and semantic silo categorization'
      ],
      tags: ['Python 3.12', 'SEO Title Engine', 'Natural Language Formatter', 'CLI Utility']
    },
    {
      id: 'schema-structured-data',
      icon: 'code',
      title: 'Schema.org & Rich Snippets Suites',
      deck: 'Structured data generators that guarantee Google Rich Results eligibility without manual coding.',
      features: [
        'Automated Product & Offer JSON-LD schema builder',
        'BreadcrumbList & Article rich snippet injectors',
        'FAQ and How-To schema generators for maximum SERP real estate',
        'Google Search Console validation ready'
      ],
      tags: ['JSON-LD', 'Schema.org', 'Rich Snippets', 'Webmaster Tool']
    },
    {
      id: 'webmaster-site-management',
      icon: 'cpu',
      title: 'Website Administration & Audit Utilities',
      deck: 'Standalone automation scripts to manage robots.txt, build XML sitemaps, and optimize internal link graphs.',
      features: [
        'Google protocol 0.9 XML sitemap generator with automatic gzip',
        'Internal link & anchor text recommendation algorithms',
        'Robots.txt security validator and crawl-budget regulator',
        '301 redirect map generator for Apache, Nginx, and Cloudflare'
      ],
      tags: ['Sitemap XML', 'Robots.txt', 'Internal Links', 'Site Health']
    },
    {
      id: 'fullstack-web-architecture',
      icon: 'database',
      title: 'Full-Stack Web Starter Suites',
      deck: 'Clean Nuxt 3 & Vue 3 production-grade boilerplates engineered for speed, conversion, and instant deployment.',
      features: [
        'Lighthouse 95+ performance scores out of the box',
        'Semantic HTML5 structure and automated meta tag injection',
        'Integrated Lemon Squeezy checkout & webhook fulfillment listeners',
        'Responsive, modern white-themed CSS architecture'
      ],
      tags: ['Nuxt 3', 'Vue 3', 'TypeScript', 'Lemon Squeezy API']
    }
  ],
  pricing: [
    {
      id: 'single-tool',
      name: 'Single SEO Utility License',
      price: '$5 – $19',
      billing: 'one-time purchase per utility',
      description: 'Choose any individual Python script or webmaster tool from our catalog with full commented source code.',
      popular: false,
      deliverables: [
        '1 Selected SEO or Webmaster Python utility codebase',
        'Instant downloadable ZIP & GitHub repository access',
        'Detailed documentation, usage examples & CLI guides',
        'Clean, commented, zero-dependency source code',
        '100% Perpetual commercial-use software license'
      ],
      cta: 'Explore Catalog Tools'
    },
    {
      id: 'all-in-one-toolkit',
      name: 'All-in-One SEO & Webmaster Suite',
      price: '$89',
      billing: 'one-time digital purchase',
      description: 'The complete bundle of all 15 SEO automation tools, title generators, schema builders, and site administration utilities.',
      popular: true,
      deliverables: [
        'All 15 Specialized SEO & Webmaster automation tools',
        'Unified CLI dashboard to run all tools from a single terminal',
        'Bulk CSV & JSON processing pipelines for large catalogs',
        'Docker container environment for automated 24/7 execution',
        '14 Days priority technical support & setup assistance',
        '100% Perpetual commercial-use software license'
      ],
      cta: 'Get Complete 15-Tool Suite'
    },
    {
      id: 'pro-web-suite',
      name: 'Pro Web Platform & SEO Suite',
      price: '$249',
      billing: 'one-time digital purchase',
      description: 'Full modern web application codebase (Nuxt 3) integrated with our entire SEO optimization engine & Lemon Squeezy checkout.',
      popular: false,
      deliverables: [
        'Complete Nuxt 3 / Vue 3 web platform codebase',
        'Integrated SEO automation engine & metadata injectors',
        'Pre-configured Lemon Squeezy payment & webhook workers',
        'Interactive client-side tools and admin dashboard',
        '30 Days dedicated technical support & deployment guide',
        '100% Perpetual commercial-use software license'
      ],
      cta: 'Get Full Platform Suite'
    }
  ],
  faqs: [
    {
      question: 'What do I receive upon purchasing a tool or suite?',
      answer: 'Upon completing your purchase through Lemon Squeezy, you receive immediate digital delivery: direct invitation/access to the private GitHub repository, a downloadable ZIP package containing the full commented source code, complete technical documentation, and CLI usage examples.'
    },
    {
      question: 'Are these tools compliant with search engine guidelines?',
      answer: 'Yes, 100%. Our tools are strictly white-hat webmaster utilities: they generate compliant Schema.org JSON-LD, format titles and meta descriptions according to Google SERP guidelines, organize paragraph readability, and validate sitemaps. They do not harvest private data, bypass authentication, or violate platform terms of service.'
    },
    {
      question: 'Do I get full commercial ownership of the source code?',
      answer: 'Yes, 100%. All tools and suites include a perpetual, non-exclusive, worldwide commercial license. You have the complete freedom to run, modify, customize, and integrate the tools into your commercial websites and client projects with zero recurring royalties.'
    },
    {
      question: 'How are the digital tools delivered and updated?',
      answer: 'Delivery is handled electronically right after checkout. You will receive an onboarding confirmation email with your repository access and direct download links. If a package receives maintenance patches or dependency updates during your support window, you will receive them directly through Git.'
    },
    {
      question: 'How do payment and checkout work?',
      answer: 'We accept payments securely through our authorized Merchant of Record partner, Lemon Squeezy. You can pay using major credit and debit cards, Apple Pay, Google Pay, or PayPal. Official tax invoices, VAT receipts, and product license keys are generated automatically upon purchase.'
    },
    {
      question: 'What is your refund policy if a script has an issue?',
      answer: 'Every software tool is backed by our technical quality guarantee. If any bug or technical defect is identified in our codebase that cannot be resolved, a refund will be issued promptly through Lemon Squeezy in accordance with our Refund Policy.'
    }
  ]
}
