from django.db import models
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
    provider = models.ManyToManyField(
        "provider.Provider", related_name="provider", null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
