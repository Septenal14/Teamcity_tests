from playwright.sync_api import sync_playwright

from pages.auth_page import LoginPage


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("admin", "admin")
        # Проверка перенаправления на нужную страницу
        page.wait_for_load_state("networkidle")

        expected_url = "http://localhost:8111/favorite/projects?mode=builds"
        assert page.url == expected_url, "Не удалось перейти на ожидаемую страницу после входа"

        browser.close()
