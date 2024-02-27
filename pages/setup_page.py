import allure
from pages.base_page import BasePage


class FirstStartWindow(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.window_locator = "#nestedPageContent"
        self.proceed_button_locator = "#proceedButton"

    def proceed_step(self):
        with allure.step("Нажатие кнопки proceed"):
            self.click_button(self.proceed_button_locator)


class Loading(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.loading_icon_locator = ".icon-refresh"

    def wait_loading(self, timeout_wait=1000, timeout_disappear=1000000):
        with allure.step("Ждем начала лоадинга"):
            self.wait_for_selector(self.loading_icon_locator, timeout_wait)
        with allure.step("Ждем когда закончится лоадинг"):
            self.wait_disappear_selector(self.loading_icon_locator, timeout_disappear)


class Agreement(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.page_url = f"/showAgreement.html"
        self.accept_checkbox_locator = "input#accept"
        self.continue_button_locator = ".submitButton"

    def check_in_box(self):
        with allure.step("Активируем чекбокс"):
            self.activate_checkbox_if_not_active(self.accept_checkbox_locator)

    def continue_agreement(self):
        with allure.step("Принимаем Agreement"):
            self.click_button(self.continue_button_locator)


class SetUpUser(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.username_locator = "#input_teamcityUsername"
        self.password_locator = "#password1"
        self.confirm_password_locator = "#retypedPassword"
        self.create_button = ".loginButton"

    def fill_user_data(self, user_name, user_password):
        self.input_text(self.username_locator, user_name)
        self.input_text(self.password_locator, user_password)
        self.input_text(self.confirm_password_locator, user_password)

    def create_user(self):
        self.click_button(self.create_button)


class SetUpPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_start_window = FirstStartWindow(self.page)
        self.loading = Loading(self.page)
        self.agreement = Agreement(self.page)
        self.setup_user = SetUpUser(self.page)

    def set_up(self, username="admin", password="admin"):
        self.navigate(self.page_url)
        self.wait_for_page_load()
        self.first_start_window.proceed_step()
        self.loading.wait_loading()
        self.first_start_window.proceed_step()
        self.loading.wait_loading()
        self.check_url(self.agreement.page_url)
        self.agreement.check_in_box()
        self.agreement.continue_agreement()
        self.wait_for_url_change(self.agreement.page_url)
        self.wait_for_page_load()
        self.setup_user.fill_user_data(username, password)
        self.setup_user.create_user()
        self.wait_for_url_change(self.setup_user.page_url)
