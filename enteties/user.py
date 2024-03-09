from enums.roles import Roles
from typing import Any
from api.api_manager import ApiManager


class Role:
    def __init__(self, role_id, scope="g", href=None):
        if role_id not in Roles.__members__:
            raise ValueError(f"Invalid role: {role_id}")
        self.role_id = role_id
        self.scope = scope
        self.href = href


class Groups:
    def __init__(self, key):
        self.key = key


class User:
    def __init__(self, username: str, password: str, session: ApiManager, roles: list, **kwargs: Any):
        self.username = username
        self.password = password
        self.email = None
        self.roles = roles
        self.groups = None
        self.api_object = session

    @property
    def creds(self):
        return self.username, self.password


