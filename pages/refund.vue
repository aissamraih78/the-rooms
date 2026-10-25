<script setup lang="ts">
import { site } from '~/data/site'

useHead({
  title: 'Refund & Revision Policy — SyntaxCraft Studio',
  meta: [
    { name: 'description', content: 'Our 100% satisfaction guarantee, revision windows, and refund policy for bespoke software engineering and Python automation.' }
  ]
})
</script>

<template>
  <div class="container" style="padding: 60px 0 100px; max-width: 860px;">
    <NuxtLink to="/" class="btn btn-secondary btn-sm" style="margin-bottom: 30px;">
      &larr; Back to Home
    </NuxtLink>

    <div class="badge" style="margin-bottom: 16px;">Quality Guarantee</div>
    <h1 style="font-size: 2.8rem; margin-bottom: 12px;">Refund & Revision Policy</h1>
    <p style="color: var(--text-muted); margin-bottom: 40px;">Effective Date: October 25, 2026</p>

    <div style="display: grid; gap: 32px; font-size: 0.96rem; line-height: 1.75; color: #cbd5e1;">
      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">1. Engineering Satisfaction Commitment</h2>
        <p>
          At SyntaxCraft Studio, our core priority is delivering functional, robust, and clean code that meets the agreed technical criteria. Because custom software engineering involves tailored manual labor and intellectual property creation, our refund and revision model is designed to protect both the client's investment and the engineering lifecycle.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">2. Complimentary Revision Windows</h2>
        <p>
          Every package includes an active post-delivery testing and revision period:
        </p>
        <ul style="margin: 12px 0 0 20px; display: grid; gap: 6px;">
          <li><strong>Starter Script ($149):</strong> 7 days of complimentary bug-fix support and environment adjustments.</li>
          <li><strong>Pro Automation & Web ($449):</strong> 14 days of dedicated revision, scope alignment, and logic tuning.</li>
          <li><strong>Enterprise Architecture ($1,199):</strong> 30 days of priority maintenance, monitoring, and patch releases.</li>
        </ul>
        <p style="margin-top: 12px;">
          During this window, any defects, deviations from the agreed brief, or operational errors in the delivered codebase will be diagnosed and fixed at no extra charge.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">3. Cancellation Before Work Begins</h2>
        <p>
          If you order a service package and request cancellation before our engineering team has commenced architecture or code writing (within 24 hours of ordering), you are entitled to a full 100% refund processed via Lemon Squeezy back to your original payment method.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">4. Inability to Fulfill Scope</h2>
        <p>
          In the rare circumstance that an external target platform renders an automation or web project technically impossible (e.g. unbypassable hardware restrictions or sudden API decommissioning), and no viable workaround can be engineered, we will issue a full or prorated refund promptly.
        </p>
      </section>

      <section>
        <h2 style="font-size: 1.4rem; color: #ffffff; margin-bottom: 12px;">5. How to Request Support or Revisions</h2>
        <p>
          To initiate a revision request or discuss your project status, email our engineering lead at:
          <br>
          <strong style="color: var(--accent-cyan);">Email:</strong> {{ site.email }}
          <br>
          Please include your order identifier or project name for immediate expedited assistance.
        </p>
      </section>
    </div>
  </div>
</template>
