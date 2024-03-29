from api.auth_api import AuthAPI
from api.project_api import ProjectAPI
from api.user_api import UserAPI


class ApiManager:
    """
    Создает экземпляры классов для тестов в одной сессии
    session получает от фикстуры "session", которая управляет сессией
    Для использования в тестах передать фикстуру "api_manager" в параметры тестового метода
    К api классам обращаться через api_manager.{api-класс}.{метод-api-класса}
    """
    def __init__(self, session):
        self.session = session
        self.auth_api = AuthAPI(session)
        self.project_api = ProjectAPI(session)
        self.user_api = UserAPI(session)

    def close_session(self):
        self.session.close()
