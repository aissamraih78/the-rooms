<script setup lang="ts">
import { site } from '~/data/site'

useHead({
  title: 'Terms of Service & Licensing — SyntaxCraft Studio',
  meta: [
    { name: 'description', content: 'Terms and Conditions of software licensing for SyntaxCraft Studio digital products, web codebases, and Python automation packages.' }
  ]
})
</script>

<template>
  <div class="container" style="padding: 60px 0 100px; max-width: 860px;">
    <NuxtLink to="/" class="btn btn-secondary btn-sm" style="margin-bottom: 30px;">
      &larr; Back to Home
    </NuxtLink>

    <div class="badge" style="margin-bottom: 16px;">Legal Documentation</div>
    <h1 style="font-size: 2.8rem; margin-bottom: 12px;">Terms of Service & Software License</h1>
    <p style="color: var(--text-muted); margin-bottom: 40px;">Last updated: October 25, 2026</p>

    <div style="display: grid; gap: 32px; font-size: 0.96rem; line-height: 1.75; color: var(--text-secondary);">
      <section>
        <h2 style="font-size: 1.4rem; color: var(--text-primary); margin-bottom: 12px;">1. Overview & Product Scope</h2>
        <p>
          SyntaxCraft Studio ("SyntaxCraft", "we", "us", or "our") develops and licenses pre-engineered digital software packages, production-grade Python automation scripts, Nuxt 3 web application codebases, and developer tooling modules. By purchasing a software license, accessing our private repositories, or downloading our codebase packages, you ("Licensee", "Customer", or "You") agree to be bound by these Terms of Service.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: var(--text-primary); margin-bottom: 12px;">2. Commercial License Grant & Code Ownership</h2>
        <p>
          Upon successful payment processing via our Merchant of Record partner, Lemon Squeezy, SyntaxCraft grants you a perpetual, worldwide, non-exclusive, irrevocable commercial license to:
        </p>
        <ul style="margin: 12px 0 0 20px; display: grid; gap: 8px;">
          <li>Use, run, inspect, and modify the source code for unlimited internal or commercial client projects.</li>
          <li>Deploy, host, and integrate the codebase within your own infrastructure or customer solutions.</li>
          <li>Incorporate the code into derivative proprietary SaaS platforms, workflows, or automated microservices without paying recurring royalties.</li>
        </ul>
        <p style="margin-top: 12px;">
          <em>Restrictions:</em> You may not redistribute, resell, or publicly publish the raw source code repositories or templates as standalone competing digital assets without adding substantial derivative value.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: var(--text-primary); margin-bottom: 12px;">3. Instant Electronic Delivery & Repository Access</h2>
        <p>
          All digital products and codebases are delivered electronically immediately following checkout confirmation:
        </p>
        <ul style="margin: 12px 0 0 20px; display: grid; gap: 8px;">
          <li>Direct automated invitation and read/clone access to the private GitHub repository containing the complete source tree.</li>
          <li>Downloadable compressed archive (.zip) containing full source code, environment Dockerfiles, and dependencies.</li>
          <li>Complete technical documentation, installation instructions, and quickstart runbooks.</li>
        </ul>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: var(--text-primary); margin-bottom: 12px;">4. Public Data Compliance & Ethical Software Standards</h2>
        <p>
          SyntaxCraft Studio software packages are engineered in strict compliance with international digital ethics, robots.txt directives, and public API provider terms. Where automation modules interact with online data, their scope is strictly confined to non-confidential, publicly accessible metrics:
        </p>
        <ul style="margin: 12px 0 0 20px; display: grid; gap: 8px;">
          <li><strong>Public SEO & Keyword Metrics:</strong> Search engine result page rankings, public indexation frequency, and aggregated keyword visibility.</li>
          <li><strong>Market & Search Trends:</strong> Google Trends search interest indicators and public macro market volume estimates.</li>
          <li><strong>Website Performance Benchmarking:</strong> Public Core Web Vitals, page speed metrics, and SSL/uptime response indicators.</li>
        </ul>
        <p style="margin-top: 12px;">
          <strong>Zero-Tolerance Compliance Statement:</strong> Our software packages do not collect, process, or harvest personal identifiable information (PII), bypass authentication firewalls, harvest credentials, or facilitate unauthorized access to private systems. All software must be utilized in accordance with applicable laws and API agreements.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: var(--text-primary); margin-bottom: 12px;">5. Payment Processing via Merchant of Record</h2>
        <p>
          All electronic billing, checkout processes, and transaction handling are facilitated securely through our authorized Merchant of Record partner, <strong>Lemon Squeezy</strong>. Lemon Squeezy handles global sales taxes, VAT, and PCI-compliant payment gateways. Major credit/debit cards, Apple Pay, Google Pay, and PayPal are accepted. Official VAT/GST receipts are issued automatically.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: var(--text-primary); margin-bottom: 12px;">6. Technical Support & Warranty</h2>
        <p>
          Each package includes a dedicated technical defect warranty and support window (7 to 30 days depending on the tier). While we guarantee the software operates as documented at the time of delivery, SyntaxCraft Studio is not liable for future breaking changes introduced by third-party external APIs, platform deprecations, or unauthorized end-user modifications.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: var(--text-primary); margin-bottom: 12px;">7. Studio Entity & Contact</h2>
        <p>
          For licensing inquiries, enterprise custom licenses, or support, please contact our team directly at:
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
