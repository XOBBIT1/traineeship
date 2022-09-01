from django.db import models


class Profile(models.Model):
    name = models.TextField("Detail_name", blank=False, null=False)
    description = models.TextField("Description", blank=False, null=False)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    cars = models.ForeignKey("cars_app.Cars", related_name='car_profile', on_delete=models.PROTECT, null=True)
    is_active = models.BooleanField(default=True)