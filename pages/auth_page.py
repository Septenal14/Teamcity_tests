from playwright.sync_api import Page
from enums.hosts import BASE_URL


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator(".loginButton")

    def navigate(self):
        self.page.goto(f"{BASE_URL}/login.html")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
