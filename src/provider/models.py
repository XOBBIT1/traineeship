from src.carshop.config.date_model_mixin import TimeStampMixin
from src.salon.models import Salon
from django.db import models


class Provider(TimeStampMixin):
    name = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField("Description", blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    salons = models.ForeignKey(
        Salon,
        related_name="salons_provider",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)
