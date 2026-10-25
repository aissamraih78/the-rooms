export const site = {
  name: 'SyntaxCraft',
  brand: 'SyntaxCraft Studio',
  tagline: 'High-Performance Web Engineering & Autonomous Python Automation',
  description: 'We engineer custom full-stack web applications, autonomous workflow automations, and public SEO analytics pipelines for growing digital businesses, founders, and creators.',
  email: 'contact@syntaxcraft.dev',
  domain: 'https://syntaxcraft.dev',
  github: 'https://github.com/syntaxcraft2026',
  location: 'Douar Ait Ouaarab, Ghassate, Ouarzazate 45000, Morocco',
  city: 'Ouarzazate, Morocco',
  availability: 'Available for New Projects',
  responseSla: 'Guaranteed response within 12 hours',
  stats: [
    { label: 'Web Applications & Automations Built', value: '120+' },
    { label: 'Average Project Delivery', value: '48h - 5d' },
    { label: 'System Uptime Reliability', value: '99.9%' },
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
      deck: 'Eliminate repetitive manual operations with robust, scheduled autonomous background scripts.',
      features: [
        'Automated file transformation, reporting, and accounting data exports',
        'Cron schedulers and daemonized background worker processes',
        'Asynchronous task queues and event-driven data processors',
        'Telegram, Discord, and Slack automated operational bots'
      ],
      tags: ['Python 3.12', 'AsyncIO', 'FastAPI', 'Celery', 'Docker']
    },
    {
      id: 'market-analytics',
      icon: 'database',
      title: 'Public SEO & Market Analytics Pipelines',
      deck: 'Automated monitoring strictly limited to public SEO metrics, search trend indicators, and website performance.',
      features: [
        'Public search engine keyword ranking & search volume metrics',
        'Google Trends and macro market demand indicators',
        'Core Web Vitals & website performance benchmarking',
        'Automated scheduled reporting via email or webhook notifications'
      ],
      tags: ['SEO Analytics', 'Public APIs', 'Google Trends', 'Core Web Vitals', 'Python 3.12']
    },
    {
      id: 'web-engineering',
      icon: 'code',
      title: 'Custom Modern Web Development',
      deck: 'Blazing-fast, responsive web applications and landing pages engineered to convert.',
      features: [
        'Full-stack applications using Nuxt 3, Vue 3, and Node.js',
        'Mobile-first, conversion-optimized landing pages and design systems',
        'Lighthouse 95+ performance scores and clean semantic SEO structure',
        'Integrated analytics, lead capture forms, and dynamic interactions'
      ],
      tags: ['Nuxt 3', 'Vue 3', 'TypeScript', 'Node.js', 'Vanilla CSS']
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
        '1 Custom Python automation script or public SEO analytics pipeline',
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
        'Full modern web application / landing page OR multi-step workflow automation',
        'Automated database integration (SQLite / PostgreSQL / CSV)',
        'Robust error handling, structured logging & failure alerts',
        'Automated background worker or public data pipeline',
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
        'High-throughput asynchronous data processing & background workers',
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
      answer: 'Standard automation scripts and pipelines are typically delivered within 48 to 72 hours. Comprehensive web applications and multi-step architectures are delivered within 3 to 7 business days, depending on project scope.'
    },
    {
      question: 'What public analytics and data types do you support?',
      answer: 'We exclusively engineer pipelines for non-confidential public metrics: public search engine keyword rankings, Google Trends macro indicators, and website performance benchmarks (Core Web Vitals). We do not scrape personal data (PII) or bypass private authentication.'
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
