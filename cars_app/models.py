from django.db import models
from cars_details_app.models import Cars_details
from provider_app.models import Provider


class Cars(models.Model):
    name = models.TextField("Detail_name", blank=False, null=False)
    description = models.TextField("Description", blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    cars_details = models.ManyToManyField(Cars_details, related_name='cars_details_app', on_delete=models.PROTECT, null=True)
    prise = models.IntegerField(requierd=True)
    provider = models.ManyToManyField(Provider, related_name='provider_app', on_delete=models.PROTECT, null=True)
    is_active = models.BooleanField(default=True)