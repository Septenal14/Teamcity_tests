from custom_requester.CustomRequester import CustomRequester


class ProjectAPI(CustomRequester):
    def __init__(self, requester):
        self.requester = requester
        self.base_url = requester.base_url
        self.session = requester.session

    def create_project(self, project_data):
        return self.send_request("POST", "/app/rest/projects", data=project_data)
