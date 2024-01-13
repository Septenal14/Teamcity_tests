import allure


class Actions:
    #TODO не понимаю смысла этого класса, честно говоря. Кажется что это должно быть в BasePage. Ну и подмена понятий browser/page
    def __init__(self, page):
        self.page = page

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
