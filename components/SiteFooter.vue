<script setup lang="ts">
import { site } from '~/data/site'
const currentYear = new Date().getFullYear()
</script>

<template>
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <NuxtLink to="/" class="brand-logo" style="margin-bottom: 12px; display: inline-flex;">
            <div class="brand-icon">&lt;/&gt;</div>
            <div class="brand-name">Syntax<span class="brand-tag">Craft</span></div>
          </NuxtLink>
          <p>{{ site.description }}</p>
          <div class="badge" style="font-size: 0.72rem;">
            <span class="badge-dot"></span>
            {{ site.availability }}
          </div>
        </div>

        <div class="footer-col">
          <h4>Engineering Services</h4>
          <ul class="footer-links">
            <li><NuxtLink to="/#services">Python Task Automation</NuxtLink></li>
            <li><NuxtLink to="/#services">Web Scraping & Data Mining</NuxtLink></li>
            <li><NuxtLink to="/#services">Full-Stack Web Engineering</NuxtLink></li>
            <li><NuxtLink to="/#services">API & Webhook Integrations</NuxtLink></li>
            <li><NuxtLink to="/#pricing">Pricing & Custom Packages</NuxtLink></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Legal & Support</h4>
          <ul class="footer-links">
            <li><NuxtLink to="/terms">Terms of Service</NuxtLink></li>
            <li><NuxtLink to="/privacy">Privacy Policy</NuxtLink></li>
            <li><NuxtLink to="/refund">Refund & Revision Policy</NuxtLink></li>
            <li><NuxtLink to="/contact">Contact Support ({{ site.email }})</NuxtLink></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          &copy; {{ currentYear }} SyntaxCraft Studio (syntaxcraft.dev). All rights reserved.
        </div>
        <div style="display: flex; gap: 20px; align-items: center;">
          <span>Official Support: <a :href="'mailto:' + site.email" style="color: #38bdf8; text-decoration: underline;">{{ site.email }}</a></span>
          <span>Payments processed securely via Lemon Squeezy</span>
        </div>
      </div>
    </div>
  </footer>
</template>
