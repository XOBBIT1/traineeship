from django.db import models
from src.carshop.config.date_model_mixin import TimeStampMixin


class CarsDetails(TimeStampMixin):
    name = models.CharField(
        max_length=256,
        null=False,
        blank=False
    )
    description = models.TextField(
        "Description",
        blank=True,
        null=True
    )
    color = image = models.ImageField(
        null=True,
        blank=True,
        upload_to="images/"
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="images/"
    )
    cars = models.ManyToManyField(
        "cars.Cars",
        related_name='car_for_details',
        null=True,  
        blank=True
    )
    car_brand = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
    is_active = models.BooleanField(default=True)
