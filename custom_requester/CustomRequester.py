import requests
import logging


class CustomRequester:
    def __init__(self, base_url):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json", "Accept": "application/json"})
        self.base_url = base_url

    def send_request(self, method, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, json=data)
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
