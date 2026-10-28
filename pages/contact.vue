<script setup lang="ts">
import { ref } from 'vue'
import { site } from '~/data/site'

const route = useRoute()
const selectedPkg = (route.query.package as string) || 'pro'

const formSubmitted = ref(false)
const formState = ref({
  name: '',
  email: '',
  packageChoice: selectedPkg === 'starter' ? 'Script Starter Package ($149)' : selectedPkg === 'enterprise' ? 'Enterprise Architecture Package ($1,199)' : 'Pro Automation & Web Suite ($449)',
  inquiryType: 'Pre-Purchase Technical Question',
  details: ''
})

function handleSubmit() {
  formSubmitted.value = true
}

useHead({
  title: 'Product Support & Technical Inquiries — SyntaxCraft Studio',
  meta: [
    { name: 'description', content: 'Contact SyntaxCraft Studio for questions regarding our software packages, commercial licensing, and technical setup.' }
  ]
})
</script>

<template>
  <div class="container" style="padding: 60px 0 100px;">
    <NuxtLink to="/" class="btn btn-secondary btn-sm" style="margin-bottom: 30px;">
      &larr; Back to Home
    </NuxtLink>

    <div style="display: grid; grid-template-columns: 1fr 1.15fr; gap: 60px; align-items: start;">
      <div>
        <div class="badge" style="margin-bottom: 16px;">Direct Engineering Desk</div>
        <h1 style="font-size: 2.8rem; margin-bottom: 16px;">Product Support & Technical Inquiries</h1>
        <p style="font-size: 1.05rem; line-height: 1.7; color: var(--text-secondary); margin-bottom: 36px;">
          Have questions regarding our Python automation packages, Nuxt 3 web starter architectures, or commercial software licensing? Our engineering team is on standby to assist with technical verification and setup guidance.
        </p>

        <div style="display: grid; gap: 20px; padding: 28px; background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);">
          <div style="display: flex; gap: 16px; align-items: flex-start;">
            <div style="width: 40px; height: 40px; border-radius: var(--radius-sm); background: rgba(6, 182, 212, 0.12); border: 1px solid rgba(6, 182, 212, 0.25); display: flex; align-items: center; justify-content: center; color: var(--accent-cyan); flex-shrink: 0;">
              ✉
            </div>
            <div>
              <div style="font-size: 0.76rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted);">Direct Support Email</div>
              <a :href="'mailto:' + site.email" style="font-size: 1.05rem; font-weight: 700; color: #ffffff; text-decoration: underline;">{{ site.email }}</a>
            </div>
          </div>

          <div style="display: flex; gap: 16px; align-items: flex-start;">
            <div style="width: 40px; height: 40px; border-radius: var(--radius-sm); background: rgba(56, 189, 248, 0.12); border: 1px solid rgba(56, 189, 248, 0.25); display: flex; align-items: center; justify-content: center; color: #38bdf8; flex-shrink: 0;">
              📍
            </div>
            <div>
              <div style="font-size: 0.76rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted);">Studio Location</div>
              <div style="font-size: 0.95rem; color: #cbd5e1;">{{ site.location }}</div>
            </div>
          </div>

          <div style="display: flex; gap: 16px; align-items: flex-start;">
            <div style="width: 40px; height: 40px; border-radius: var(--radius-sm); background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.25); display: flex; align-items: center; justify-content: center; color: var(--accent-emerald); flex-shrink: 0;">
              ⚡
            </div>
            <div>
              <div style="font-size: 0.76rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted);">Response SLA</div>
              <div style="font-size: 0.95rem; color: #cbd5e1;">{{ site.responseSla }}</div>
            </div>
          </div>

          <div style="display: flex; gap: 16px; align-items: flex-start;">
            <div style="width: 40px; height: 40px; border-radius: var(--radius-sm); background: rgba(139, 92, 246, 0.12); border: 1px solid rgba(139, 92, 246, 0.25); display: flex; align-items: center; justify-content: center; color: var(--accent-indigo); flex-shrink: 0;">
              💻
            </div>
            <div>
              <div style="font-size: 0.76rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted);">Verified Developer Profile</div>
              <a :href="site.github" target="_blank" rel="noopener noreferrer" style="font-size: 0.95rem; color: #38bdf8; text-decoration: underline;">{{ site.github }}</a>
            </div>
          </div>
        </div>
      </div>

      <!-- Form Box -->
      <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: 40px;">
        <div v-if="formSubmitted" style="text-align: center; padding: 40px 10px;">
          <div style="width: 60px; height: 60px; border-radius: 50%; background: rgba(16, 185, 129, 0.15); border: 1px solid var(--accent-emerald); display: flex; align-items: center; justify-content: center; color: var(--accent-emerald); font-size: 1.8rem; margin: 0 auto 20px;">
            ✓
          </div>
          <h2 style="font-size: 1.6rem; margin-bottom: 12px;">Inquiry Dispatched Successfully!</h2>
          <p style="color: var(--text-secondary); max-width: 420px; margin: 0 auto 24px; line-height: 1.6;">
            Thank you, <strong>{{ formState.name }}</strong>. Our lead engineer has received your inquiry and will respond to <strong>{{ formState.email }}</strong> within 12 hours.
          </p>
          <NuxtLink to="/" class="btn btn-secondary btn-sm">
            Return to Homepage
          </NuxtLink>
        </div>

        <form v-else @submit.prevent="handleSubmit" style="display: grid; gap: 20px;">
          <h2 style="font-size: 1.5rem; margin-bottom: 6px;">Technical Inquiry & Support Request</h2>
          <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 10px;">Fill out the details below for an expedited response from our technical team.</p>

          <div>
            <label style="display: block; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 8px; color: var(--text-secondary);">Your Name</label>
            <input
              v-model="formState.name"
              type="text"
              required
              placeholder="e.g. Alex Morgan"
              style="width: 100%; padding: 13px 16px; background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-subtle); border-radius: var(--radius-sm); color: #ffffff; font-size: 0.95rem; outline: none; transition: border-color 0.15s;"
            />
          </div>

          <div>
            <label style="display: block; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 8px; color: var(--text-secondary);">Work Email</label>
            <input
              v-model="formState.email"
              type="email"
              required
              placeholder="e.g. alex@company.com"
              style="width: 100%; padding: 13px 16px; background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-subtle); border-radius: var(--radius-sm); color: #ffffff; font-size: 0.95rem; outline: none; transition: border-color 0.15s;"
            />
          </div>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
            <div>
              <label style="display: block; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 8px; color: var(--text-secondary);">Package of Interest</label>
              <select
                v-model="formState.packageChoice"
                style="width: 100%; padding: 13px 16px; background: #0c121e; border: 1px solid var(--border-subtle); border-radius: var(--radius-sm); color: #ffffff; font-size: 0.88rem; outline: none;"
              >
                <option>Script Starter Package ($149)</option>
                <option>Pro Automation & Web Suite ($449)</option>
                <option>Enterprise Architecture Package ($1,199)</option>
                <option>General Licensing / Setup Question</option>
              </select>
            </div>

            <div>
              <label style="display: block; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 8px; color: var(--text-secondary);">Inquiry Type</label>
              <select
                v-model="formState.inquiryType"
                style="width: 100%; padding: 13px 16px; background: #0c121e; border: 1px solid var(--border-subtle); border-radius: var(--radius-sm); color: #ffffff; font-size: 0.88rem; outline: none;"
              >
                <option>Pre-Purchase Technical Question</option>
                <option>License & Commercial Rights</option>
                <option>Technical Setup & Compatibility</option>
                <option>Bug Fix & Warranty Support</option>
              </select>
            </div>
          </div>

          <div>
            <label style="display: block; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 8px; color: var(--text-secondary);">Inquiry Details</label>
            <textarea
              v-model="formState.details"
              rows="4"
              required
              placeholder="Describe your technical question, deployment environment, or licensing inquiry..."
              style="width: 100%; padding: 13px 16px; background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-subtle); border-radius: var(--radius-sm); color: #ffffff; font-size: 0.95rem; outline: none; resize: vertical; line-height: 1.6;"
            ></textarea>
          </div>

          <button type="submit" class="btn btn-primary" style="width: 100%; justify-content: center;">
            Submit Technical Inquiry &rarr;
          </button>
        </form>
      </div>
    </div>
  </div>
</template>
