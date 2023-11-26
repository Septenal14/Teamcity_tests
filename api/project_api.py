from custom_requester.CustomRequester import CustomRequester


class ProjectAPI(CustomRequester):
    def __init__(self, base_url, auth_credentials):
        super().__init__(base_url, auth_credentials)

    def create_project(self, project_data):
        return self.send_request("POST", "/app/rest/projects", data=project_data)
