# Generated by Django 3.2.9 on 2022-09-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars_details', '0001_initial'),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='cars_details',
            field=models.ManyToManyField(blank=True, null=True, related_name='cars_details', to='cars_details.CarsDetails'),
        ),
    ]
