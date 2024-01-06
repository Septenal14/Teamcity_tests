import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        with allure.step(f"Переход на URL: {url}"):
            self.page.goto(url)

    def check_url(self, expected_url):
        with allure.step(f"Проверка URL: ожидаемый URL - {expected_url}"):
            assert self.page.url == expected_url

    def wait_for_url_change(self, previous_url):
        with allure.step(f"Проверка, что URL: {previous_url} изменился"):
            self.page.wait_for_function(f"window.location.href !== '{previous_url}'")

    def wait_for_page_load(self):
        with allure.step(f"Ожидание загрузки страницы"):
            self.page.wait_for_load_state('load')
