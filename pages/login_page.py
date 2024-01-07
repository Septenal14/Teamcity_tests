import allure
from enums.hosts import BASE_URL
from actions.ui_actions import Actions
from pages.base_page import BasePage


class ContentFragment:
    def __init__(self, page):
        self.page = page
        self.selector = "#pageContent"


class LoginForm:
    def __init__(self, content_fragment, actions):
        self.content_fragment = content_fragment
        self.actions = actions
        self.username = f"{self.content_fragment.selector} #username"
        self.password = f"{self.content_fragment.selector} #password"
        self.login_button = f"{self.content_fragment.selector} .loginButton"

    def input_user_data(self, user_name, user_password):
        with allure.step("ввод пользовательских данных"):
            self.actions.input_filtered_text(self.username, user_name)
            self.actions.input_filtered_text(self.password, user_password)

    def click_login_button(self):
        with allure.step("клик по кнопке авторизации"):
            self.actions.click_button(self.login_button)

    def is_login_button_active(self):
        with allure.step("проверка активности кнопки авторизации"):
            return self.actions.is_element_active(self.login_button)


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_url = f'{BASE_URL}/login.html'
        self.actions = Actions(page)
        self.content = ContentFragment(page)
        self.login_form = LoginForm(self.content, self.actions)

    def go_to_login_page(self):
        with allure.step("Переход на страницу логина"):
            self.navigate(self.login_url)
            self.wait_for_page_load()

    def login(self):
        self.go_to_login_page()
        self.login_form.input_user_data("admin", "admin")
        self.login_form.click_login_button()
        self.wait_for_url_change(self.login_url)
