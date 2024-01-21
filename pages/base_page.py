import allure
from playwright.sync_api import Page
from enums.hosts import BASE_URL


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self._base_url = BASE_URL
        self._endpoint = ""

    @property
    def page_url(self):
        return self._base_url + self._endpoint

    @page_url.setter
    def page_url(self, endpoint):
        self._endpoint = endpoint

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

    def click_button(self, selector):
        with allure.step(f"Клик по элементу: {selector}"):
            self.page.click(selector)

    def is_element_present(self, selector):
        with allure.step(f"Проверка наличия элемента: {selector}"):
            return len(self.page.query_selector_all(selector)) > 0

    def is_button_active(self, selector):
        with allure.step(f"Проверка активности кнопки: {selector}"):
            return self.page.is_enabled(selector)

    def input_text(self, selector, text):
        with allure.step(f"Ввод текста '{text}' в элемент: {selector}"):
            self.page.fill(selector, text)

    def input_filtered_text(self, selector, text):
        with allure.step(f"Ввод текста 'FILTERED' в элемент: {selector}"):
            self.page.fill(selector, text)

    def wait_for_selector(self, selector, timeout=30000):
        with allure.step(f"Ожидаем появление селектора {selector}, таймаут: {timeout/100} секунд"):
            self.page.wait_for_selector(selector, state="attached", timeout=timeout)

    def wait_disappear_selector(self, selector, timeout=30000):
        with allure.step(f"Ожидание исчезновения лоадера: {selector}"):
            self.page.wait_for_selector(selector, state="detached", timeout=timeout)

    def activate_checkbox_if_not_active(self, selector):
        with allure.step(f"Активация чекбокса: {selector}"):
            if not self.page.is_checked(selector):
                self.page.click(selector)
                assert self.page.is_checked(selector), f"Чекбокс {selector} не получилось активировать"
