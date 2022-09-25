import random
from src.provider.models import Provider
from src.salon.models import Salon
from core.data import random_name, random_year, random_description_provider


def create_provider_script():
    provider = Provider.objects.create(
        name=random_name(),
        description=random_description_provider(),
        date=random_year,
        salons=random.choice(Salon.objects.all()),
    )

