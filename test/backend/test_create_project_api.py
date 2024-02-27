import pytest
import allure
from data.project_data import ProjectData
from http import HTTPStatus
from contextlib import contextmanager
from data.project_data import ProjectResponseModel


@contextmanager
def project_cleanup(super_admin, created_project_id):
    try:
        yield
    finally:
        with allure.step("Удаляем созданный проект"):
            super_admin.api_object.project_api.clean_up_project(created_project_id)


class TestProjectCreate:
    project_data = None

    @classmethod
    def setup_class(cls):
        cls.project_data = ProjectData.create_project_data()
        cls.project_data_id = cls.project_data.id

    @allure.feature("project")
    @allure.title("Создание проекта")
    @allure.description("Создание проекта. Проверка успешности создания "
                        "и его нахождения в списке проектов")
    def test_project_create(self, super_admin, user_create):
        with project_cleanup(super_admin, self.project_data_id):
            with allure.step("Отправка запроса на создание проекта"):
                response = super_admin.api_object.project_api.create_project(self.project_data.model_dump()).text
            with allure.step("Проверка совпадения id проекта и родительского проекта в теле ответа и в теле запроса"):
                project_response = ProjectResponseModel.model_validate_json(response)
                assert project_response.id == self.project_data_id, \
                    f"expected project id= {self.project_data_id}, but '{project_response.id}' given"
                assert project_response.parentProjectId == self.project_data.parentProject["locator"], \
                    (f"expected parent project id= {self.project_data.parentProject['locator']},"
                     f" but '{project_response.parentProjectId}' given in response")
            with allure.step("отправка запроса на получение информации о созданном проекте"):
                response = super_admin.api_object.project_api.get_project_by_locator(self.project_data.name).text
            with allure.step("проверка соответствия параметров созданного проекта с отправленными данными"):
                created_project = ProjectResponseModel.model_validate_json(response)
                assert created_project.id == self.project_data.id, \
                    f"expected project id= {self.project_data_id}, but '{created_project.id}' given"
                assert created_project.name == self.project_data.name, \
                    f"expected project name= {self.project_data.name}, but '{created_project.name}' given"
                assert project_response.parentProjectId == self.project_data.parentProject["locator"], \
                    (f"expected parent project id= {self.project_data.parentProject['locator']},"
                     f" but '{project_response.parentProjectId}' given in response")

    @pytest.mark.parametrize("id_value, desc, assert_cont", [
        (1, "Первый символ не ascii", "starts with non-letter character"),
        ('a' * 256, "Более 255 символов", "is 256 characters long while the maximum length is 225")
    ])
    @pytest.mark.negative
    @allure.feature("project")
    @allure.title("Создание проекта")
    @allure.description("Негативный кейс создания проекта с использованием параметризации")
    def test_project_create_negative(self, super_admin, project_invalid_id_data, id_value, desc, assert_cont):
        with allure.step(f"Подготовка данных для отправки запроса '{desc}'"):
            project_invalid_data = project_invalid_id_data(id_value)
        with allure.step("Отправка запроса на создание проекта"):
            resp = super_admin.api_object.project_api.create_project(project_invalid_data, expected_status=HTTPStatus.INTERNAL_SERVER_ERROR)
        with allure.step("Проверка ответа"):
            assert assert_cont in resp.text, "Response don't have expected message"

