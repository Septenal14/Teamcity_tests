from custom_requester.custom_requestor import CustomRequester


class AuthAPI(CustomRequester):
    def __init__(self, session):
        super().__init__(session)
        self.authenticate_and_get_csrf()

    def authenticate_and_get_csrf(self):
        # TODO все тот же коммент про юзера
        self.session.auth = ("admin", "admin")
        #TODO А если что то пойдет не так и csrf токена не будет? может проверку сделать?
        csrf_token = self.send_request("GET", "/authenticationTest.html?csrf").text
        #TODO зачем распаковка когда можно через именнованные агрументы?
        self._update_session_headers(**{"X-TC-CSRF-Token": csrf_token})
