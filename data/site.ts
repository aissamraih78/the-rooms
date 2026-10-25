export const site = {
  name: 'SyntaxCraft',
  brand: 'SyntaxCraft Studio',
  tagline: 'High-Performance Web Engineering & Autonomous Python Automation',
  description: 'We engineer custom web applications, resilient data scraping pipelines, and 24/7 workflow automations for growing digital businesses, SaaS founders, and creators.',
  email: 'contact@syntaxcraft.dev',
  domain: 'https://syntaxcraft.dev',
  availability: 'Available for New Projects',
  responseSla: 'Guaranteed response within 12 hours',
  stats: [
    { label: 'Automations & Scripts Built', value: '120+' },
    { label: 'Average Project Delivery', value: '48h - 5d' },
    { label: 'Pipeline Uptime Reliability', value: '99.9%' },
    { label: 'Client Code Ownership', value: '100%' }
  ],
  nav: [
    { label: 'Services', href: '/#services' },
    { label: 'Automation Lab', href: '/#automation' },
    { label: 'Pricing', href: '/#pricing' },
    { label: 'Process', href: '/#process' },
    { label: 'FAQ', href: '/#faq' },
    { label: 'Contact', href: '/contact' }
  ],
  services: [
    {
      id: 'python-automation',
      icon: 'terminal',
      title: 'Python Workflow & Task Automation',
      deck: 'Eliminate repetitive manual tasks with robust, scheduled autonomous background scripts.',
      features: [
        'Headless browser automation (Playwright & Selenium)',
        'Automated file transformation, reporting, and ETL data pipelines',
        'Cron schedulers and daemonized background worker processes',
        'Telegram, Discord, and Slack automated event bots'
      ],
      tags: ['Python 3.12', 'Playwright', 'AsyncIO', 'Celery', 'Docker']
    },
    {
      id: 'web-scraping',
      icon: 'database',
      title: 'Resilient Web Scraping & Data Pipelines',
      deck: 'Extract clean, structured data from complex dynamic websites at scale without getting blocked.',
      features: [
        'Smart anti-bot evasion & stealth browser fingerprinting',
        'Rotating proxy pools, session managers & captcha handling',
        'Direct export to JSON, CSV, PostgreSQL, or SQLite databases',
        'Real-time change monitoring and automatic email/webhook alerts'
      ],
      tags: ['Scrapy', 'BeautifulSoup', 'Proxy Rotation', 'FastAPI', 'PostgreSQL']
    },
    {
      id: 'web-engineering',
      icon: 'code',
      title: 'Custom Modern Web Development',
      deck: 'Blazing-fast, responsive web applications and landing pages engineered to convert.',
      features: [
        'Full-stack applications using Nuxt, Vue 3, Next.js, and Node.js',
        'Mobile-first, conversion-optimized landing pages and design systems',
        'Lighthouse 95+ performance scores and clean semantic SEO structure',
        'Integrated analytics, lead capture forms, and dynamic interactions'
      ],
      tags: ['Nuxt 3', 'Vue 3', 'TypeScript', 'Node.js', 'Tailwind CSS']
    },
    {
      id: 'api-integrations',
      icon: 'cpu',
      title: 'API Integrations & Payment Gateways',
      deck: 'Seamlessly connect third-party platforms, webhooks, and payment checkouts into your systems.',
      features: [
        'Lemon Squeezy & Stripe payment checkout flows and webhook listeners',
        'RESTful & GraphQL custom microservice development',
        'CRM, email marketing, and third-party SaaS API connectors',
        'Secure API token management and OAuth2 authentication flows'
      ],
      tags: ['Lemon Squeezy API', 'Stripe', 'REST APIs', 'Webhooks', 'OAuth2']
    }
  ],
  pricing: [
    {
      id: 'starter',
      name: 'Script Starter',
      price: '$149',
      billing: 'one-time investment',
      description: 'Ideal for small-to-medium tasks, single-purpose automation scripts, or specific API integrations.',
      popular: false,
      deliverables: [
        '1 Custom Python automation script or web scraper',
        'Complete setup guide and environment documentation',
        'Clean, commented, and typed Python source code',
        '48-Hour Rapid Delivery guarantee',
        '7 Days post-delivery bug-fix support',
        '100% Full commercial copyright transfer'
      ],
      cta: 'Order Starter Script'
    },
    {
      id: 'pro',
      name: 'Pro Automation & Web',
      price: '$449',
      billing: 'one-time investment',
      description: 'Our most popular tier: comprehensive workflow automation or a full-featured high-converting web landing page.',
      popular: true,
      deliverables: [
        'Full modern web application / landing page OR multi-step automation pipeline',
        'Automated database integration (SQLite / PostgreSQL / CSV)',
        'Robust error handling, structured logging & failure alerts',
        'Rotating proxy setup or headless browser workflow',
        '3 to 5 Business days delivery',
        '14 Days dedicated revision & support period',
        '100% Full commercial copyright transfer'
      ],
      cta: 'Order Pro Package'
    },
    {
      id: 'enterprise',
      name: 'Enterprise Architecture',
      price: '$1,199',
      billing: 'one-time investment',
      description: 'Comprehensive end-to-end full-stack web system, high-volume automated data pipelines, or complex custom SaaS tooling.',
      popular: false,
      deliverables: [
        'Complete full-stack system (Frontend + Backend + Database)',
        'High-scale scraping engine or multi-threaded background workers',
        'Custom administrative controls & webhook notification system',
        'Server deployment, Docker containerization & SSL setup',
        '7 to 10 Business days turnaround',
        '30 Days priority maintenance & direct support line',
        '100% Full commercial copyright transfer'
      ],
      cta: 'Request Enterprise System'
    }
  ],
  faqs: [
    {
      question: 'Do I get full ownership of the source code?',
      answer: 'Yes, 100%. Upon completion and delivery, you receive full commercial intellectual property (IP) rights and source code custody. There are no vendor lock-ins or recurring licensing fees for our custom code.'
    },
    {
      question: 'What is the typical turnaround time for a project?',
      answer: 'Standard automation scripts and scrapers are typically delivered within 48 to 72 hours. Comprehensive web applications and multi-step pipelines are delivered within 3 to 7 business days, depending on project scope.'
    },
    {
      question: 'How do you handle revisions and quality assurance?',
      answer: 'Every project goes through rigorous unit and integration testing before delivery. We include a dedicated revision period (from 7 to 30 days depending on the selected package) to guarantee the software operates flawlessly in your environment.'
    },
    {
      question: 'How do payment and checkout work?',
      answer: 'We accept payments securely through our authorized Merchant of Record partner, Lemon Squeezy. You can pay using major credit and debit cards, Apple Pay, Google Pay, or PayPal. Invoices and VAT receipts are generated automatically upon purchase.'
    },
    {
      question: 'Can you maintain or scale the system after delivery?',
      answer: 'Absolutely. We offer ongoing maintenance retainers, cloud deployment support, and feature expansion packages tailored to your growing operational needs.'
    }
  ]
}
