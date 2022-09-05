from django.db import models
from src.carshop.config.date_model_mixin import TimeStampMixin


class Profile(TimeStampMixin):
    name =models.CharField(
        max_length=256,
        null=False,
        blank=False)

    description = models.TextField(
        "Description",
        blank=False,
        null=False
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="images/"
    )
    cars = models.ForeignKey(
        "cars.Cars",
        related_name='car_profile',
        on_delete=models.PROTECT,
        null=True
    )
    is_active = models.BooleanField(default=True)