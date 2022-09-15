from django.contrib.auth.models import User
from django.db import models
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
        "cars_details.CarsDetails",
        related_name="car",
        null=True,
        blank=True,
    )
    location = CountryField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
