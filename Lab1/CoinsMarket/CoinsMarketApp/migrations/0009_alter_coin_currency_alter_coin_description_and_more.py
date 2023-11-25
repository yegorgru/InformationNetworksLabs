# Generated by Django 4.2.7 on 2023-11-24 21:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoinsMarketApp', '0008_alter_coin_image_obverse_alter_coin_image_reverse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='currency',
            field=models.CharField(blank=True, choices=[('UAH', 'Hryvnia'), ('KP', 'Kopiyka'), ('USD', 'Dollar'), ('UC', 'USA Cent'), ('EUR', 'Euro'), ('EC', 'Eurocent'), ('CZK', 'Czech Koruna'), ('HL', 'Czech Heller'), ('PLN', 'Zloty'), ('GR', 'Grosz')], max_length=3),
        ),
        migrations.AlterField(
            model_name='coin',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='coin',
            name='diameter',
            field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='coin',
            name='image_obverse',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='coin',
            name='image_reverse',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='coin',
            name='material',
            field=models.CharField(blank=True, choices=[('S', 'Silver'), ('G', 'Gold'), ('N', 'Nickel'), ('A', 'Antimony'), ('B', 'Bronze'), ('C', 'Cupronickel'), ('Cp', 'Copper'), ('Br', 'Brass')], max_length=2),
        ),
        migrations.AlterField(
            model_name='coin',
            name='par',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='coin',
            name='price',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='coin',
            name='weight',
            field=models.FloatField(blank=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='coin',
            name='year',
            field=models.IntegerField(blank=True),
        ),
    ]
