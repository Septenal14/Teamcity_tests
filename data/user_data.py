from utils.custom_faker import DataGenerator
from enums.roles import Roles
from pydantic import BaseModel, Field


class RoleAssignment(BaseModel):
    roleId: str
    scope: str


class RolesModel(BaseModel):
    role: list[RoleAssignment]


class UserData(BaseModel):
    username: str = Field(default_factory=DataGenerator.fake_name)
    password: str = Field(default_factory=DataGenerator.fake_project_id)
    email: str = Field(default_factory=DataGenerator.fake_email)
    roles: RolesModel

    @staticmethod
    def create_user_data(role=Roles.SYSTEM_ADMIN.value, scope="g") -> dict[str, any]:
        return UserData(
            roles=RolesModel(role=[RoleAssignment(roleId=role, scope=scope)])
        ).model_dump()
