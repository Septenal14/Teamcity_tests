from playwright.sync_api import sync_playwright

from pages.auth_page import LoginPage
from pages.favorite_project_page import FavoriteProjectsPage
from pages.project_page import ProjectsPage


def test_login(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("admin", "admin")

    # Ожидание загрузки страницы после входа
    page.wait_for_load_state("networkidle")

    # Проверка перенаправления на нужную страницу
    expected_url = "http://localhost:8111/favorite/projects?mode=builds"
    assert page.url == expected_url, "Не удалось перейти на ожидаемую страницу после входа"


def test_create_new_project(browser):
    # Аутентификация
    login_page = LoginPage(browser)
    login_page.navigate()
    login_page.login("admin", "admin")

    # Переход на страницу проектов и создание нового проекта
    projects_page = ProjectsPage(browser)
    projects_page.navigate()
    projects_page.create_new_project()

    # Проверка перехода на страницу создания проекта
    expected_url = ProjectsPage._create_project_url()
    assert browser.url == expected_url, "Не удалось перейти на страницу создания проекта"


def test_create_project():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("admin", "admin")

        # После успешной авторизации, переходим на страницу Favorite Projects
        favorite_projects_page = FavoriteProjectsPage(page)
        favorite_projects_page.navigate()

        # Нажимаем на кнопку создания нового проекта
        favorite_projects_page.click_create_project()

        # Проверяем, что URL соответствует ожидаемому
        expected_url = "http://localhost:8111/admin/createObjectMenu.html?projectId=_Root&showMode=createProjectMenu&cameFromUrl=http%3A%2F%2Flocalhost%3A8111%2Ffavorite%2Fprojects%3Fmode%3Dbuilds#createManually"
        assert page.url == expected_url, "URL страницы не соответствует ожидаемому"

        browser.close()


