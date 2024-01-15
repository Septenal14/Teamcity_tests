import pytest
import requests

from api.api_manager import ApiManager
from data.project_data import ProjectData
from utils.custom_faker import DataGenerator
from utils.browser_setup import BrowserSetup
from resources.user_creds import USERNAME, PASSWORD
from data.user_data import UserData
from enums.roles import Roles


@pytest.fixture(scope="function")
def browser():
    playwright, browser_instance, page = BrowserSetup.setup()
    yield page
    BrowserSetup.teardown(playwright, browser_instance)


@pytest.fixture(scope='class')
def session():
    http_session = requests.Session()
    yield http_session
    http_session.close()


@pytest.fixture(scope='class')
def api_manager(session):
    return ApiManager(session)


@pytest.fixture
def user_session():
    user_pool = []

    def _create_user_session():
        session = requests.Session()
        user_session = ApiManager(session)
        user_pool.append(user_session)
        return user_session

    yield _create_user_session

    for user in user_pool:
        user.close_session()


@pytest.fixture
def super_admin_creds():
    return USERNAME, PASSWORD


def _create_user_creds(user_session, user_data, admin_creds):
    super_admin = user_session()
    super_admin.auth_api.authenticate(admin_creds)
    super_admin.user_api.create_user(user_data)
    user_creds = (user_data['username'], user_data['password'])
    user = user_session()
    user.auth_api.authenticate(user_creds)
    user.creds = user_creds
    return user


@pytest.fixture
def system_admin_account(user_session, super_admin_creds):
    return _create_user_creds(
        user_session,
        UserData.create_user_data(role=Roles.SYSTEM_ADMIN),
        super_admin_creds
    )


@pytest.fixture
def project_admin_account(user_session, super_admin_creds):
    return _create_user_creds(
        user_session,
        UserData.create_user_data(role=Roles.PROJECT_ADMIN),
        super_admin_creds
    )


@pytest.fixture
def not_auth_session(session):
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
