# Generated by Django 4.2.7 on 2023-11-25 00:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoinsMarketApp', '0009_alter_coin_currency_alter_coin_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='currency',
            field=models.CharField(choices=[('UAH', 'Hryvnia'), ('KP', 'Kopiyka'), ('USD', 'Dollar'), ('UC', 'USA Cent'), ('EUR', 'Euro'), ('EC', 'Eurocent'), ('CZK', 'Czech Koruna'), ('HL', 'Czech Heller'), ('PLN', 'Zloty'), ('GR', 'Grosz')], max_length=3),
        ),
        migrations.AlterField(
            model_name='coin',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='coin',
            name='diameter',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='coin',
            name='material',
            field=models.CharField(choices=[('S', 'Silver'), ('G', 'Gold'), ('N', 'Nickel'), ('A', 'Antimony'), ('B', 'Bronze'), ('C', 'Cupronickel'), ('Cp', 'Copper'), ('Br', 'Brass')], max_length=2),
        ),
        migrations.AlterField(
            model_name='coin',
            name='par',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='coin',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='coin',
            name='weight',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='coin',
            name='year',
            field=models.IntegerField(),
        ),
    ]
