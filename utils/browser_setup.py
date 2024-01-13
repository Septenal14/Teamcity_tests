from playwright.sync_api import sync_playwright


class BrowserSetup:
    @classmethod
    def setup(cls):
        playwright = sync_playwright().start()
        # TODO хардкод хедлесс? Такое лучше в окружении держать
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        # TODO хардкод разрешение? Такое лучше в окружении держать
        page.set_viewport_size({"width": 1920, "height": 1080})
        return playwright, browser, page

    @classmethod
    def teardown(cls, playwright, browser):
        browser.close()
        playwright.stop()