from api.auth_api import AuthAPI
from api.project_api import ProjectAPI
from api.vcs_root_api import VCSRootAPI
from api.build_api import BuildAPI
from data.project_data import ProjectData
from data.vcs_root_data import VCSRootData
from data.build_config_data import BuildConfigData


def test_teamcity_build_process():
    # Аутентификация и получение CSRF токена, создание сессии
    auth_api = AuthAPI()

    # Получение данных для теста
    project_data = ProjectData.create_project()
    project_id = project_data["id"]  # Сохраняем project_id
    project_name = project_data["name"]  # Сохраняем project_name
    # Создание проекта
    project_api = ProjectAPI(auth_api)
    project_response = project_api.create_project(project_data)
    response_data = project_response.json()
    assert response_data['id'] == project_id
    assert response_data['name'] == project_name
    assert response_data['parentProjectId'] == "_Root"

