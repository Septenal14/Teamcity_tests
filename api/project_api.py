from custom_requester.custom_requestor import CustomRequester


class ProjectAPI(CustomRequester):
    def __init__(self, session):
        super().__init__(session)

    def create_project(self, project_data):
        return self.send_request("POST", "/app/rest/projects", data=project_data)

    def get_project(self, project_data):
        return self.send_request("GET", "/app/rest/projects")
