
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Color",
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
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CarsDetails",
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
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("car_brand", models.CharField(max_length=200)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "cars",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="car_for_details",
                        to="cars.Cars",
                    ),
                ),
                (
                    "color",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="car_color",
                        to="cars_details.Color",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
