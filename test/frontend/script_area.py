import allure
from pages.script_page import ScriptPage
from pages.login_page import LoginPage

@allure.title("Авторизация и создание проекта")
@allure.description("авторизация пользователя, переход по ссылке на страницу создания проекта, создание проекта")
def test_create_project(browser_page):
    with allure.step("Авторизация пользователя"):
        login_page = LoginPage(browser_page)
        login_page.login()
    with allure.step("Создание проекта"):
        script_page = ScriptPage(browser_page)
        script_page.fill_script()

