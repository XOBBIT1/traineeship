from celery import shared_task
from src.carshop.celery import app
from src.profile.api.views.utils import Util
from src.provider.scripts.create_provider import create_provider_script


@shared_task
def create_provider():
    create_provider_script()
