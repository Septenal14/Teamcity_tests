# Автотестовый Фреймворк

Данный фреймворк предназначен для автоматизации тестирования Teamcity. Ниже приведена инструкция по его использованию и краткое описание ключевых директорий.

## Инструкция по запуску

1. Установите необходимые зависимости, выполнив следующую команду:

   ```shell
   pip install -r requirements.txt

2. Установите Playwright:

   ```shell
   playwright install

3. Запустите тесты, выполнив команду:

    ```shell
    pytest

## Ключевые директории

- **custom_requester**: В этой директории находится  `CustomRequester.py` , который предоставляет возможность отправки HTTP-запросов к Teamcity API и логирования действий. Он использует библиотеку `requests` для взаимодействия с API.

- **api**: В этой директории находятся модули для взаимодействия с API, например, `auth_api.py` и `project_api.py`.

- **data**: Здесь хранятся файлы или классы, предоставляющие тестовые данные. Например, `project_data.py` содержит данные для создания проектов.

- **enums**: В данной директории находятся файлы с перечислениями и константами, такие как `host.py` с базовым URL и `status_codes.py` с определением статус-кодов.

- **tests**: Эта директория предназначена для хранения автотестов. Файлы, содержащие тесты, должны иметь префикс `test_`, например, `test_create_build.py`.

- **logs**: Здесь хранятся логи тестов. Для каждого теста будет создан лог-файл `requester.log` в этой директории.

- **utils**: В этой директории размещаются вспомогательные модули или классы, которые могут быть использованы в тестах.



