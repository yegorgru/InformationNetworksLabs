# Generated by Django 4.2.7 on 2023-11-23 23:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoinsMarketApp', '0005_remove_coin_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]