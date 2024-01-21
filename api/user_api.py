from custom_requester.custom_requestor import CustomRequester
from http import HTTPStatus


class UserAPI(CustomRequester):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def create_user(self, user_data):
        return self.send_request("POST", "/app/rest/users", data=user_data)

    def delete_user(self, user_locator):
        return self.send_request("DELETE", f"/app/rest/users/{user_locator}",
                                 expected_status=HTTPStatus.NO_CONTENT)
