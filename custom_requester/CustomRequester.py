import requests
import logging


class CustomRequester:
    def __init__(self, base_url, auth_credentials):
        self.base_url = base_url
        self.auth_credentials = auth_credentials
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json", "Accept": "application/json"})

    def get_csrf_token(self):
        response = self.send_request("GET", "/authenticationTest.html?csrf")
        self.session.headers.update({"X-TC-CSRF-Token": response.text})
        return response.text

    def send_request(self, method, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        if headers is None:
            headers = {}
        response = self.session.request(method, url, auth=self.auth_credentials, json=data, headers=headers)
        response.raise_for_status()
        return response


    def log_response(self, response):
        # Логирование запроса и ответа
        request = response.request
        request_headers = "\n".join([f"{header}: {value}" for header, value in request.headers.items()])
        response_headers = "\n".join([f"{header}: {value}" for header, value in response.headers.items()])

        self.logger.info(f"Request: {request.method} {request.url}\nHeaders:\n{request_headers}")
        if request.body:
            self.logger.info(f"Body: {request.body}")

        self.logger.info(f"Response: {response.status_code}\nHeaders:\n{response_headers}")
        if response.text:
            self.logger.info(f"Body: {response.text}")
