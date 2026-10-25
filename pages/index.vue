<script setup lang="ts">
import { site } from '~/data/site'

useHead({
  title: 'SyntaxCraft — High-Performance Web & Python Automation Studio',
  meta: [
    {
      name: 'description',
      content: 'Engineering custom web applications, workflow automations, and robust public data pipelines for growing digital businesses.'
    }
  ]
})
</script>

<template>
  <div>
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="container">
        <div class="hero-grid">
          <div>
            <div class="badge">
              <span class="badge-dot"></span>
              Autonomous Python Systems & Modern Web Studio
            </div>

            <h1 class="hero-title">
              We Craft Resilient <span class="gradient-cyan-indigo">Web Applications</span> & High-Speed <span class="gradient-text">Python Automation</span>
            </h1>

            <p class="hero-subtitle">
              From bespoke full-stack applications and high-converting landing pages to intelligent bots, public data pipelines, and 24/7 background workflows. Built for stability, engineered for speed.
            </p>

            <div class="hero-actions">
              <NuxtLink to="/#pricing" class="btn btn-primary">
                Explore Packages & Pricing
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
              </NuxtLink>
              <NuxtLink to="/contact" class="btn btn-secondary">
                Request Custom Consultation
              </NuxtLink>
            </div>
          </div>

          <div>
            <TerminalShowcase />
          </div>
        </div>

        <!-- Stats Bar -->
        <div class="stats-bar">
          <div v-for="stat in site.stats" :key="stat.label" class="stat-item">
            <div class="stat-val stat-val-highlight">{{ stat.value }}</div>
            <div class="stat-label">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="section-shell">
      <div class="container">
        <div class="section-head">
          <div class="badge">Core Competencies</div>
          <h2>Engineered Solutions for Modern Digital Operations</h2>
          <p>
            Whether you need to extract critical market intelligence, automate complex multi-platform processes, or deploy high-converting web applications, we build production-grade software you can rely on.
          </p>
        </div>

        <div class="services-grid">
          <div v-for="svc in site.services" :key="svc.id" class="service-card">
            <div class="service-icon-wrap">
              <svg v-if="svc.icon === 'terminal'" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" x2="20" y1="19" y2="19"/></svg>
              <svg v-else-if="svc.icon === 'database'" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/></svg>
              <svg v-else-if="svc.icon === 'code'" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
              <svg v-else xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/></svg>
            </div>

            <h3>{{ svc.title }}</h3>
            <p class="service-deck">{{ svc.deck }}</p>

            <ul class="service-features">
              <li v-for="feat in svc.features" :key="feat">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
                <span>{{ feat }}</span>
              </li>
            </ul>

            <div class="tags-wrap">
              <span v-for="tag in svc.tags" :key="tag" class="tag-pill">{{ tag }}</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Pricing Section -->
    <section id="pricing" class="section-shell" style="background: rgba(12, 18, 30, 0.5); border-block: 1px solid var(--border-subtle);">
      <div class="container">
        <div class="section-head">
          <div class="badge">Transparent Investment</div>
          <h2>Flat-Fee Pricing with Zero Hidden Costs</h2>
          <p>
            Choose the package that aligns with your technical requirements. Every project includes full commented source code, dedicated post-delivery support, and 100% intellectual property transfer.
          </p>
        </div>

        <div class="pricing-grid">
          <div
            v-for="pkg in site.pricing"
            :key="pkg.id"
            class="pricing-card"
            :class="{ featured: pkg.popular }"
          >
            <div v-if="pkg.popular" class="popular-ribbon">Most Popular Choice</div>

            <div class="price-header">
              <h3>{{ pkg.name }}</h3>
              <p class="price-desc">{{ pkg.description }}</p>
            </div>

            <div class="price-amount-box">
              <span class="price-val">{{ pkg.price }}</span>
              <span class="price-billing">{{ pkg.billing }}</span>
            </div>

            <ul class="deliverables-list">
              <li v-for="item in pkg.deliverables" :key="item">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
                <span>{{ item }}</span>
              </li>
            </ul>

            <NuxtLink
              :to="'/contact?package=' + pkg.id"
              class="btn"
              :class="pkg.popular ? 'btn-primary' : 'btn-secondary'"
              style="width: 100%;"
            >
              {{ pkg.cta }}
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>

    <!-- Process Section -->
    <section id="process" class="section-shell">
      <div class="container">
        <div class="section-head">
          <div class="badge">Delivery Lifecycle</div>
          <h2>Predictable, Transparent Engineering Process</h2>
          <p>
            We adhere to disciplined software development practices to ensure your scripts and applications deploy on schedule without regressions.
          </p>
        </div>

        <div class="process-steps">
          <div class="step-card">
            <div class="step-num">STAGE 01</div>
            <h3>Architecture & Scope</h3>
            <p>We review your exact input datasets, target platforms, or design specifications and establish concrete deliverable milestones.</p>
          </div>

          <div class="step-card">
            <div class="step-num">STAGE 02</div>
            <h3>Agile Engineering</h3>
            <p>We write clean, typed, modular code with integrated error handling, anti-block proxies, or responsive CSS design tokens.</p>
          </div>

          <div class="step-card">
            <div class="step-num">STAGE 03</div>
            <h3>Stress Testing</h3>
            <p>Every script and component is validated against real network constraints, edge-case payloads, and concurrency limits.</p>
          </div>

          <div class="step-card">
            <div class="step-num">STAGE 04</div>
            <h3>Handover & Support</h3>
            <p>We deliver the complete private GitHub repository, setup documentation, and stay on standby during your revision window.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section id="faq" class="section-shell" style="border-top: 1px solid var(--border-subtle);">
      <div class="container">
        <div class="section-head">
          <div class="badge">Got Questions?</div>
          <h2>Frequently Asked Questions</h2>
          <p>Everything you need to know about our development lifecycle, intellectual property, and billing.</p>
        </div>

        <div class="faq-wrap">
          <details v-for="faq in site.faqs" :key="faq.question" class="faq-item">
            <summary class="faq-summary">
              <span>{{ faq.question }}</span>
              <svg class="faq-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
            </summary>
            <div class="faq-content">
              {{ faq.answer }}
            </div>
          </details>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="section-shell">
      <div class="container">
        <div class="cta-banner">
          <h2>Ready to Automate Your Operations or Build Your Next Web Project?</h2>
          <p>
            Get in touch with our team today. We typically evaluate technical specifications and provide quotes within 12 hours.
          </p>
          <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
            <NuxtLink to="/contact" class="btn btn-primary">
              Contact SyntaxCraft Studio
            </NuxtLink>
            <NuxtLink to="/#pricing" class="btn btn-secondary">
              View Pricing Packages
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
