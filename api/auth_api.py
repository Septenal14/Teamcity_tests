from custom_requester.custom_requestor import CustomRequester


class AuthAPI(CustomRequester):
    def __init__(self, session):
        super().__init__(session)
        self.authenticate_and_get_csrf()        # вызов метода для авторизации при создании экземпляра класса

    def authenticate_and_get_csrf(self):
        self.session.auth = ("admin", "admin")
        csrf_token = self.send_request("GET", "/authenticationTest.html?csrf").text
        self._update_session_headers(**{"X-TC-CSRF-Token": csrf_token})
