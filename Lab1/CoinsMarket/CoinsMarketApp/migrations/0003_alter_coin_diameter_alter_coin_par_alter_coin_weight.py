# Generated by Django 4.2.7 on 2023-11-23 23:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoinsMarketApp', '0002_coin_dealhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='diameter',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='coin',
            name='par',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='coin',
            name='weight',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]