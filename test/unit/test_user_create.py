from enums.roles import Roles


def test_user(super_admin, user_create):
    project_admin = user_create(Roles.PROJECT_ADMIN.value)
    project_admin.api_object.auth_api.authenticate(project_admin.creds)
    system_admin = user_create(Roles.SYSTEM_ADMIN.value)
    system_admin.api_object.auth_api.authenticate(system_admin.creds)

    print(project_admin.username)
    print(system_admin.username)
