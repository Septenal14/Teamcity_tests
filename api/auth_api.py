from custom_requester.CustomRequester import CustomRequester
from enums.hosts import BASE_URL


class AuthAPI(CustomRequester):
    def __init__(self):
        super().__init__(BASE_URL)
        self.authenticate_and_get_csrf()

    def authenticate_and_get_csrf(self):
        # Шаг 1: Аутентификация с базовыми учетными данными
        self.session.auth = ("admin", "admin")  # Учетные данные администратора, при желании можно вынести в переменные окружения
        # Шаг 2: Получение CSRF токена
        csrf_token = self.send_request("GET", "/authenticationTest.html?csrf").text
        # Шаг 3: Обновление заголовков сессии
        self.session.headers.update({"X-TC-CSRF-Token": csrf_token})
