# Generated by Django 3.2.9 on 2022-09-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0002_cars_cars_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(verbose_name='Description')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('is_active', models.BooleanField(default=True)),
                ('cars', models.ManyToManyField(blank=True, null=True, related_name='car', to='cars.Cars')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
