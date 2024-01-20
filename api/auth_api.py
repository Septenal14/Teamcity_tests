from custom_requester.custom_requestor import CustomRequester


class AuthAPI(CustomRequester):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def authenticate(self, user_creds):
        # TODO все тот же коммент про юзера
        self.session.auth = user_creds
        #TODO А если что то пойдет не так и csrf токена не будет? может проверку сделать?
        csrf_token = self.send_request("GET", "/authenticationTest.html?csrf").text
        if not csrf_token:
            raise ValueError("CSRF token is missing or invalid")
        #TODO зачем распаковка когда можно через именнованные агрументы?
        self._update_session_headers(**{"X_TC_CSRF_Token": csrf_token})
