from custom_requester.CustomRequester import CustomRequester


class ProjectAPI(CustomRequester):
    def __init__(self, requester):
        super().__init__(requester.base_url)
        self.requester = requester
        self.base_url = requester.base_url
        self.session = requester.session

    def create_project(self, project_data):
        return self.send_request("POST", "/app/rest/projects", data=project_data)

    def get_project(self, project_data):
        return self.send_request("GET", "/app/rest/projects")

    def is_project_in_list(self, project_id, project_name):
        """
        Проверяет, что проект с указанными project_id и project_name присутствует в списке проектов.

        :param project_id: ID проекта
        :param project_name: Название проекта
        :return: True, если проект найден; False в противном случае, и сообщение об ошибке
        """
        project_list_response = self.get_project()
        if project_list_response.status_code != 200:
            raise Exception(f"Failed to fetch project list. Status code: {project_list_response.status_code}")

        projects_list = project_list_response.json().get("project", [])
        for project in projects_list:
            if project["id"] == project_id and project["name"] == project_name:
                return True, None  # Проект найден
        return False, f"Проект с ID={project_id} и названием '{project_name}' не найден в списке проектов."