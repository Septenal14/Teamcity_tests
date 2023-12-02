from api.auth_api import AuthAPI
from api.build_api import BuildAPI
from api.project_api import ProjectAPI
from api.vcs_root_api import VCSRootAPI


class ApiManager:
    def __init__(self, session):
        self.auth_api = AuthAPI(session)
        self.build_api = BuildAPI(session)
        self.project_api = ProjectAPI(session)
        self.vcs_root_api = VCSRootAPI(session)