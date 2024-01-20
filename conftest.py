import pytest
import requests

from api.api_manager import ApiManager
from data.project_data import ProjectData
from utils.custom_faker import DataGenerator
from utils.browser_setup import BrowserSetup
from resources.user_creds import USERNAME, PASSWORD
from data.user_data import UserData
from enums.roles import Roles
from enteties.user import User, Groups, Role


@pytest.fixture(scope="function")
def browser_page():
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
def super_admin(user_session, super_admin_creds):
    new_session = user_session()
    super_admin = User(USERNAME, PASSWORD, new_session, ["SUPER_ADMIN", "g"])
    super_admin.api_object.auth_api.authenticate(super_admin.creds)
    return super_admin


@pytest.fixture
def super_admin_creds():
    return USERNAME, PASSWORD


@pytest.fixture
def user_create(user_session, super_admin):
    created_users_pool = []
    def _user_create(role):
        user_data = UserData.create_user_data(role=Roles.PROJECT_ADMIN.value, scope="g")
        super_admin.api_object.user_api.create_user(user_data)
        new_session = user_session()
        created_users_pool.append(user_data['username'])
        return User(user_data['username'], user_data['password'], new_session, [Role(role)])

    yield _user_create

    for username in created_users_pool:
        super_admin.api_object.user_api.delete_user(username)


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
