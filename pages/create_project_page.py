from playwright.sync_api import Page

class ProjectCreationPage:
    def __init__(self, page: Page):
        self.page = page
        self.name_input = page.locator("input[name='name']")
        self.id_input = page.locator("#externalId")
        self.create_button = page.locator("#createProject")

    def navigate(self):
        self.page.goto("http://localhost:8111/admin/createObjectMenu.html?projectId=_Root&showMode=createProjectMenu&cameFromUrl=http%3A%2F%2Flocalhost%3A8111%2Ffavorite%2Fprojects%3Fmode%3Dbuilds#createManually")

    def create_project(self, name, project_id):
        self.name_input.fill(name)
        self.id_input.fill(project_id)
        self.create_button.click()
