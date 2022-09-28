# Generated by Django 3.2.9 on 2022-09-25 18:38

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0006_auto_20220925_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salon',
            name='balance',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
