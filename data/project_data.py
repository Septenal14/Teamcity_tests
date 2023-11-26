class ProjectData:
    @staticmethod
    def create_project():
        return {
            "parentProject": {"locator": "_Root"},
            "name": "test project",
            "id": "testprojectId",
            "copyAllAssociatedSettings": True
        }
