import asyncio
from playwright.async_api import async_playwright

async def get_page_dimensions():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://example.com')  # Load a page
        
        dimensions = await page.evaluate('''() => {
            return {
                width: document.documentElement.clientWidth,
                height: document.documentElement.clientHeight, 
                deviceScaleFactor: window.devicePixelRatio,
            }
        }''')
        
        print(dimensions)
        await browser.close()

asyncio.run(get_page_dimensions())