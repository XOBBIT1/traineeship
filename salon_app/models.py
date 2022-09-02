from django.contrib.auth.models import User
from django.db import models


class Salon(models.Model):
    name = models.TextField("Name", blank=False, null=False)
    name_client = models.ForeignKey(User, related_name='client', on_delete=models.PROTECT, null=True)
    name_provider = models.ForeignKey("provider_app.Provider", related_name='provider_salon', on_delete=models.PROTECT, null=True)
    cars_details = models.ForeignKey("cars_app.Cars", related_name='cars_details_app', on_delete=models.PROTECT, null=True)
    cars = models.ForeignKey("cars_details_app.Cars_details", related_name='car', on_delete=models.PROTECT, null=True)
    location = models.TextField("Описание", blank=False, null=False)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

