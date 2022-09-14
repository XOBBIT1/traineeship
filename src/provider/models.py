from django.db import models
from src.carshop.config.date_model_mixin import TimeStampMixin


class Provider(TimeStampMixin):
    name = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField("Description", blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    cars = models.ManyToManyField(
        "cars.Cars", related_name="car", null=True, blank=True
    )
    salons = models.ManyToManyField(
        "salon.Salon", related_name="salon", null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
