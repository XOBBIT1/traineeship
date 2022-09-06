from django.db import models


class Cars_details(models.Model):
    name = models.TextField("Detail_name", blank=False, null=False)
    description = models.TextField("Description", blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    cars = models.ForeignKey("cars_app.Cars", related_name='car_for_details', on_delete=models.PROTECT, null=True)
    is_active = models.BooleanField(default=True)