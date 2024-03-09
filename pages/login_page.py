import allure
from pages.base_page import BasePage


class LoginFormElement(BasePage):
    def __init__(self, page):
        self.page = page
        super().__init__(page)
        self.username = "#username"
        self.password = "#password"
        self.login_button = ".loginButton"

    def input_user_data(self, user_name, user_password):
        with allure.step("ввод пользовательских данных"):
            self.actions.input_filtered_text(self.username, user_name)
            self.actions.input_filtered_text(self.password, user_password)

    def click_login_button(self):
        # TODO где то степы с большой буквы где то с маленькой
        #  - принято
        with allure.step("клик по кнопке авторизации"):
            self.actions.click_button(self.login_button)

    def is_login_button_active(self):
        with allure.step("проверка активности кнопки авторизации"):
            return self.actions.is_element_present(self.login_button)


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page_url = '/login.html'
        self.page = page
        self.login_form = LoginFormElement(page)

    def go_to_login_page(self):
        with allure.step("переход на страницу логина"):
            self.actions.navigate(self.page_url)
            self.actions.wait_for_page_load()

    def login(self, user_name="admin",  user_password="admin"):
        self.go_to_login_page()
        self.login_form.input_user_data(user_name, user_password)
        self.login_form.click_login_button()
        self.actions.wait_for_url_change(self.page_url)
