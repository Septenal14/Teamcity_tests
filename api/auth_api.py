from custom_requester.custom_requestor import CustomRequester


class AuthAPI(CustomRequester):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def authenticate(self, user_creds):
        self.session.auth = user_creds
        csrf_token = self.send_request("GET", "/authenticationTest.html?csrf").text
        if not csrf_token:
            raise ValueError("CSRF token is missing or invalid")
        self._update_session_headers(**{"X-TC-CSRF-Token": csrf_token})
