from custom_requester.custom_requestor import CustomRequester


class VCSRootAPI(CustomRequester):
    def __init__(self, session):
        super().__init__(session)

    def create_vcs_root(self, vcs_root_data):
        return self.send_request("POST", "/app/rest/vcs-roots", data=vcs_root_data)
