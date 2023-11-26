class VCSRootData:
    @staticmethod
    def create_vcs_root(project_id):
        return {
            "id": "MyCustomRootId",
            "name": "MyCustomRoot",
            "vcsName": "jetbrains.git",
            "project": {"id": project_id},
            "properties": {
                "property": [
                    {"name": "authMethod", "value": "ANONYMOUS"},
                    {"name": "branch", "value": "refs/heads/master"},
                    {"name": "url", "value": "https://github.com/AlexPshe/spring-core-for-qa"}
                ]
            }
        }
