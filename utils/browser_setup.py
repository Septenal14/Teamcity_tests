from playwright.sync_api import sync_playwright


class BrowserSetup:
    @classmethod
    def setup(cls):
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})
        return playwright, browser, page

    @classmethod
    def teardown(cls, playwright, browser):
        browser.close()
        playwright.stop()