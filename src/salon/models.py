from django.contrib.auth.models import User
from django.db import models
# from djmoney.models.fields import MoneyField
# from djmoney.money import Money
# from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
from django_countries.fields import CountryField
from src.carshop.config.date_model_mixin import TimeStampMixin


class Salon(TimeStampMixin):
    name = models.CharField(max_length=256, null=False, blank=False)
    name_client = models.ManyToManyField(
        "profile.Profile", related_name="client", null=True, blank=True
    )
    name_provider = models.ManyToManyField(
        "provider.Provider",
        related_name="provider_salon",
        null=True,
        blank=True,
    )
    car = models.ManyToManyField(
        "cars.Cars",
        related_name="car",
        null=True,
        blank=True,
    )
    location = CountryField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    is_active = models.BooleanField(default=True)
    # balance = MoneyField(
    #     max_digits=10,
    #     decimal_places=2,
    #     validators=[
    #         MinMoneyValidator(10),
    #         MaxMoneyValidator(1500),
    #         MinMoneyValidator(Money(500, 'NOK')),
    #         MaxMoneyValidator(Money(900, 'NOK')),
    #         MinMoneyValidator({'EUR': 100, 'USD': 50}),
    #         MaxMoneyValidator({'EUR': 1000, 'USD': 500}),
    #     ]
    # )

    def __str__(self):
        return self.name
