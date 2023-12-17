# Определение рабочей директории и переменных окружения
cd .. || exit

# Получение текущей директории и экспорт IP-адресов
teamcity_tests_directory="$(pwd)"
export ips
ips=$(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')
export ip=${ips%%$'\n'*}
echo "Current IP: $ip"

# Инициализация переменных и директорий
workdir="teamcity_tests_infrastructure"
teamcity_server_workdir="teamcity_server"
teamcity_agent_workdir="teamcity_agent"
teamcity_server_container_name="teamcity-server-instance"
teamcity_agent_container_name="teamcity_agent_instance"

# Удаление и создание новых директорий
cd infra || exit
echo "Deleting all containers"
rm -rf $workdir
mkdir $workdir
cd $workdir || exit
mkdir $teamcity_server_workdir $teamcity_agent_workdir

# Запуск TeamCity Server и Agent
docker stop $teamcity_server_container_name $teamcity_agent_container_name
docker rm $teamcity_server_container_name $teamcity_agent_container_name
docker run -d --name $teamcity_server_container_name -v "$(pwd)"/logs:/opt/teamcity/logs -p 8111:8111 jetbrains/teamcity-server
docker run -d --name $teamcity_agent_container_name -e SERVER_URL="http://$ip:8111" -v "$(pwd)"/conf:/data/teamcity_agent/conf jetbrains/teamcity-agent

# Установка Python зависимостей
pip install -r "$teamcity_tests_directory"/requirements.txt

# Установка и запуск Playwright
playwright install

# Запуск тестов с pytest и создание Allure отчетов
pytest -v --alluredir="$teamcity_tests_directory"/results

# Запуск Allure Report сервера в Docker
docker run -d -p 5050:5050 -v "$teamcity_tests_directory"/results:/allure-report frankescobar/allure-docker-service

echo "Allure Report is available at http://$ip:5050"
