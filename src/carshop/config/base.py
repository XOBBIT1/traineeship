import os
from pathlib import Path
from decouple import config 
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CUR_DIR = os.path.join(__file__)

dotenv_file = os.path.join(CUR_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

SECRET_KEY = config('SECRET_KEY')
DEBUG = "True"
ALLOWED_HOSTS = [
    "*"
]

ROOT_URLCONF = 'src.carshop.urls'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
