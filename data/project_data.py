from utils.custom_faker import DataGenerator


class ProjectData:
    @staticmethod
    def create_project():
        return {
            "parentProject": {"locator": "_Root"},
            "name": DataGenerator.fake_name(),
            "id": DataGenerator.fake_id(),
            "copyAllAssociatedSettings": True
        }
