<script setup lang="ts">
import { site } from '~/data/site'

useHead({
  title: 'Privacy Policy — SyntaxCraft Studio',
  meta: [
    { name: 'description', content: 'Privacy Policy for SyntaxCraft Studio. Learn how we handle your personal data, respect confidentiality, and maintain zero data harvesting standards.' }
  ]
})
</script>

<template>
  <div class="container" style="padding: 60px 0 100px; max-width: 860px;">
    <NuxtLink to="/" class="btn btn-secondary btn-sm" style="margin-bottom: 30px;">
      &larr; Back to Home
    </NuxtLink>

    <div class="badge" style="margin-bottom: 16px;">Data Protection & Ethics</div>
    <h1 style="font-size: 2.8rem; margin-bottom: 12px;">Privacy Policy</h1>
    <p style="color: var(--text-muted); margin-bottom: 40px;">Effective Date: October 25, 2026</p>

    <div style="display: grid; gap: 32px; font-size: 0.96rem; line-height: 1.75; color: #cbd5e1;">
      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">1. Information We Collect</h2>
        <p>
          We only collect data that is strictly required to communicate with you and complete your bespoke software development projects:
        </p>
        <ul style="margin: 12px 0 0 20px; display: grid; gap: 6px;">
          <li>Contact details: Name, business email address, company or project title.</li>
          <li>Project specifications: Technical briefs, scope descriptions, and API documentation provided directly by you.</li>
          <li>Transactional records: Invoice receipts, purchase identifiers, and tier subscriptions provided via our payment partner.</li>
        </ul>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">2. Zero Personal Data Harvesting Guarantee</h2>
        <p>
          SyntaxCraft Studio operates strictly as an engineering and software architecture studio. We do not harvest, store, scrape, sell, or broker consumer personal data (PII), email lists, or private user credentials. Any automated analytics or monitoring tools engineered for clients operate exclusively on public, authorized APIs and non-confidential metrics (such as public search rankings, Google Trends, and Core Web Vitals).
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">3. Payment Information Security</h2>
        <p>
          SyntaxCraft Studio does not store, process, or transmit your credit card or sensitive financial information on our servers. All transaction billing is managed by <strong>Lemon Squeezy</strong> acting as Merchant of Record under PCI-DSS Level 1 compliance.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">4. Confidentiality & Non-Disclosure</h2>
        <p>
          We treat all proprietary algorithms, client business logic, database credentials, and business concepts shared with us under strict confidentiality. We do not resell, open-source, or distribute your custom codebase without your explicit written authorization.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">5. Cookies & Tracking</h2>
        <p>
          Our website uses minimal, privacy-focused technical cookies essential for session persistence and security. We do not use intrusive cross-site tracking beacons or sell marketing profiles to third parties.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">6. Contacting Data Protection</h2>
        <p>
          If you have questions regarding data retention, or would like to request deletion of your project records, please contact our privacy desk at:
          <br>
          <strong style="color: var(--accent-cyan);">Office:</strong> {{ site.location }}
          <br>
          <strong style="color: var(--accent-cyan);">Email:</strong> {{ site.email }}
        </p>
      </section>
    </div>
  </div>
</template>
