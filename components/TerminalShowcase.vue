<script setup lang="ts">
import { ref } from 'vue'

const activeTab = ref('scraper')
const isRunning = ref(false)
const terminalOutput = ref<string[]>([
  '✓ Loaded 4 parallel workers on Python 3.12 engine',
  '✓ Session proxy pool initialized: 50 residential IPs active',
  '✓ Target ready: https://target-platform.internal/catalog',
  '⚡ Ready to run automated tasks...'
])

const tabs = [
  { id: 'scraper', name: 'scraper_engine.py' },
  { id: 'bot', name: 'webhook_worker.py' },
  { id: 'pipeline', name: 'data_pipeline.py' },
]

const codeSnippets: Record<string, string[]> = {
  scraper: [
    'import asyncio, httpx, playwright.async_api',
    '',
    'async def extract_catalog_stream(proxy_pool):',
    '    async with httpx.AsyncClient(proxies=proxy_pool) as client:',
    '        response = await client.get("https://api.stream.io/v2/items")',
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
    if (activeTab.value === 'scraper') {
      terminalOutput.value.push('→ Connected 10 async worker threads...')
      terminalOutput.value.push('→ Harvested 1,420 clean records [0 errors]')
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
      <div>
        <button
          class="btn btn-sm"
          style="background: rgba(6, 182, 212, 0.15); color: #38bdf8; border: 1px solid rgba(6, 182, 212, 0.3); font-family: var(--font-mono); font-size: 0.72rem; padding: 4px 10px;"
          :disabled="isRunning"
          @click="runScript"
        >
          {{ isRunning ? '⚡ Running...' : '▶ Run Code' }}
        </button>
      </div>
    </div>

    <div class="terminal-body">
      <div v-for="(line, index) in codeSnippets[activeTab]" :key="index" class="terminal-code-line">
        <span class="line-no">{{ index + 1 }}</span>
        <span>
          <template v-if="line.startsWith('import ') || line.startsWith('from ') || line.startsWith('def ') || line.startsWith('async ')">
            <span class="code-keyword">{{ line.split(' ')[0] }}</span> {{ line.substring(line.indexOf(' ') + 1) }}
          </template>
          <template v-else-if="line.startsWith('#')">
            <span class="code-comment">{{ line }}</span>
          </template>
          <template v-else>
            {{ line }}
          </template>
        </span>
      </div>

      <div class="terminal-output">
        <div v-for="(out, i) in terminalOutput" :key="i" style="margin-bottom: 3px;">
          {{ out }}
        </div>
      </div>
    </div>
  </div>
</template>
