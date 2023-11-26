from custom_requester.CustomRequester import CustomRequester


class AuthAPI(CustomRequester):
    def __init__(self, base_url):
        auth_credentials = ("admin", "admin")  # Эти данные могут быть загружены из конфига или переменных окружения
        super().__init__(base_url, auth_credentials)
        self.csrf_token = self.get_csrf_token()

    def get_csrf_token(self):
        response = self.send_request("GET", "/authenticationTest.html?csrf")
        csrf_token = response.text
        self.session.headers.update({"X-TC-CSRF-Token": csrf_token})
        return csrf_token
