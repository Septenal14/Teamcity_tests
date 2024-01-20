import pytest
import allure
from data.project_data import ProjectData
from http import HTTPStatus
from contextlib import contextmanager


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
        cls.created_project_id = cls.project_data["id"]

    @allure.feature("project")
    @allure.title("Создание проекта")
    @allure.description("Создание проекта. Проверка успешности создания "
                        "и его нахождения в списке проектов")
    def test_project_create(self, super_admin, user_create):
        with project_cleanup(super_admin, self.created_project_id):
            with allure.step("Отправка запроса на создание проекта"):
                create_project_response = super_admin.api_object.project_api.create_project(self.project_data).json()
            with allure.step("Проверка совпадения id проекта в теле ответа и в теле запроса"):
                assert create_project_response.get("id", {}) == self.created_project_id,\
                    f"expected project id= {self.created_project_id}, but '{create_project_response.get('id', {})}' given"
            with allure.step("Получение списка проектов"):
                get_projects_response = super_admin.api_object.project_api.get_project().json()
            with allure.step("Записываем в переменную список id проектов"):
                project_ids = [project.get('id', {}) for project in get_projects_response.get('project', [])]
            with allure.step("Проверка наличия id созданного проекта в массиве"):
                assert self.created_project_id + 1 in project_ids, \
                    f"expected created project id={self.created_project_id} in project_ids, but not matched"
            # #TODO а если упадет выше, то проект не удалится)
            #  - resolved

    @pytest.mark.parametrize("id_value, desc, assert_cont", [
        (1, "Первый символ не ascii", "starts with non-letter character"),
        ('a' * 256, "Более 255 символов", "is 256 characters long while the maximum length is 225")
    ])
    @pytest.mark.negative
    @allure.feature("project")
    @allure.title("Создание проекта")
    @allure.description("Негативный кейс создания проекта с использованием параметризации")
    def test_project_create_negative(self, api_manager, project_invalid_id_data, id_value, desc, assert_cont):
        with allure.step(f"Подготовка данных для отправки запроса '{desc}'"):
            project_invalid_data = project_invalid_id_data(id_value)
        with allure.step("Отправка запроса на создание проекта"):
            resp = api_manager.project_api.create_project(project_invalid_data, expected_status=HTTPStatus.INTERNAL_SERVER_ERROR)
        with allure.step("Проверка ответа"):
            assert assert_cont in resp.text, "Response don't have expected message"

