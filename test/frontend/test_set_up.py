import allure
from pages.setup_page import SetUpPage


@allure.title("Сетап сервера")
@allure.description("Сетапим проект принимая пользовательское соглашение, инициализируя БД и создавая админ юзера")
def test_set_up(browser):
    with allure.step("Сетап"):
        set_up_page = SetUpPage(browser)
        set_up_page.set_up()
