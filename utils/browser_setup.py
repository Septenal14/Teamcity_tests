from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv


load_dotenv(override=True)
browser_width = int(os.getenv('BROWSER_WIDTH', '800'))
browser_height = int(os.getenv('BROWSER_HEIGHT', '600'))
headless_mode = bool(os.getenv('HEADLESS', 'True'))


class BrowserSetup:
    @classmethod
    def setup(cls):
        playwright = sync_playwright().start()
        # TODO хардкод хедлесс? Такое лучше в окружении держать
        browser = playwright.chromium.launch(headless=headless_mode)
        page = browser.new_page()
        # TODO хардкод разрешение? Такое лучше в окружении держать
        page.set_viewport_size({"width": browser_width, "height": browser_height})
        return playwright, browser, page

    @classmethod
    def teardown(cls, playwright, browser):
        browser.close()
        playwright.stop()
