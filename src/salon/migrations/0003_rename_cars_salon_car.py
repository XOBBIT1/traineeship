# Generated by Django 3.2.9 on 2022-09-08 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("salon", "0002_auto_20220908_1130"),
    ]

    operations = [
        migrations.RenameField(
            model_name="salon",
            old_name="cars",
            new_name="car",
        ),
    ]
