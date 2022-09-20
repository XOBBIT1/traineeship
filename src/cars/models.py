from src.provider.models import Provider
from src.profile.models import Profile
from src.salon.models import Salon
from django.db import models
from djmoney.models.fields import MoneyField
from src.carshop.config.date_model_mixin import TimeStampMixin
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class Cars(TimeStampMixin):
    name = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField("Description", blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    cars_details = models.ManyToManyField(
        "cars_details.CarsDetails", related_name="cars_details", null=True, blank=True
    )
    provider = models.ForeignKey(
        Provider, related_name="cars_provider", on_delete=models.CASCADE, null=True, blank=True
    )
    salon = models.ForeignKey(
        Salon, related_name="cars_salon", on_delete=models.CASCADE, null=True, blank=True
    )
    profile = models.ForeignKey(
        Profile, related_name="cars_profile", on_delete=models.CASCADE, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    price = MoneyField(
        max_digits=19, decimal_places=4, null=True, blank=True, default_currency="USD"
    )
