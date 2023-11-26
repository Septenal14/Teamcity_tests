import pytest
from api.auth_api import AuthAPI
from api.project_api import ProjectAPI
from api.vcs_root_api import VCSRootAPI
from api.build_api import BuildAPI
from data.project_data import ProjectData
from data.vcs_root_data import VCSRootData
from data.build_config_data import BuildConfigData

def test_teamcity_build_process():
    # Аутентификация и получение CSRF токена
    auth_api = AuthAPI("http://localhost:8111")

    # Получение данных для теста
    project_data = ProjectData.create_project()
    vcs_root_data = VCSRootData.create_vcs_root(project_data["id"])
    build_config_data = BuildConfigData.create_build_config(project_data["id"])

    # Создание проекта
    project_api = ProjectAPI(auth_api)
    project_response = project_api.create_project(project_data)
    assert project_response.status_code == 200

    # Создание VCS Root
    vcs_root_api = VCSRootAPI(auth_api)
    vcs_root_response = vcs_root_api.create_vcs_root(vcs_root_data)
    assert vcs_root_response.status_code == 200

    # Создание конфигурации сборки
    build_api = BuildAPI(auth_api)
    build_config_response = build_api.create_build_configuration(build_config_data)
    assert build_config_response.status_code == 200

    # Здесь можно добавить дополнительные шаги и проверки, если требуется
