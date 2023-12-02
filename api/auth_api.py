from custom_requester.custom_requestor import CustomRequester


class AuthAPI(CustomRequester):
    def __init__(self, session):
        super().__init__(session)
        self.authenticate_and_get_csrf()

    def authenticate_and_get_csrf(self):
        # Шаг 1: Аутентификация с базовыми учетными данными
        self.session.auth = ("admin", "admin")  # Учетные данные администратора, при желании можно вынести в переменные окружения
        # Шаг 2: Получение CSRF токена
        csrf_token = self.send_request("GET", "/authenticationTest.html?csrf").text
        # Шаг 3: Обновление заголовков сессии
        self._update_session_headers(**{"X-TC-CSRF-Token": csrf_token})
