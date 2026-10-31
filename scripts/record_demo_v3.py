import asyncio
import os
import subprocess
import imageio_ffmpeg
from playwright.async_api import async_playwright

async def record_master_demo():
    video_dir = r"C:\Users\Alone\Desktop\syntaxcraft_demo_recording_v3"
    os.makedirs(video_dir, exist_ok=True)
    
    # 1. Clean previous recordings
    for f in os.listdir(video_dir):
        try:
            os.remove(os.path.join(video_dir, f))
        except Exception:
            pass

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            record_video_dir=video_dir,
            viewport={"width": 1920, "height": 1080},
            record_video_size={"width": 1920, "height": 1080}
        )
        page = await context.new_page()
        
        # Load warmed-up local site instantly
        print("1. Opening local platform on http://localhost:3333/...")
        await page.goto("http://localhost:3333/", wait_until="domcontentloaded", timeout=15000)
        await page.wait_for_timeout(1000)  # zero dead air - immediate hero view
        
        # Scroll smoothly to interactive sandbox
        print("2. Demonstrating interactive sandbox...")
        await page.locator("#showcase").scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)
        
        # Click Run Code on extractor tab
        run_btn = page.locator(".terminal-run-btn").first
        if await run_btn.count() > 0:
            await run_btn.click()
            await page.wait_for_timeout(2500)
            
        # Switch tab to webhook worker
        tabs = page.locator(".terminal-tab")
        if await tabs.count() > 1:
            await tabs.nth(1).click()
            await page.wait_for_timeout(1200)
            if await run_btn.count() > 0:
                await run_btn.click()
                await page.wait_for_timeout(2500)
                
        # Switch tab to data pipeline
        if await tabs.count() > 2:
            await tabs.nth(2).click()
            await page.wait_for_timeout(1200)
            if await run_btn.count() > 0:
                await run_btn.click()
                await page.wait_for_timeout(2500)

        # Scroll to Pricing section
        print("3. Demonstrating transparent commercial pricing...")
        await page.locator("#pricing").scroll_into_view_if_needed()
        await page.wait_for_timeout(3500)
        
        # Scroll down through fulfillment model
        print("4. Showing fulfillment model and GitHub delivery...")
        await page.locator("#process").scroll_into_view_if_needed()
        await page.wait_for_timeout(2500)
        
        # Scroll to Footer
        await page.evaluate("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'})")
        await page.wait_for_timeout(2000)

        # Navigate to GitHub official repo
        print("5. Showing official GitHub codebase...")
        try:
            await page.goto("https://github.com/syntaxcraft2026/the-rooms", wait_until="domcontentloaded", timeout=20000)
            await page.wait_for_timeout(2500)
            await page.mouse.wheel(0, 600)
            await page.wait_for_timeout(2500)
        except Exception as e:
            print("GitHub load error:", e)
        
        await context.close()
        await browser.close()
        
    print("Video captured. Now converting to MP4...")
    webm_files = [f for f in os.listdir(video_dir) if f.endswith(".webm")]
    if webm_files:
        input_webm = os.path.join(video_dir, webm_files[0])
        output_mp4 = r"C:\Users\Alone\Desktop\syntaxcraft_product_demo.mp4"
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        cmd = [
            ffmpeg_exe, "-y", "-i", input_webm,
            "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p",
            output_mp4
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        print("Conversion result returncode:", res.returncode)
        if res.returncode == 0:
            print("Pristine MP4 generated successfully:", output_mp4)
            size_mb = os.path.getsize(output_mp4) / (1024 * 1024)
            print(f"File size: {size_mb:.2f} MB")

if __name__ == "__main__":
    asyncio.run(record_master_demo())
