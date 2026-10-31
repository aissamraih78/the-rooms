<script setup lang="ts">
import { ref } from 'vue'

const activeTab = ref('title')
const isRunning = ref(false)
const terminalOutput = ref<string[]>([
  '✓ Loaded 15 SEO automation modules on Python 3.12 engine',
  '✓ Search engine guideline validator: Active & Compliant',
  '✓ Target: On-Page SEO Optimization & Schema Generator',
  '⚡ Ready to run automated SEO tasks...'
])

const tabs = [
  { id: 'title', name: 'title_optimizer.py' },
  { id: 'schema', name: 'schema_builder.py' },
  { id: 'content', name: 'content_formatter.py' },
]

const codeSnippets: Record<string, string[]> = {
  title: [
    'from seo_tools import optimize_product_title',
    '',
    '# High-CTR Product Title Optimization Engine',
    'title, score = optimize_product_title(',
    '    raw_name="handmade leather messenger bag men vintage",',
    '    primary_keyword="Leather Messenger Bag",',
    '    max_chars=60',
    ')',
    'print(f"SEO Title: {title}")',
    'print(f"SERP Pixel Width: 482px | CTR Score: {score}/100")'
  ],
  schema: [
    'from schema_tools import ProductSchema',
    '',
    '# Build Google Rich-Result Schema.org JSON-LD',
    'schema = ProductSchema(',
    '    name="Vintage Leather Messenger Bag",',
    '    sku="SKU-8921",',
    '    price="149.00",',
    '    currency="USD",',
    '    rating=4.9',
    ')',
    'json_ld = schema.to_json_ld()',
    'print("✓ Google Search Console validation passed [0 errors]")'
  ],
  content: [
    'from content_tools import format_paragraphs, audit_readability',
    '',
    '# Paragraph flow and readability score analyzer',
    'clean_body = format_paragraphs(raw_copy, words_per_p=45)',
    'stats = audit_readability(clean_body)',
    '',
    'print(f"✓ Flesch-Kincaid Score: {stats.score} [Optimal]")',
    'print(f"✓ Formatted 6 paragraphs with H2 transition anchors")'
  ]
}

function runScript() {
  if (isRunning.value) return
  isRunning.value = true
  terminalOutput.value = ['Executing ' + activeTab.value + ' in sandbox...']
  
  setTimeout(() => {
    terminalOutput.value.push('→ Initializing isolated SEO execution runtime...')
  }, 400)
  
  setTimeout(() => {
    if (activeTab.value === 'title') {
      terminalOutput.value.push('→ Analyzing search intent weighting & keyword density...')
      terminalOutput.value.push('→ Generated: "Vintage Leather Messenger Bag for Men | Handcrafted Daily Briefcase"')
      terminalOutput.value.push('✓ Status 200 OK — 58 characters (482px width) — CTR Score: 94/100!')
    } else if (activeTab.value === 'schema') {
      terminalOutput.value.push('→ Validating Schema.org Product & AggregateRating attributes...')
      terminalOutput.value.push('→ Synthesized valid JSON-LD structured data block.')
      terminalOutput.value.push('✓ Status 200 OK — Google Rich Result Eligibility Verified!')
    } else {
      terminalOutput.value.push('→ Scanning sentence length distribution & transition words...')
      terminalOutput.value.push('→ Restructured 4 dense blocks into 6 readable paragraphs.')
      terminalOutput.value.push('✓ Status 200 OK — Flesch-Kincaid: 78.4 (Plain English, Grade 8)!')
    }
    isRunning.value = false
  }, 1200)
}
</script>

<template>
  <div class="terminal-window">
    <div class="terminal-header">
      <div class="terminal-dots">
        <span class="terminal-dot red"></span>
        <span class="terminal-dot yellow"></span>
        <span class="terminal-dot green"></span>
      </div>
      <div class="terminal-tabs">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          class="terminal-tab"
          :class="{ active: activeTab === tab.id }"
          @click="activeTab = tab.id"
        >
          {{ tab.name }}
        </button>
      </div>
      <button class="terminal-run-btn" :disabled="isRunning" @click="runScript">
        <span v-if="isRunning">Executing...</span>
        <span v-else>▶ Run Code</span>
      </button>
    </div>

    <div class="terminal-code">
      <div
        v-for="(line, idx) in codeSnippets[activeTab]"
        :key="idx"
        class="code-line"
      >
        <span class="line-num">{{ idx + 1 }}</span>
        <span class="line-content" v-html="formatCode(line)"></span>
      </div>
    </div>

    <div class="terminal-output">
      <div
        v-for="(out, idx) in terminalOutput"
        :key="idx"
        class="output-line"
        :class="{ success: out.includes('✓'), info: out.includes('→'), warn: out.includes('⚡') }"
      >
        {{ out }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
function formatCode(code: string): string {
  if (!code) return '&nbsp;'
  const escaped = code
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')

  const tokens: string[] = []
  const saveToken = (html: string) => {
    tokens.push(html)
    return `___TOKEN_${tokens.length - 1}___`
  }

  // 1. Highlight comments first
  let res = escaped.replace(/(#.*$)/g, (m) => saveToken(`<span style="color: #64748b; font-style: italic;">${m}</span>`))
  // 2. Highlight string literals
  res = res.replace(/(".*?")/g, (m) => saveToken(`<span style="color: #10b981;">${m}</span>`))
  // 3. Highlight keywords
  res = res.replace(/\b(import|from|async|def|return|await|with|as)\b/g, '<span style="color: #f43f5e; font-weight: 600;">$1</span>')
  // 4. Highlight classes and functions
  res = res.replace(/\b(ProductSchema|Review|optimize_product_title|format_paragraphs|audit_readability|print)\b/g, '<span style="color: #38bdf8;">$1</span>')

  // Restore tokens
  return res.replace(/___TOKEN_(\d+)___/g, (_, idx) => tokens[parseInt(idx, 10)])
}
</script>
