from api.auth_api import AuthAPI
from api.project_api import ProjectAPI
from data.project_data import ProjectData


class TestProjectCreate:
    project_data = None

    @classmethod
    def setup_class(cls):
        cls.project_data = ProjectData.create_project()
        cls.created_project_id = cls.project_data["id"]

    def test_project_create(self):
        auth_api = AuthAPI()
        project_api = ProjectAPI(auth_api)

        create_project_response = project_api.create_project(self.project_data).json()
        assert create_project_response.get("id", {}) == self.created_project_id,\
            f"expected project id= {self.created_project_id}, but '{create_project_response.get('id', {})}' given"
        get_projects_response = project_api.get_project(self).json()
        project_ids = [project['id'] for project in get_projects_response['project']]
        assert self.created_project_id in project_ids, \
            f"expected created project id={self.created_project_id} in project_ids, but not matched"
