import pytest
import requests

from api.api_manager import ApiManager
from data.project_data import ProjectData
from data.vcs_root_data import VCSRootData
from data.build_config_data import BuildConfigData


@pytest.fixture(scope='class')
def session():
    """
    Начинает сессию. Скоуп класса - одна сессия на весь тестовый класс
    По окончанию тестов yield закроет сессию
    """
    http_session = requests.Session()
    yield http_session
    http_session.close()


@pytest.fixture(scope='class')
def api_manager(session):
    return ApiManager(session)


@pytest.fixture
def vcs_root_data_fixture(project_data_fixture):
    project_id = project_data_fixture["id"]
    return VCSRootData.create_vcs_root(project_id)


@pytest.fixture
def build_config_data_fixture():
    project_id = "testprojectId"  # Пример project_id, его можно получать динамически
    return BuildConfigData.create_build_config(project_id)


@pytest.fixture
def project_invalid_id_data():
    def _project_invalid_id_data(project_invalid_id):
        return ProjectData.create_project_data_negative(project_invalid_id)
    return _project_invalid_id_data
