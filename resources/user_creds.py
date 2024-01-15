import os
from dotenv import load_dotenv


load_dotenv()

USERNAME = ''
PASSWORD = os.getenv('SUPER_USER_TOKEN')
