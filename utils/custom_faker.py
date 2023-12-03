import string
from faker import Faker

faker_instance = Faker()


class DataGenerator:

    @staticmethod
    def fake_id():
        first_letter = faker_instance.random.choice(string.ascii_letters)
        rest_characters = ''.join(faker_instance.random.choices(string.ascii_letters + string.digits + '_', k=10))
        project_id = first_letter + rest_characters
        return project_id

    @staticmethod
    def fake_name():
        return faker_instance.word()  # or any other suitable Faker method for name generation