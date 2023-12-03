from playwright.sync_api import Page


class EditProjectPage:
    def __init__(self, page: Page):
        self.page = page
        self.project_created_message = page.locator("div#message_projectCreated")
        self.save_button = page.locator("input[name='submitButton']")


class EditProjectPageActions:
    def __init__(self, page: Page, locators):
        self.page = page
        self.locators = locators

    def verify_project_created(self, project_name):
        expected_substring = f'Project "{project_name}" has been successfully created.'
        message_locator = self.page.locator("#message_projectCreated")
        actual_message = message_locator.text_content()
        return expected_substring in actual_message and message_locator.is_visible()
