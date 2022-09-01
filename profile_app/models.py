from django.db import models
from .cars.models import Cars


class Profile(models.Model):
    name = models.TextField("Detail_name", blank=False, null=False)
    description = models.TextField("Description", blank=False, null=False)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    balance = models.IntegerField(requierd=True)
    cars = models.ManyToManyField(Cars, related_name='car', on_delete=models.PROTECT, null=True)
    is_active = models.BooleanField(default=True)