from utils.custom_faker import DataGenerator
from enums.roles import Roles


class UserData:
    @staticmethod
    def create_user_data(role="SYSTEM_ADMIN", scope="g"):
        return {
                "username": DataGenerator.fake_name(),
                "password": DataGenerator.fake_project_id(),
                "email": "example@email.com",
                "roles": {
                    "role": [
                        {
                            "roleId": role,
                            "scope": scope,
                        }
                    ]
                }
        }
