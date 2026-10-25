<script setup lang="ts">
import { site } from '~/data/site'

useHead({
  title: 'Terms of Service — SyntaxCraft Studio',
  meta: [
    { name: 'description', content: 'Terms and Conditions of service for SyntaxCraft Studio software development, web engineering, and Python automation.' }
  ]
})
</script>

<template>
  <div class="container" style="padding: 60px 0 100px; max-width: 860px;">
    <NuxtLink to="/" class="btn btn-secondary btn-sm" style="margin-bottom: 30px;">
      &larr; Back to Home
    </NuxtLink>

    <div class="badge" style="margin-bottom: 16px;">Legal Documentation</div>
    <h1 style="font-size: 2.8rem; margin-bottom: 12px;">Terms of Service</h1>
    <p style="color: var(--text-muted); margin-bottom: 40px;">Last updated: October 25, 2026</p>

    <div style="display: grid; gap: 32px; font-size: 0.96rem; line-height: 1.75; color: #cbd5e1;">
      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">1. Overview & Service Scope</h2>
        <p>
          SyntaxCraft Studio ("SyntaxCraft", "we", "us", or "our") provides bespoke software development, web engineering, API integration, and Python automation engineering services. By commissioning a service, placing an order, or utilizing our deliverables, you ("Client", "Customer", or "You") agree to be bound by these Terms of Service. Over 99% of our work consists of custom web development (Nuxt 3 / Vue / Node.js) and internal business workflow automation.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">2. Intellectual Property & Code Ownership</h2>
        <p>
          Upon full settlement of agreed project invoices or upfront package payments, all custom source code, configurations, and bespoke assets created specifically for the Client are transferred 100% to the Client. The Client receives full commercial rights, distribution rights, and modification freedom. We retain no proprietary royalty claims or recurring licensing encumbrances on bespoke client deliverables.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">3. Project Delivery & Milestones</h2>
        <p>
          Estimated delivery timelines (e.g., 48 hours for Starter scripts, 3–5 days for Pro packages) are calculated starting from the date all necessary inputs, API credentials, and project briefs are delivered by the Client. Deliverables are provided via private Git repositories, compressed tarballs, or secure direct digital transfer.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">4. Public Data Compliance & Permissible Analytics Scope</h2>
        <p>
          SyntaxCraft Studio adheres strictly to international digital ethics, robots.txt directives, and public API provider terms. Where automation involves data observation, our scope is strictly limited to non-confidential, publicly available business statistics:
        </p>
        <ul style="margin: 12px 0 0 20px; display: grid; gap: 8px;">
          <li><strong>Public SEO & Keyword Metrics:</strong> Search engine result page rankings, public indexation frequency, and aggregated keyword visibility.</li>
          <li><strong>Market & Search Trends:</strong> Google Trends search interest indicators and public macro market volume estimates.</li>
          <li><strong>Website Performance Benchmarking:</strong> Public Core Web Vitals, page speed metrics, and SSL/uptime response indicators.</li>
        </ul>
        <p style="margin-top: 12px;">
          <strong>Zero-Tolerance Compliance Statement:</strong> We strictly prohibit and refuse any projects involving personal identifiable information (PII), authentication bypass, credential harvesting, copyright-infringing digital content, or unauthorized private systems access. All delivered code must comply with governing laws and API agreements.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">5. Payment Processing via Merchant of Record</h2>
        <p>
          All electronic billing, checkout processes, and transaction handling are facilitated securely through our authorized Merchant of Record partner, <strong>Lemon Squeezy</strong>. Lemon Squeezy handles global sales taxes, VAT, and PCI-compliant payment gateways. Major credit/debit cards, Apple Pay, Google Pay, and PayPal are accepted.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">6. Limitation of Liability</h2>
        <p>
          While SyntaxCraft Studio exercises industry-standard testing and quality assurance, software is provided "as delivered." We shall not be liable for third-party platform API changes, service outages, rate limiting, or consequential business interruption arising outside our direct engineering scope.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">7. Governing Office & Contact</h2>
        <p>
          For contractual inquiries or formal correspondence, please reach our administrative office directly at:
          <br>
          <strong style="color: var(--accent-cyan);">Studio Address:</strong> {{ site.location }}
          <br>
          <strong style="color: var(--accent-cyan);">Email:</strong> {{ site.email }}
          <br>
          <strong style="color: var(--accent-cyan);">Website:</strong> {{ site.domain }}
        </p>
      </section>
    </div>
  </div>
</template>
