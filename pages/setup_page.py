import allure
from pages.base_page import BasePage
from enums.hosts import BASE_URL
from actions.ui_actions import Actions


class FirstStartWindow:
    def __init__(self, page, actions):
        self.page = page
        self.actions = actions
        self.window_locator = "#nestedPageContent"
        self.proceed_button_locator = "#proceedButton"

    def proceed_step(self):
        with allure.step("Нажатие кнопки proceed"):
            self.actions.click_button(self.proceed_button_locator)


class Loading:
    def __init__(self, page, actions):
        self.page = page
        self.actions = actions
        self.loading_icon_locator = ".icon-refresh"

    def wait_loading(self, timeout_wait=1000, timeout_disappear=1000000):
        with allure.step("Ждем начала лоадинга"):
            self.actions.wait_for_selector(self.loading_icon_locator, timeout_wait)
        with allure.step("Ждем когда закончится лоадинг"):
            self.actions.wait_disappear_selector(self.loading_icon_locator, timeout_disappear)


class Agreement:
    def __init__(self, page, actions):
        self.page = page
        self.actions = actions
        self.page_url = f"{BASE_URL}/showAgreement.html"
        self.accept_checkbox_locator = "input#accept"
        self.continue_button_locator = ".submitButton"

    def check_in_box(self):
        with allure.step("Активируем чекбокс"):
            self.actions.activate_checkbox_if_not_active(self.accept_checkbox_locator)

    def continue_agreement(self):
        with allure.step("Принимаем Agreement"):
            self.actions.click_button(self.continue_button_locator)


class SetUpUser:
    def __init__(self, page, actions):
        self.page = page
        self.actions = actions
        self.page_url = f"{BASE_URL}/setupAdmin.html"
        self.username_locator = "#input_teamcityUsername"
        self.password_locator = "#password1"
        self.confirm_password_locator = "#retypedPassword"
        self.create_button = ".loginButton"

    def fill_user_data(self, user_name, user_password):
        self.actions.input_text(self.username_locator, user_name)
        self.actions.input_text(self.password_locator, user_password)
        self.actions.input_text(self.confirm_password_locator, user_password)

    def create_user(self):
        self.actions.click_button(self.create_button)


class SetUpPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.actions = Actions(page)
        self.first_start_window = FirstStartWindow(self.page, self.actions)
        self.loading = Loading(self.page, self.actions)
        self.agreement = Agreement(self.page, self.actions)
        self.setup_user = SetUpUser(self.page, self.actions)

    def set_up(self):
        self.navigate(BASE_URL)
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
        self.setup_user.fill_user_data("admin", "admin")
        self.setup_user.create_user()
        self.wait_for_url_change(self.setup_user.page_url)
