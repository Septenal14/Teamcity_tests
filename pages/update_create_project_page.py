import allure
from actions.ui_actions import Actions
from pages.base_page import BasePage
from enums.hosts import BASE_URL


class ContentFragment:
    def __init__(self, page):
        self.page = page
        self.selector = "#content"


class MenuListCreateFragment:
    def __init__(self, content_fragment, actions):
        self.content_fragment = content_fragment
        self.actions = actions
        self.create_from_url_selector = (f"{self.content_fragment.selector} "
                                         f"a.createOption:has-text('From a repository URL')")
        self.create_manually_selector = (f"{self.content_fragment.selector} "
                                         f"a.createOption:has-text(' Manually')")

    def click_create_from_url(self):
        with allure.step("Выбор создания проекта по URL"):
            self.actions.click_button(self.create_from_url_selector)

    def click_create_manually(self):
        with allure.step("Выбор создания проекта мануально"):
            self.actions.click_button(self.create_manually_selector)

    def is_create_from_url_active(self):
        with allure.step("Проверка активности кнопки создания проекта по URL"):
            return self.actions.is_element_active(self.create_from_url_selector)

    def is_create_manually_active(self):
        with allure.step("Проверка активности кнопки создания проекта мануально"):
            return self.actions.is_element_active(self.create_manually_selector)


class CreateFormContainerFragment:
    def __init__(self, content_fragment, actions):
        self.content_fragment = content_fragment
        self.actions = actions
        self.project_name_selector = f"{self.content_fragment.selector} input#name"
        self.project_id_selector = f"{self.content_fragment.selector} input#externalId"
        self.project_description_selector = f"{self.content_fragment.selector} input#description"
        self.create_project_button = f"{self.content_fragment.selector} input.submitButton"

    def input_project_details(self, name, id, description):
        with allure.step("Ввод данных для создания проекта"):
            self.actions.input_text(self.project_name_selector, name)
            self.actions.input_text(self.project_id_selector, id)
            self.actions.input_text(self.project_description_selector, description)

    def click_create_button(self):
        with allure.step("Нажатие кнопки создания проекта"):
            self.actions.click_button(self.create_project_button)


class ProjectCreationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page_url = (f'{BASE_URL}/admin/createObjectMenu.html?projectId=_Root&showMode=createProjectMenu&'
                         f'cameFromUrl=http%3A%2F%2Flocalhost%3A8111%2Ffavorite%2Fprojects')
        self.actions = Actions(page)
        self.content = ContentFragment(page)
        self.menu_list_create = MenuListCreateFragment(self.content, self.actions)
        self.create_form_container = CreateFormContainerFragment(self.content, self.actions)

    def go_to_creation_page(self):
        with allure.step("Переход на страницу создания проекта"):
            self.navigate(self.page_url)
            self.wait_for_page_load()

    def create_project(self, name, project_id, description):
        self.go_to_creation_page()
        self.menu_list_create.click_create_manually()
        self.create_form_container.input_project_details(name, project_id, description)
        self.create_form_container.click_create_button()
