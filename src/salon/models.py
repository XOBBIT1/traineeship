from src.carshop.config.date_model_mixin import TimeStampMixin
from src.profile.models import Profile
from django.contrib.auth.models import User
from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
from django_countries.fields import CountryField


class Salon(TimeStampMixin):
    name = models.CharField(max_length=256, null=False, blank=False)
    name_client = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="client",
        null=True,
        blank=True
    )
    location = CountryField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    is_active = models.BooleanField(default=True)
    balance = MoneyField(
        max_digits=10,
        null=True,
        blank=True,
        default_currency="USD",
        decimal_places=2,
        validators=[
            MinMoneyValidator(10),
            MaxMoneyValidator(1500),
            MinMoneyValidator(Money(500, 'NOK')),
            MaxMoneyValidator(Money(900, 'NOK')),
            MinMoneyValidator({'EUR': 100, 'USD': 50}),
            MaxMoneyValidator({'EUR': 1000, 'USD': 500}),
        ]
    )

    def __str__(self):
        return self.name
