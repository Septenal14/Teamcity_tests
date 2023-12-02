import pytest

from data.project_data import ProjectData
from data.vcs_root_data import VCSRootData
from data.build_config_data import BuildConfigData
from playwright.sync_api import sync_playwright
from pages.auth_page import LoginPage


@pytest.fixture
def project_data_fixture():
    return ProjectData.create_project()


@pytest.fixture
def vcs_root_data_fixture(project_data_fixture):
    project_id = project_data_fixture["id"]
    return VCSRootData.create_vcs_root(project_id)


@pytest.fixture
def build_config_data_fixture():
    project_id = "testprojectId"  # Пример project_id, его можно получать динамически
    return BuildConfigData.create_build_config(project_id)


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)
        yield browser
        browser.close()