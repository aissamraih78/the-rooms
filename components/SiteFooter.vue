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
          <div class="badge" style="font-size: 0.72rem; margin-top: 10px;">
            <span class="badge-dot"></span>
            {{ site.availability }}
          </div>
          <div style="margin-top: 14px; font-size: 0.85rem; color: var(--text-muted); line-height: 1.5;">
            📍 {{ site.location }}
          </div>
        </div>

        <div class="footer-col">
          <h4>Engineering Services</h4>
          <ul class="footer-links">
            <li><NuxtLink to="/#services">Python Task Automation</NuxtLink></li>
            <li><NuxtLink to="/#services">Public SEO & Market Analytics</NuxtLink></li>
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
            <li>
              <a :href="site.github" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 6px;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
                </svg>
                <span>GitHub Repository</span>
              </a>
            </li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          &copy; {{ currentYear }} SyntaxCraft Studio (syntaxcraft.dev). All rights reserved.
        </div>
        <div style="display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
          <span>📍 {{ site.city }}</span>
          <span>Official Support: <a :href="'mailto:' + site.email" style="color: #38bdf8; text-decoration: underline;">{{ site.email }}</a></span>
          <span>Payments processed securely via Lemon Squeezy</span>
        </div>
      </div>
    </div>
  </footer>
</template>
