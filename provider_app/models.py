from django.db import models
from .cars.models import Cars
from .salon.models import Salon


class Provider(models.Model):
    name = models.TextField("Name", blank=False, null=False)
    description = models.TextField("Description", blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    cars = models.ManyToManyField(Cars, related_name='car', on_delete=models.PROTECT, null=True)
    salons = models.ManyToManyField(Salon, related_name='salon_app', on_delete=models.PROTECT, null=True)
    is_active = models.BooleanField(default=True)