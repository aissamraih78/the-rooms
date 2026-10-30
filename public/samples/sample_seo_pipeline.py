"""
SyntaxCraft Studio - Open Evaluation Sample: SEO Analytics Pipeline
Website: https://syntaxcraft.dev
License: Free for evaluation, MIT

This self-contained script demonstrates our asynchronous pipeline pattern
for extracting public search trends and Core Web Vitals benchmarks.
"""

import asyncio
import time
from datetime import datetime, timezone


class PublicMetricsSample:
    def __init__(self):
        self.version = "1.0.0-sample"

    async def analyze_keyword(self, keyword: str):
        # Simulates non-blocking async network call to public index
        await asyncio.sleep(0.15)
        length_factor = min(len(keyword) * 5, 40)
        return {
            "keyword": keyword,
            "difficulty": 45 + length_factor,
            "estimated_monthly_searches": 8400 + (len(keyword) * 120),
            "trend": "+12.4% (Quarterly Growth)",
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        }

    async def benchmark_domain(self, domain: str):
        await asyncio.sleep(0.2)
        return {
            "domain": domain,
            "lcp_sec": 1.15,
            "fid_ms": 14,
            "cls_score": 0.008,
            "performance_rating": "Good (Passes Core Web Vitals)"
        }


async def main():
    print("=" * 65)
    print("⚡ SyntaxCraft Studio — Public Evaluation Sample Pipeline")
    print("=" * 65)
    
    sample = PublicMetricsSample()
    keywords = ["Nuxt 3 starter kit", "FastAPI background worker", "Lemon Squeezy integration"]
    domains = ["syntaxcraft.dev", "example.com"]
    
    start_time = time.time()
    
    print("\n[1/2] Dispathing asynchronous keyword trend tasks...")
    kw_tasks = [sample.analyze_keyword(k) for k in keywords]
    kw_results = await asyncio.gather(*kw_tasks)
    
    for r in kw_results:
        print(f"  ✓ [{r['keyword']}] Difficulty: {r['difficulty']}/100 | Volume: {r['estimated_monthly_searches']} | {r['trend']}")
        
    print("\n[2/2] Benchmarking domain public Core Web Vitals...")
    domain_tasks = [sample.benchmark_domain(d) for d in domains]
    domain_results = await asyncio.gather(*domain_tasks)
    
    for d in domain_results:
        print(f"  ✓ [{d['domain']}] LCP: {d['lcp_sec']}s | FID: {d['fid_ms']}ms | Rating: {d['performance_rating']}")
        
    elapsed = time.time() - start_time
    print("-" * 65)
    print(f"✓ All tasks executed successfully in {elapsed:.2f} seconds.")
    print("For full production suites & commercial licenses visit: https://syntaxcraft.dev\n")


if __name__ == "__main__":
    asyncio.run(main())
