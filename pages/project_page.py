from playwright.sync_api import Page
from enums.hosts import BASE_URL


class ProjectsPage:
    def __init__(self, page: Page):
        self.page = page
        self.new_project_button = page.locator(".ProjectCreateSection__button--VX")


class ProjectsPageActions:
    def __init__(self, page: Page, locators):
        self.page = page
        self.locators = locators

    def navigate(self):
        self.page.goto(f"{BASE_URL.BASE_URL}/favorite/projects?mode=builds")

    def create_new_project(self):
        self.new_project_button.click()
        self.page.wait_for_url(self._create_project_url())

    @staticmethod
    def _create_project_url():
        base_url = BASE_URL.BASE_URL
        project_id = "_Root"
        show_mode = "createProjectMenu"
        came_from_url = "http%3A%2F%2Flocalhost%3A8111%2Ffavorite%2Fprojects%3Fmode%3Dbuilds"
        return f"{base_url}/admin/createObjectMenu.html?projectId={project_id}&showMode={show_mode}&cameFromUrl={came_from_url}#createManually"
