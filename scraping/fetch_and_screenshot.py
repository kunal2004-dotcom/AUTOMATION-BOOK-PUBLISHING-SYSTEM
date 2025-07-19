from playwright.sync_api import sync_playwright
import os

def fetch_chapter_and_screenshot(url, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Save screenshot
        screenshot_path = os.path.join(save_dir, "chapter 1.png")
        page.screenshot(path=screenshot_path, full_page=True)

        # Save text
        content = page.inner_text("body")
        text_path = os.path.join(save_dir, "raw_text.txt")
        with open(text_path, "w", encoding="utf-8") as f:
            f.write(content)

        browser.close()
