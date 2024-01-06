import allure
from pages.update_create_project_page import ProjectCreationPage
from pages.update_login_page import LoginPage
import time


@allure.title("Авторизация и создание проекта")
@allure.description("авторизация пользователя, переход по ссылке на страницу создания проекта, создание проекта")
def test_create_project(browser, random_name, random_project_id, api_manager):
    with allure.step("Авторизация пользователя"):
        login_page = LoginPage(browser)
        login_page.login()
    with allure.step("Создание проекта"):
        project_creation_page = ProjectCreationPage(browser)
        project_creation_page.create_project(random_name, random_project_id, random_name)
    with allure.step("Удаление проекта"):
        time.sleep(2)
        api_manager.project_api.clean_up_project(random_project_id)
