import logging
import os
from enums.hosts import BASE_URL
from http import HTTPStatus
from enums.colors import GREEN, RED, RESET


class CustomRequester:
    base_headers = dict({"Content-Type": "application/json", "Accept": "application/json"})

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.base_url = BASE_URL

    def send_request(self, method, endpoint, data=None, expected_status=HTTPStatus.OK, need_logging=True):
        """
        Враппер для запросов. Позволяет прикручивать различную логику

        :param method: Метод запроса
        :param endpoint: Эндпоинт для склейки с BASE_URL в переменной "url"
        :param data: Тело запроса. По умолчанию пустое, чтобы пропускало NO_CONTENT ответы
        :param expected_status: Ожидаемый статус ответа. Если ожидается иной от SC_OK - передать в методе api-класса
        :param need_logging: Передача флага для логгирования. По умолчанию = True
        :return: Возвращает объект ответа
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, json=data)

        if need_logging:
            self.log_request_and_response(response)
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}")

        return response

    def _update_session_headers(self, **kwargs):
        """
        Принимает на вход словарь ключ-значений
        Обновляет заголовки сессии
        """
        self.headers = self.base_headers.copy()
        self.headers.update(kwargs)
        self.session.headers.update(self.headers)

    def log_request_and_response(self, response):
        """
        Логгирование запросов и ответов. Настройки логгирования описаны в pytest.ini
        Преобразует вывод в curl-like (-H хэдэеры), (-d тело)

        :param response: Объект response получаемый из метода "send_request"
        """
        try:
            request = response.request
            headers = " \\\n".join([f"-H '{header}: {value}'" for header, value in request.headers.items()])
            full_test_name = f"pytest {os.environ.get('PYTEST_CURRENT_TEST', '').replace(' (call)', '')}"

            body = ""
            if hasattr(request, 'body') and request.body is not None:
                if isinstance(request.body, bytes):
                    body = request.body.decode('utf-8')
                body = f"-d '{body}' \n" if body != '{}' else ''

            self.logger.info(
                f"{GREEN}{full_test_name}{RESET}\n"
                f"curl -X {request.method} '{request.url}' \\\n"
                f"{headers} \\\n"
                f"{body}"
            )

            response_status = response.status_code
            is_success = response.ok
            response_data = response.text
            if not is_success:
                self.logger.info(f"\tRESPONSE:"
                                 f"\nSTATUS_CODE: {RED}{response_status}{RESET}"
                                 f"\nDATA: {RED}{response_data}{RESET}")
        except Exception as e:
            self.logger.info(f"\nLogging went wrong: {type(e)} - {e}")
