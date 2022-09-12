from django.db import models
from src.carshop.config.date_model_mixin import TimeStampMixin
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class Profile(TimeStampMixin, AbstractBaseUser):
    username = models.CharField(max_length=256, unique=True, null=False, blank=False)
    email = models.EmailField(
        max_length=256, unique=True, null=False, db_index=True, blank=False
    )
    description = models.TextField("Description", blank=False, null=False)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    cars = models.ManyToManyField("cars.Cars", related_name="car_profile", null=True)
    bio = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def tokens(self):
        return " "
