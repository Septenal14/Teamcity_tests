import allure
from pages.base_page import BasePage


class ScriptElement(BasePage):
    def __init__(self, page):
        self.page = page
        super().__init__(page)
        self.script_area = '.CodeMirror >> textarea'

    def input_data(self, script_area):
        with allure.step("ввод пользовательских данных"):
            self.actions.input_text(script_area, "TestTestTest\nTestTestTestTestTestTestTestTestTestTestTest")


class ElementsChoose(BasePage):
    def __init__(self, page):
        self.page = page
        super().__init__(page)
        self.command_line = 'text="Command Line"'

    def click_element(self, element):
        self.actions.click_button(element)
        self.actions.wait_for_page_load()


class ScriptPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page_url = '/admin/editRunType.html?id=buildType:Test123_Test123&runnerId=__NEW_RUNNER__&cameFromUrl=%2Fadmin%2FeditBuildRunners.html%3Fid%3DbuildType%253ATest123_Test123%26init%3D1&cameFromTitle='
        self.page = page
        self.script_element = ScriptElement(page)
        self.element_choose = ElementsChoose(page)

    def fill_script(self):
        with allure.step("переход на страницу логина"):
            self.actions.navigate(self.page_url)
            self.element_choose.click_element(self.element_choose.command_line)
            self.script_element.input_data(self.script_element.script_area)

