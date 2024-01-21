import allure
from pages.create_project_page import ProjectCreationPage
from pages.login_page import LoginPage
import time


@allure.title("Авторизация и создание проекта")
@allure.description("авторизация пользователя, переход по ссылке на страницу создания проекта, создание проекта")
def test_create_project(browser_page, random_name, random_project_id, super_admin):
    with allure.step("Авторизация пользователя"):
        login_page = LoginPage(browser_page)
        login_page.login()
    with allure.step("Создание проекта"):
        project_creation_page = ProjectCreationPage(browser_page)
        project_creation_page.create_project(random_name, random_project_id, random_name)
    #TODO а если упадет выше, то проект не удалится)
    with allure.step("Удаление проекта"):
        super_admin.api_object.project_api.clean_up_project(random_project_id)
