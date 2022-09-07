# Generated by Django 3.2.9 on 2022-09-07 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cars_details", "0001_initial"),
        ("provider", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Salon",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=256)),
                ("location", models.CharField(max_length=256)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "cars",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="car",
                        to="cars_details.CarsDetails",
                    ),
                ),
                (
                    "name_client",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="client",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "name_provider",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="provider_salon",
                        to="provider.Provider",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]