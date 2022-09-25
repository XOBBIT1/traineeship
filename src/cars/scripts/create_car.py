import random
from src.cars.models import Cars
from src.provider.models import Provider
from core.data import cars_models, random_cars_models, random_description, random_year


def create_car_script():
    car_for_dealer = Cars.objects.create(
        name=random_cars_models(),
        description=random_description(),
        created_at=random_year(),
        price=random.randint(5000, 15000),
        provider=random.choice(Provider.objects.all()),
    )


def salon_buy_car():
    pass