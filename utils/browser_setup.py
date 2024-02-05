from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv


load_dotenv(override=True)
browser_width = int(os.getenv('BROWSER_WIDTH', '800'))
browser_height = int(os.getenv('BROWSER_HEIGHT', '600'))
headless_env = os.getenv('HEADLESS', 'True')
headless_mode = (headless_env == 'True' or headless_env != 'False' and bool(headless_env))

 
class BrowserSetup:
    @classmethod
    def setup(cls):
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=headless_mode)
        page = browser.new_page()
        page.set_viewport_size({"width": browser_width, "height": browser_height})
        return playwright, browser, page

    @classmethod
    def teardown(cls, playwright, browser):
        browser.close()
        playwright.stop()
