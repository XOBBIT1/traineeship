from django.contrib.auth.models import User
from django.db import models
from cars_details_app.models import Cars_details
from cars_app.models import Cars
from provider_app.models import Provider


class Salon(models.Model):
    name = models.TextField("Name", blank=False, null=False)
    name_client = models.ForeignKey(User, related_name='client', on_delete=models.PROTECT, null=True)
    name_provider = models.ManyToManyField(Provider, related_name='provider_app ', on_delete=models.PROTECT, null=True)
    cars_details = models.ManyToManyField(Cars_details, related_name='cars_details_app', on_delete=models.PROTECT, null=True)
    cars = models.ManyToManyField(Cars, related_name='car', on_delete=models.PROTECT, null=True)
    location = models.TextField("Описание", blank=False, null=False)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    is_active = models.BooleanField(default=True)
    balance = models.IntegerField(requierd=True)

    def __str__(self):
        return self.name

