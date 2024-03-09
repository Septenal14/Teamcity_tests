from enums.theme_type import ThemeType
from actions.page_actions import PageActions


class Header:
    def __init__(self, actions: PageActions):
        self.actions = actions
        self.container = 'header.Header__container--Cv'
        self.logo_button = '.ring-header-logo'
        self.projects_button = 'a[title="Projects"] >> text="Projects"'
        self.add_project_button = 'a[title="Create subproject"][data-test-link-with-icon="add"]'
        # self.changes_button = 'a[title="Changes"] >> text="Changes"'
        # self.agents_button = 'a[title="Agents"] >> text="Agents"'
        # self.agents_counter = 'span[data-hint-container-id="header-agents-active"]'
        # self.queue_button = 'a[title="Queue"] >> text="Queue"'
        # self.queue_counter = '[data-hint-container-id="header-queue-number"]'
        # self.theme_button = 'button >> text=/Theme/'
        # self.theme_drop_down = '[data-test-shown="true"]:has-text("Light"):has-text("Dark"):has-text("System theme")'
        # self.light_theme_button = 'div[data-test-shown="true"] >> text="Light"'
        # self.dark_theme_button = 'div[data-test-shown="true"] >> text="Dark"'
        # self.system_theme_button = 'div[data-test-shown="true"] >> text="System theme"'

    def go_to_projects_throw_header_button(self):
        self.actions.is_button_active(self.projects_button)
        self.actions.click_button(self.projects_button)
        self.actions.wait_for_page_load()

    def go_to_create_project_throw_header_button(self):
        self.actions.is_button_active(self.add_project_button)
        self.actions.click_button(self.add_project_button)
        self.actions.wait_for_page_load()

    # def go_to_agents_throw_header_button(self):
    #     self.actions.is_button_active(self.agents_button)
    #     self.actions.click_button(self.agents_button)
    #     self.actions.wait_for_page_load()

    # def change_theme(self, theme_type: ThemeType):
    #     self.actions.click_button(self.theme_button)
    #     match theme_type:
    #         case ThemeType.SYSTEM:
    #             self.actions.click_button(self.system_theme_button)
    #         case ThemeType.LIGHT:
    #             self.actions.click_button(self.light_theme_button)
    #         case ThemeType.DARK:
    #             self.actions.click_button(self.dark_theme_button)
    #
    #     self.actions.wait_for_page_load()
