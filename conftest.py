import pytest
import requests

from api.api_manager import ApiManager
from data.project_data import ProjectData
from utils.custom_faker import DataGenerator
from utils.browser_setup import BrowserSetup


@pytest.fixture(scope="function")
def browser():
    playwright, browser_instance, page = BrowserSetup.setup()
    yield page
    BrowserSetup.teardown(playwright, browser_instance)


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
def project_invalid_id_data():
    def _project_invalid_id_data(project_invalid_id):
        return ProjectData.create_project_data_negative(project_invalid_id)
    return _project_invalid_id_data


@pytest.fixture
def random_name():
    return DataGenerator.fake_name()


@pytest.fixture
def random_project_id():
    return DataGenerator.fake_project_id()
