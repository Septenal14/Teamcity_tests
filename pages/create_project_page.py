from playwright.sync_api import Page
from elements.creating_page_elements import InputElement, ButtonElement


class ProjectCreationPage:

    def __init__(self, page: Page):
        self.page = page
        self.name_input = InputElement(page.locator("input[name='name']"))
        self.id_input = InputElement(page.locator("#externalId"))
        self.create_button = ButtonElement(page.locator("#createProject"))


class ProjectCreationPageActions:
    def __init__(self, page: Page, locators: ProjectCreationPage):
        self.page = page
        self.locators = locators

    def navigate(self):
        self.page.goto(
            "http://localhost:8111/admin/createObjectMenu.html?projectId=_Root&showMode=createProjectMenu&cameFromUrl=http%3A%2F%2Flocalhost%3A8111%2Ffavorite%2Fprojects%3Fmode%3Dbuilds#createManually",
            wait_until="load")

    def create_project(self, project_name, project_id):
        self.locators.name_input.clear_and_fill(project_name)
        self.locators.id_input.clear_and_fill(project_id)
        self.locators.create_button.click()
