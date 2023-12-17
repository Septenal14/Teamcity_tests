import os
from enum import Enum
from dotenv import load_dotenv


load_dotenv()


class UserCreds(Enum):
    EMAIL = os.getenv('USER_EMAIL')
    PASSWORD = os.getenv('USER_PASSWORD')
