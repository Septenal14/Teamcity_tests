from data.project_data import ProjectData


class TestProjectCreate:
    project_data = None

    @classmethod
    def setup_class(cls):
        cls.project_data = ProjectData.create_project()
        cls.created_project_id = cls.project_data["id"]

    def test_project_create(self, api_manager):
        create_project_response = api_manager.project_api.create_project(self.project_data).json()
        assert create_project_response.get("id", {}) == self.created_project_id,\
            f"expected project id= {self.created_project_id}, but '{create_project_response.get('id', {})}' given"

        get_projects_response = api_manager.project_api.get_project().json()
        project_ids = [project['id'] for project in get_projects_response['project']]
        assert self.created_project_id in project_ids, \
            f"expected created project id={self.created_project_id} in project_ids, but not matched"

        api_manager.project_api.clean_up_project(self.created_project_id)
