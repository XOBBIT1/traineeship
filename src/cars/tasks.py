from celery import shared_task
from src.carshop.celery import app
from src.profile.api.views.utils import Util
from src.cars.models import Cars
from src.salon.models import Salon
from src.cars.scripts.create_car import create_car_script, salon_buy_car_script


@shared_task
def create_car():
    create_car_script().delay(5)


@app.task
def profile_buy_car():
    pass


@app.task
def salon_buy_car():
    salon_buy_car_script()
