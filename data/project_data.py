import string

import faker
from faker import Faker
from faker.generator import random


class ProjectDataGenerator:
    faker = Faker()

    @staticmethod
    def generate_project_id():
        first_letter = random.choice(string.ascii_letters)

        # Добавьте остальные символы (буквы, цифры и подчеркивания) случайным образом
        rest_characters = ''.join(random.choices(string.ascii_letters + string.digits + '_', k=10))

        # Объедините первую букву и остальные символы
        project_id = first_letter + rest_characters
        return project_id

    @staticmethod
    def generate_project_name():
        return ProjectDataGenerator.faker.word() # or any other suitable Faker method for name generation


class ProjectData:
    @staticmethod
    def create_project(name=None, projectid=None):
        if not name:
            name = ProjectDataGenerator.generate_project_name()
        if not projectid:
            projectid = ProjectDataGenerator.generate_project_id()
        return {
            "parentProject": {"locator": "_Root"},
            "name": name,
            "id": projectid,
            "copyAllAssociatedSettings": True
        }
