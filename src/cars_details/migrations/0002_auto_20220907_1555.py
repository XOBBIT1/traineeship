# Generated by Django 3.2.9 on 2022-09-07 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars_details", "0001_initial"),
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
        migrations.RemoveField(
            model_name="carsdetails",
            name="color",
        ),
        migrations.AddField(
            model_name="carsdetails",
            name="color",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="car_color", to="cars_details.Color"
            ),
        ),
    ]
