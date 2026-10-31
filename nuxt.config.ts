export default defineNuxtConfig({
  compatibilityDate: '2026-08-01',
  ssr: true,
  modules: ['@nuxt/eslint'],
  devtools: { enabled: false },
  nitro: {
    prerender: {
      crawlLinks: false,
      routes: [
        '/',
        '/terms',
        '/privacy',
        '/refund',
        '/contact',
        '/listings',
      ],
    },
  },
  css: [
    '~/assets/styles/main.css',
  ],
  app: {
    head: {
      htmlAttrs: { lang: 'en' },
      title: 'SyntaxCraft — Production-Grade SEO Automation Tools & Webmaster Utilities',
      meta: [
        { name: 'viewport', content: 'width=device-width, initial-scale=1, maximum-scale=5' },
        {
          name: 'description',
          content: 'Specialized 100% compliant SEO automation scripts, product title generators, metadata synthesizers, and webmaster administration utilities.',
        },
        { name: 'theme-color', content: '#f8fafc' },
        { property: 'og:title', content: 'SyntaxCraft — Production-Grade SEO Automation Tools & Webmaster Utilities' },
        { property: 'og:description', content: 'Specialized 100% compliant SEO automation scripts, product title generators, metadata synthesizers, and webmaster utilities.' },
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
