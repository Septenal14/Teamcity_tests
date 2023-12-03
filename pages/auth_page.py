from playwright.sync_api import Page
from enums.hosts import BASE_URL


class LoginPageLocators:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator(".loginButton")


class LoginPageActions:
    def __init__(self, locators):
        self.locators = locators

    def navigate_to_login(self):
        self.locators.page.goto(f"{BASE_URL}/login.html", wait_until="load")

    def login(self, username, password):
        self.locators.username_input.fill(username)
        self.locators.password_input.fill(password)
        self.locators.login_button.click()

