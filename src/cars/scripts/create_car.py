import random
from src.cars.models import Cars
from src.provider.models import Provider
from src.salon.models import Salon
from django.db import transaction
from core.data import cars_models, random_cars_models, random_description, random_year


def create_car_script():
    try:
        Cars.objects.create(
            name=random_cars_models(),
            description=random_description(),
            created_at=random_year(),
            price=random.randint(5000, 15000),
            provider=random.choice(Provider.objects.all()),
        )
    except Exception as e:
        raise e


def salon_buy_car_script():
    get_car = Cars.objects.all()
    get_salon = Salon.objects.all()

    if get_car.price <= get_salon.balance:

        get_salon.balance -= get_car.price
        with transaction.atomic():
            Cars.objects.all().get(id=car.id).update(col = F('col') + price)
            Salon.objects.get(id).update(car_count=F("car_count") + count_car_rand)

    else:
        raise Exception("You don't have enough money")
