from enums.hosts import BASE_URL
from playwright.sync_api import Page

class FavoriteProjectsPage:
    def __init__(self, page: Page):
        self.page = page
        self.create_project_button = page.locator("a[href*='createProjectMenu']")
        self.project_titles = page.locator("h2.ring-heading-heading")
        self.project_links = page.locator("a.ring-link-link")
        self.project_action_buttons = page.locator("button.ring-button-button")
        self.project_statuses = page.locator("span.Subproject__noChildrenWarning--tQ")

    def navigate(self):
        self.page.goto(f"{BASE_URL}/favorite/projects?mode=builds")

    def click_create_project(self):
        self.create_project_button.click()

