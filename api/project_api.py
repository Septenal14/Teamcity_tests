from custom_requester.custom_requestor import CustomRequester
from enums.status_codes import StatusCodes


class ProjectAPI(CustomRequester):
    def __init__(self, session):
        super().__init__(session)

    def create_project(self, project_data):
        return self.send_request("POST", "/app/rest/projects", data=project_data)

    def get_project(self):
        return self.send_request("GET", "/app/rest/projects")

    def delete_project(self, project_id):
        return self.send_request("DELETE",
                                 f"/app/rest/projects/id:{project_id}",
                                 expected_status=StatusCodes.NO_CONTENT)

    def clean_up_project(self, created_project_id):
        """
        Функция клининга в тесте. Удаляет созданный проект и проверяет его отсутствии в списке проектов.
        При юзе в UI вызывать через api_manager
        :param created_project_id: принимает на вход созданный id_проекта который нужно удалить
        """
        self.delete_project(created_project_id)
        get_projects_response = self.get_project().json()

        project_ids = [project.get('id', {}) for project in get_projects_response.get('project', [])]
        assert created_project_id not in project_ids, \
            f"The expected list of IDs should not include created_project_id={created_project_id}, but it was found."
