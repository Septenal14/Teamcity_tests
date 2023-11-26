import requests
import logging
from logging.handlers import RotatingFileHandler
import os
from enums.status_codes import StatusCodes


class CustomRequester:
    def __init__(self, base_url):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json", "Accept": "application/json"})
        self.base_url = base_url

        self.logger = logging.getLogger(__name__)
        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)

            # Define log format
            log_format = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

            # Получите абсолютный путь к директории, где находится CustomRequester.py
            current_directory = os.path.dirname(os.path.abspath(__file__))

            # Определите абсолютный путь к лог-файлу
            log_file = os.path.join(current_directory, 'logs', 'requester.log')
            file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024 * 5, backupCount=5)
            file_handler.setFormatter(log_format)

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(log_format)

            # Add handlers to logger
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def send_request(self, method, endpoint, data=None, expected_status=StatusCodes.SC_OK, **kwargs):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"Sending {method} request to {url}\nHeaders: {self.session.headers}\nBody: {data}")
        response = self.session.request(method, url, json=data)

        # Determine how to parse the response
        if 'application/json' in response.headers.get('Content-Type', ''):
            response_data = response.json()
        else:
            response_data = response.text

        # Log response details
        self.logger.info(
            f"Response from {url}: {response.status_code}\nHeaders: {response.headers}\nBody: {response_data}")

        # Check for expected status code
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}")

        return response
