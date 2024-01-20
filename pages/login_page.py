import allure
from pages.base_page import BasePage


class LoginForm(BasePage):
    def __init__(self, page):
        self.page = page
        super().__init__(page)
        self.username = "#username"
        self.password = "#password"
        self.login_button = ".loginButton"

    def input_user_data(self, user_name, user_password):
        with allure.step("ввод пользовательских данных"):
            self.input_filtered_text(self.username, user_name)
            self.input_filtered_text(self.password, user_password)

    def click_login_button(self):
        # TODO где то степы с большой буквы где то с маленькой
        #  - принято
        with allure.step("клик по кнопке авторизации"):
            self.click_button(self.login_button)

    def is_login_button_active(self):
        with allure.step("проверка активности кнопки авторизации"):
            return self.is_element_present(self.login_button)


class LoginPage(BasePage):
    def __init__(self, page):
        # TODO подмена понятий. page != browser
        super().__init__(page)
        self.page_url = '/login.html'
        # TODO зачем инициировать контент тут и передавать дальше, если он тут не используется?
        #  - resolved
        self.page = page
        self.login_form = LoginForm(page)

    def go_to_login_page(self):
        with allure.step("переход на страницу логина"):
            self.navigate(self.page_url)
            self.wait_for_page_load()

    def login(self, user_name="admin",  user_password="admin"):
        self.go_to_login_page()
        # TODO всегда только один пользователь? а что если захочу зайти под другим?
        self.login_form.input_user_data(user_name, user_password)
        self.login_form.click_login_button()
        self.wait_for_url_change(self.page_url)
