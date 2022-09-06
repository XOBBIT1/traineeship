from django.db import models


class Provider(models.Model):
    name = models.TextField("Name", blank=False, null=False)
    description = models.TextField("Description", blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    cars = models.ForeignKey("cars_app.Cars", related_name='car',on_delete=models.PROTECT, null=True)
    salons = models.ForeignKey("salon_app.Salon", related_name='salon_app', on_delete=models.PROTECT, null=True)
    is_active = models.BooleanField(default=True)