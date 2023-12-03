import logging
from logging.handlers import RotatingFileHandler
import os
from enums.status_codes import StatusCodes
from enums.hosts import BASE_URL


class CustomRequester:
    base_headers = dict({"Content-Type": "application/json", "Accept": "application/json"})

    def __init__(self, session):
        self.session = session
        self.base_url = BASE_URL
        self.logger = None
        self.setup_logger()

    def send_request(self, method, endpoint, data=None, expected_status=StatusCodes.SC_OK, need_logging=True, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, json=data)

        if need_logging:
            self.log_request_and_response(method, url, data, response)

        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}")

        return response

    def _update_session_headers(self, **kwargs):
        self.headers = self.base_headers.copy()
        self.headers.update(kwargs)
        self.session.headers.update(self.headers)

    def setup_logger(self):
        self.logger = logging.getLogger(__name__)
        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)

            # Define log format
            log_format = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

            # Получение абсолютного пути к директории, где находится custom_requestor.py
            current_directory = os.path.dirname(os.path.abspath(__file__))

            # Определение абсолютного пути к лог-файлу
            log_file = os.path.join(current_directory, 'logs', 'requester.log')
            file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024 * 5, backupCount=5)
            file_handler.setFormatter(log_format)

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(log_format)

            # Add handlers to logger
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def log_request_and_response(self, method, url, data, response):
        self.logger.info(f"Sending {method} request to {url}\nHeaders: {self.session.headers}\nBody: {data}")
        response_data = response.json() if 'application/json' in response.headers.get('Content-Type', '') \
            else response.text
        self.logger.info(f"Response from {url}: {response.status_code}\n"
                         f"Headers: {response.headers}\nBody: {response_data}")
