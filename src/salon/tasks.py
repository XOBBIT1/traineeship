from celery import shared_task
from src.carshop.celery import app
from src.profile.api.views.utils import Util
from src.salon.models import Salon
from src.salon.scripts.create_salon import create_salon_script


@shared_task
def create_salon():
    create_salon_script()
