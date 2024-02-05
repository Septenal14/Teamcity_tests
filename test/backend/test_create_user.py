from enums.roles import Roles
from data.project_data import ProjectData
from data.project_data import ProjectResponseModel


class TestProjectCreate:
    project_data = None

    @classmethod
    def setup_class(cls):
        cls.project_data = ProjectData.create_project_data()

    def test_project_create_user(self, super_admin, user_create):
        project_user = user_create(Roles.PROJECT_ADMIN.value)
        project_user.api_object.auth_api.authenticate(project_user.creds)
        project_user.api_object.project_api.create_project(self.project_data.model_dump())
        response = super_admin.api_object.project_api.get_project_by_locator(self.project_data.name).text
        created_project = ProjectResponseModel.model_validate_json(response)
        assert created_project.id == self.project_data.id
        assert created_project.name == self.project_data.name


