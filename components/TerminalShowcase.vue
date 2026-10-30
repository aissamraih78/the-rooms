<script setup lang="ts">
import { ref } from 'vue'

const activeTab = ref('extractor')
const isRunning = ref(false)
const terminalOutput = ref<string[]>([
  '✓ Loaded 4 parallel workers on Python 3.12 engine',
  '✓ Dataset connection established: SSL verified endpoint',
  '✓ Target ready: https://api.public-market.io/v2/catalog',
  '⚡ Ready to run automated tasks...'
])

const tabs = [
  { id: 'extractor', name: 'data_extractor.py' },
  { id: 'bot', name: 'webhook_worker.py' },
  { id: 'pipeline', name: 'data_pipeline.py' },
]

const codeSnippets: Record<string, string[]> = {
  extractor: [
    'import asyncio, httpx',
    '',
    'async def sync_public_catalog(api_endpoint):',
    '    async with httpx.AsyncClient(timeout=10.0) as client:',
    '        response = await client.get(api_endpoint)',
    '        items = response.json().get("results", [])',
    '        return [clean_entity(item) for item in items]',
    '',
    '# Autonomous scheduler daemon',
    'asyncio.run(pipeline_daemon(interval_sec=3600))'
  ],
  bot: [
    'from fastapi import FastAPI, Request',
    'from bot_handler import notify_telegram, sync_database',
    '',
    'app = FastAPI(title="SyntaxCraft Webhook Listener")',
    '',
    '@app.post("/webhooks/order-created")',
    'async def handle_order(req: Request):',
    '    event = await req.json()',
    '    await sync_database(event["data"])',
    '    await notify_telegram(f"⚡ New Order Settled: ${event[\'total\']}")',
    '    return {"status": "dispatched"}'
  ],
  pipeline: [
    'import polars as pl',
    'from sqlalchemy import create_engine',
    '',
    'def execute_etl_pipeline(source_csv, db_uri):',
    '    df = pl.read_csv(source_csv).filter(pl.col("verified") == True)',
    '    df = df.with_columns(pl.col("revenue").fill_null(0))',
    '    df.write_database(table_name="analytics_daily", connection=db_uri)',
    '    print("✓ Pipeline ETL finished: 12,480 rows indexed.")'
  ]
}

function runScript() {
  if (isRunning.value) return
  isRunning.value = true
  terminalOutput.value = ['Executing ' + activeTab.value + ' in sandbox...']
  
  setTimeout(() => {
    terminalOutput.value.push('→ Initializing isolated sandbox environment...')
  }, 400)
  
  setTimeout(() => {
    if (activeTab.value === 'extractor') {
      terminalOutput.value.push('→ Connected 10 async worker threads...')
      terminalOutput.value.push('→ Processed 1,420 clean records [0 errors]')
      terminalOutput.value.push('✓ Status 200 OK — Data persisted to SQLite warehouse!')
    } else if (activeTab.value === 'bot') {
      terminalOutput.value.push('→ Webhook payload received & signature verified.')
      terminalOutput.value.push('→ Sent notification to Telegram channel [Message ID: 94812]')
      terminalOutput.value.push('✓ Status 200 OK — Task resolved in 84ms!')
    } else {
      terminalOutput.value.push('→ Loaded dataset: 14,200 raw data entities.')
      terminalOutput.value.push('→ Normalizing schema & indexing timestamps...')
      terminalOutput.value.push('✓ ETL execution finished in 142ms [Memory: 18MB]!')
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
  res = res.replace(/\b(FastAPI|Request|AsyncClient|polars|pl|sqlite3|create_engine)\b/g, '<span style="color: #38bdf8;">$1</span>')

  // Restore tokens
  return res.replace(/___TOKEN_(\d+)___/g, (_, idx) => tokens[parseInt(idx, 10)])
}
</script>
