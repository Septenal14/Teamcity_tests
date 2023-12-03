from pages.auth_page import LoginPageLocators, LoginPageActions
from pages.create_project_page import ProjectCreationPage, ProjectCreationPageActions
from pages.edit_project_page import EditProjectPage, EditProjectPageActions
from pages.favorite_project_page import FavoriteProjectsPage, FavoriteProjectsPageActions
from utils.custom_faker import DataGenerator


def test_create_project(browser, api_manager):
    page = browser.new_page()

    # Инициализация локаторов и действий для страницы логина
    login_locators = LoginPageLocators(page)
    login_actions = LoginPageActions(login_locators)
    login_actions.navigate_to_login()
    login_actions.login("admin", "admin")

    favorite_projects_locators = FavoriteProjectsPage(page)
    favorite_projects_actions = FavoriteProjectsPageActions(page, favorite_projects_locators)
    favorite_projects_actions.click_create_project()

    create_project_locators = ProjectCreationPage(page)
    create_project_actions = ProjectCreationPageActions(page, create_project_locators)
    project_name = DataGenerator.fake_name()
    project_id = DataGenerator.fake_id()
    create_project_actions.create_project(project_name, project_id)

    edit_project_locators = EditProjectPage(page)
    edit_project_actions = EditProjectPageActions(page, edit_project_locators)
    assert edit_project_actions.verify_project_created(project_name), "Сообщение о создании проекта не соответствует ожидаемому или не отображается"

    api_manager.project_api.clean_up_project(project_id)
