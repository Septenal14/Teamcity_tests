from custom_requester.custom_requestor import CustomRequester
from enums.status_codes import StatusCodes


class ProjectAPI(CustomRequester):
    def __init__(self, session):
        super().__init__(session)

    def create_project(self, project_data):
        return self.send_request("POST", "/app/rest/projects", data=project_data)

    def get_project(self, project_data):
        return self.send_request("GET", "/app/rest/projects")

    def delete_project(self, project_id):
        return self.send_request("DELETE",
                                 f"/app/rest/projects/id:{project_id}",
                                 expected_status=StatusCodes.NO_CONTENT)

    def clean_up_project(self, created_project_id):
        self.delete_project(created_project_id)
        get_projects_response = self.get_project(self).json()

        project_ids = [project['id'] for project in get_projects_response['project']]
        assert created_project_id not in project_ids, \
            f"expected created project id={created_project_id} in project_ids, but not matched"
