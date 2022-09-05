from django.contrib.auth.models import User
from django.db import models
from src.carshop.config.date_model_mixin import TimeStampMixin

class Salon(TimeStampMixin):
    name = models.CharField(max_length=256, null=False, blank=False)
    name_client = models.ForeignKey(
        User, related_name="client", on_delete=models.PROTECT, null=True
    )
    name_provider = models.ManyToManyField(
        "provider.Provider",
        related_name="provider_salon",
        null=True,  
        blank=True,
    )
    cars = models.ManyToManyField(
        "cars_details.CarsDetails",
        related_name="car",
        null=True,  
        blank=True,
    )
    location = models.CharField(max_length=256, null=False, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
