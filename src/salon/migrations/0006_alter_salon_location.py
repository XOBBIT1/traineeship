# Generated by Django 3.2.9 on 2022-09-09 10:21

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("salon", "0005_alter_salon_name_client"),
    ]

    operations = [
        migrations.AlterField(
            model_name="salon",
            name="location",
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
