from custom_requester.CustomRequester import CustomRequester


class VCSRootAPI(CustomRequester):
    def __init__(self, requester):
        self.requester = requester
        self.base_url = requester.base_url
        self.session = requester.session

    def create_vcs_root(self, vcs_root_data):
        return self.send_request("POST", "/app/rest/vcs-roots", data=vcs_root_data)
