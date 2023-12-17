from pages.auth_page import LoginPageLocators, LoginPageActions
from pages.create_project_page import ProjectCreationPage, ProjectCreationPageActions
from pages.edit_project_page import EditProjectPage, EditProjectPageActions
from pages.favorite_project_page import FavoriteProjectsPage, FavoriteProjectsPageActions
from utils.custom_faker import DataGenerator
from utils.browser_setup import BrowserSetup
from elements.creating_page_elements import InputElement, ButtonElement


def setup_module(module):
    global browser, page
    browser, page = BrowserSetup.setup()

def teardown_module(module):
    BrowserSetup.teardown(browser)

def test_create_project(api_manager):
    # Инициализация Page Objects и Actions для страницы логина
    login_locators = LoginPageLocators(page)
    login_actions = LoginPageActions(login_locators)
    login_actions.navigate_to_login()
    login_actions.login("admin", "admin")

    # Инициализация Page Objects и Actions для страницы избранных проектов
    favorite_projects_page = FavoriteProjectsPage(page)
    favorite_projects_actions = FavoriteProjectsPageActions(page, favorite_projects_page)
    favorite_projects_actions.click_create_project()

    # Инициализация Page Objects и Actions для страницы создания проекта
    create_project_page = ProjectCreationPage(page)
    create_project_actions = ProjectCreationPageActions(page, create_project_page)
    project_name = DataGenerator.fake_name()
    project_id = DataGenerator.fake_id()
    create_project_actions.create_project(project_name, project_id)

    # Инициализация Page Objects и Actions для страницы редактирования проекта
    edit_project_page = EditProjectPage(page)
    edit_project_actions = EditProjectPageActions(page, edit_project_page)
    assert edit_project_actions.verify_project_created(project_name), "Сообщение о создании проекта не соответствует ожидаемому или не отображается"

    # Очистка созданного проекта через API
    api_manager.project_api.clean_up_project(project_id)
