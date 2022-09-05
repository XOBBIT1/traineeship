# Generated by Django 3.2.9 on 2022-09-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('color', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('car_brand', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
                ('cars', models.ManyToManyField(blank=True, null=True, related_name='car_for_details', to='cars.Cars')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
