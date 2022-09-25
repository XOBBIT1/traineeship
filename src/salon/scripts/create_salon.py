from src.salon.models import Salon
from src.provider.models import Provider
from src.profile.models import Profile
import random
from core.data import random_salon_name, random_cars_models, random_description, random_location


def create_salon_script():
    car_for_dealer = Salon.objects.create(name=random_salon_name(),
                                          name_client=random.choice(Profile.objects.all()),
                                          location=random_location(),
                                          balance=random.randint(15000, 20000),
                                          )

