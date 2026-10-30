<script setup lang="ts">
import { site } from '~/data/site'

useHead({
  title: 'Refund & Warranty Policy — SyntaxCraft Studio',
  meta: [
    { name: 'description', content: 'Our satisfaction guarantee, technical defect warranty, and refund policy for digital software packages and automation codebases.' }
  ]
})
</script>

<template>
  <div class="container" style="padding: 60px 0 100px; max-width: 860px;">
    <NuxtLink to="/" class="btn btn-secondary btn-sm" style="margin-bottom: 30px;">
      &larr; Back to Home
    </NuxtLink>

    <div class="badge" style="margin-bottom: 16px;">Quality Guarantee</div>
    <h1 style="font-size: 2.8rem; margin-bottom: 12px;">Refund & Warranty Policy</h1>
    <p style="color: var(--text-muted); margin-bottom: 40px;">Effective Date: October 25, 2026</p>

    <div style="display: grid; gap: 32px; font-size: 0.96rem; line-height: 1.75; color: var(--text-secondary);">
      <section>
        <h2 style="font-size: 1.4rem; color: var(--text-primary); margin-bottom: 12px;">1. Digital Software Quality Commitment</h2>
        <p>
          At SyntaxCraft Studio, our core priority is delivering production-ready, clean, and fully functional digital codebases, automation packages, and web starter architectures. Because our products are delivered electronically as downloadable digital source code, repository access, and technical documentation, our refund and warranty policy is structured to guarantee technical reliability while complying with global digital goods standards.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: var(--text-primary); margin-bottom: 12px;">2. Complimentary Technical Support & Defect Warranty</h2>
        <p>
          Every software package includes dedicated technical onboarding and defect warranty support from the date of purchase:
        </p>
        <ul style="margin: 12px 0 0 20px; display: grid; gap: 6px;">
          <li><strong>Script Starter Package ($149):</strong> 7 days of complimentary setup assistance, environment adjustments, and bug fixes.</li>
          <li><strong>Pro Automation & Web Suite ($449):</strong> 14 days of dedicated technical support, dependency alignment, and defect resolution.</li>
          <li><strong>Enterprise Architecture Package ($1,199):</strong> 30 days of priority technical onboarding, monitoring guidance, and patch releases.</li>
        </ul>
        <p style="margin-top: 12px;">
          During this active window, any bugs, execution defects, or deviations from the stated product documentation will be diagnosed, resolved, or updated at zero extra charge.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: var(--text-primary); margin-bottom: 12px;">3. Refund Eligibility for Digital Goods</h2>
        <p>
          We stand firmly behind the technical quality of our codebase packages. You are eligible for a 100% refund processed through our Merchant of Record partner, Lemon Squeezy, under the following circumstances:
        </p>
        <ul style="margin: 12px 0 0 20px; display: grid; gap: 8px;">
          <li><strong>Unresolvable Technical Defect:</strong> If the delivered codebase exhibits a critical functional error or incompatibility with the documented operating environment, and our engineering team cannot resolve it within 3 business days of notification.</li>
          <li><strong>Duplicate Purchase:</strong> If you accidentally place a duplicate order for the same digital software package.</li>
          <li><strong>Non-Delivery:</strong> In the rare event that electronic access or repository invitation is not provided within 24 hours of successful payment confirmation.</li>
        </ul>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">4. Processing of Refunds via Lemon Squeezy</h2>
        <p>
          Approved refunds are submitted directly through the <strong>Lemon Squeezy</strong> merchant portal and credited back to your original payment method (Credit/Debit Card, Apple Pay, Google Pay, or PayPal). Standard bank processing times typically range between 3 to 7 business days.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">5. How to Initiate a Support Request or Refund</h2>
        <p>
          To request technical assistance, report a codebase bug, or inquire about a refund, simply email our support desk:
          <br>
          <strong style="color: var(--accent-cyan);">Email:</strong> {{ site.email }}
          <br>
          Please include your Lemon Squeezy Order ID and license details for immediate assistance.
        </p>
      </section>
    </div>
  </div>
</template>
