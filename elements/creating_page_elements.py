class InputElement:
    def __init__(self, locator):
        self.locator = locator

    def fill(self, text):
        self.locator.fill(text)

    def clear_and_fill(self, text):
        self.locator.fill("")  # Очищаем поле
        self.locator.fill(text)  # Заполняем новым текстом


class ButtonElement:
    def __init__(self, locator):
        self.locator = locator

    def click(self):
        self.locator.click()
