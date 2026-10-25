export default defineNuxtConfig({
  compatibilityDate: '2026-08-01',
  ssr: true,
  modules: ['@nuxt/eslint'],
  devtools: { enabled: false },
  nitro: {
    prerender: {
      routes: [
        '/',
        '/terms',
        '/privacy',
        '/refund',
        '/contact',
      ],
    },
  },
  css: [
    '~/assets/styles/main.css',
  ],
  app: {
    head: {
      htmlAttrs: { lang: 'en' },
      title: 'SyntaxCraft — High-Performance Web & Python Automation Studio',
      meta: [
        { name: 'viewport', content: 'width=device-width, initial-scale=1, maximum-scale=5' },
        {
          name: 'description',
          content: 'Engineering custom web applications, workflow automations, and resilient data scraping pipelines for growing digital businesses and ambitious creators.',
        },
        { name: 'theme-color', content: '#070b12' },
        { property: 'og:title', content: 'SyntaxCraft — High-Performance Web & Python Automation Studio' },
        { property: 'og:description', content: 'Engineering custom web applications, workflow automations, and resilient data scraping pipelines.' },
        { property: 'og:type', content: 'website' },
        { property: 'og:url', content: 'https://syntaxcraft.dev' },
      ],
      link: [
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap' },
        { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }
      ]
    },
  },
})
