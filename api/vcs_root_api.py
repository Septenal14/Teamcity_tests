from custom_requester.CustomRequester import CustomRequester


class VCSRootAPI(CustomRequester):
    def __init__(self, base_url, auth_credentials):
        super().__init__(base_url, auth_credentials)

    def create_vcs_root(self, vcs_root_data):
        return self.send_request("POST", "/app/rest/vcs-roots", data=vcs_root_data)
