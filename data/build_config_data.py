class BuildConfigData:
    @staticmethod
    def create_build_config(project_id):
        return {
            "id": "myBuildId",
            "name": "Test Build",
            "project": {
                "id": project_id
            },
            "steps": {
                "step": [
                    {
                        "name": "Print hello world",
                        "type": "simpleRunner",
                        "properties": {
                            "property": [
                                {"name": "script.content", "value": "echo 'Hello World!'"},
                                {"name": "teamcity.step.mode", "value": "default"},
                                {"name": "use.custom.script", "value": "true"}
                            ]
                        }
                    }
                ]
            }
        }
