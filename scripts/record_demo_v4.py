import asyncio
import os
import time
import subprocess
import imageio_ffmpeg
from playwright.async_api import async_playwright

async def record_master_seo_demo():
    video_dir = r"C:\Users\Alone\Desktop\syntaxcraft_demo_recording_v4"
    os.makedirs(video_dir, exist_ok=True)
    
    # 1. Clean previous recordings
    for f in os.listdir(video_dir):
        try:
            os.remove(os.path.join(video_dir, f))
        except Exception:
            pass

    t_start = 0
    t_ready = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            record_video_dir=video_dir,
            viewport={"width": 1920, "height": 1080},
            record_video_size={"width": 1920, "height": 1080}
        )
        t_start = time.time()
        page = await context.new_page()
        
        # 1. Fast load with warm server
        print("1. Loading platform...")
        await page.goto("http://localhost:3333/", wait_until="domcontentloaded", timeout=15000)
        await page.wait_for_selector(".hero-title", timeout=15000)
        await page.wait_for_selector(".terminal-window", timeout=15000)
        # Ensure styles and fonts are applied
        await page.wait_for_timeout(800)
        t_ready = time.time()

        # 2. Hero Section Display (starts here cleanly)
        print("2. Displaying Hero Section & Value Proposition...")
        await page.evaluate("window.scrollTo(0, 0)")
        await page.wait_for_timeout(2500)
        
        # 3. Interactive Terminal Execution
        print("3. Demonstrating Interactive SEO Terminal in Real-Time...")
        await page.locator("#showcase").scroll_into_view_if_needed()
        await page.wait_for_timeout(800)
        
        # Run Code on Tab 1: title_optimizer.py
        run_btn = page.locator(".terminal-run-btn").first
        if await run_btn.count() > 0:
            await run_btn.click()
            await page.wait_for_timeout(2200)
            
        # Switch tab to schema_builder.py & run
        tabs = page.locator(".terminal-tab")
        if await tabs.count() > 1:
            await tabs.nth(1).click()
            await page.wait_for_timeout(700)
            if await run_btn.count() > 0:
                await run_btn.click()
                await page.wait_for_timeout(2200)
                
        # Switch tab to content_formatter.py & run
        if await tabs.count() > 2:
            await tabs.nth(2).click()
            await page.wait_for_timeout(700)
            if await run_btn.count() > 0:
                await run_btn.click()
                await page.wait_for_timeout(2200)

        # 4. Scroll to 15 SEO & Webmaster Utilities Catalog
        print("4. Browsing 15 SEO & Webmaster Utilities Catalog...")
        await page.locator("#tools").scroll_into_view_if_needed()
        await page.wait_for_timeout(2000)
        
        # Smooth scrolling through modular tools
        await page.mouse.wheel(0, 450)
        await page.wait_for_timeout(1800)
        await page.mouse.wheel(0, 500)
        await page.wait_for_timeout(1800)

        # 5. Scroll to Transparent Pricing & Commercial Bundles ($5-$19, $89, $249)
        print("5. Showing Pricing Tiers and Lemon Squeezy Licensing...")
        await page.locator("#pricing").scroll_into_view_if_needed()
        await page.wait_for_timeout(3000)
        
        # 6. Fulfillment model and FAQ
        print("6. Showing Instant Digital Fulfillment & White-Hat FAQ...")
        await page.locator("#process").scroll_into_view_if_needed()
        await page.wait_for_timeout(2000)

        faq = page.locator("#faq")
        if await faq.count() > 0:
            await faq.scroll_into_view_if_needed()
            await page.wait_for_timeout(2000)

        # 7. Navigate to Official GitHub repository
        print("7. Showing Verified GitHub Codebase & Python Tests...")
        try:
            await page.goto("https://github.com/syntaxcraft2026/the-rooms", wait_until="domcontentloaded", timeout=20000)
            await page.wait_for_timeout(2500)
            await page.mouse.wheel(0, 400)
            await page.wait_for_timeout(2500)
        except Exception as e:
            print("GitHub load error:", e)
        
        await context.close()
        await browser.close()

    trim_delay = max(0.0, round(t_ready - t_start - 0.2, 2))
    print(f"Video captured. Initial load took ~{t_ready - t_start:.2f}s. Trimming first {trim_delay}s to ensure 0s dead air...")

    webm_files = [f for f in os.listdir(video_dir) if f.endswith(".webm")]
    if webm_files:
        input_webm = os.path.join(video_dir, webm_files[0])
        output_mp4 = r"C:\Users\Alone\Desktop\syntaxcraft_product_demo.mp4"
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        
        # Use -ss before -i to trim any initial loading/blank frame with zero dead air
        cmd = [
            ffmpeg_exe, "-y",
            "-ss", str(trim_delay),
            "-i", input_webm,
            "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p",
            output_mp4
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        print("Conversion result returncode:", res.returncode)
        if res.returncode == 0:
            print("Pristine MP4 generated successfully:", output_mp4)
            size_mb = os.path.getsize(output_mp4) / (1024 * 1024)
            print(f"File size: {size_mb:.2f} MB")
            return output_mp4
    return None

if __name__ == "__main__":
    asyncio.run(record_master_seo_demo())
