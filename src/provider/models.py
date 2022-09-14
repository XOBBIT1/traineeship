from src.carshop.config.date_model_mixin import TimeStampMixin
from django.db import models



class Provider(TimeStampMixin):
    name = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField("Description", blank=False, null=False)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    cars = models.ManyToManyField(
        "cars.Cars", related_name="car", null=True, blank=True
    )
    salons = models.ManyToManyField(
        "salon.Salon", related_name="salon", null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
