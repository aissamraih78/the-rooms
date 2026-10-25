<script setup lang="ts">
import { site } from '~/data/site'
</script>

<template>
  <header class="site-header">
    <div class="container header-inner">
      <NuxtLink to="/" class="brand-logo" aria-label="SyntaxCraft Studio Home">
        <div class="brand-icon">&lt;/&gt;</div>
        <div class="brand-name">Syntax<span class="brand-tag">Craft</span></div>
      </NuxtLink>

      <nav aria-label="Primary Navigation">
        <ul class="nav-links">
          <li v-for="item in site.nav" :key="item.label">
            <NuxtLink :to="item.href" class="nav-link">{{ item.label }}</NuxtLink>
          </li>
        </ul>
      </nav>

      <div style="display: flex; align-items: center; gap: 12px;">
        <NuxtLink to="/#pricing" class="btn btn-primary btn-sm">
          Get Started
        </NuxtLink>
      </div>
    </div>
  </header>
</template>
