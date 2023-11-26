from custom_requester.CustomRequester import CustomRequester


class BuildAPI(CustomRequester):
    def __init__(self, requester):
        self.requester = requester
        self.base_url = requester.base_url
        self.session = requester.session

    def create_build_configuration(self, build_config_data):
        return self.requester.send_request("POST", "/app/rest/buildTypes", data=build_config_data)

    def run_build(self, build_data):
        return self.send_request("POST", "/app/rest/buildQueue", data=build_data)

    def check_build_status(self, build_id):
        return self.send_request("GET", f"/app/rest/builds/id:{build_id}")
