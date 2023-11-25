from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime


class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    balance = models.IntegerField()


class Coin(models.Model):
    CURRENCY = [
        ("UAH", "Hryvnia"),
        ("KP", "Kopiyka"),
        ("USD", "Dollar"),
        ("UC", "USA Cent"),
        ("EUR", "Euro"),
        ("EC", "Eurocent"),
        ("CZK", "Czech Koruna"),
        ("HL", "Czech Heller"),
        ("PLN", "Zloty"),
        ("GR", "Grosz"),
    ]
    MATERIAL = [
        ("S", "Silver"),
        ("G", "Gold"),
        ("N", "Nickel"),
        ("A", "Antimony"),
        ("B", "Bronze"),
        ("C", "Cupronickel"),
        ("Cp", "Copper"),
        ("Br", "Brass"),
    ]
    owner = models.IntegerField()
    par = models.IntegerField(validators=[MinValueValidator(1)], blank=True)
    currency = models.CharField(max_length=3, choices=CURRENCY, blank=True)
    year = models.IntegerField(blank=True)
    material = models.CharField(max_length=2, choices=MATERIAL, blank=True)
    weight = models.FloatField(validators=[MinValueValidator(0)], blank=True)
    diameter = models.FloatField(validators=[MinValueValidator(0)], blank=True)
    price = models.IntegerField(validators=[MinValueValidator(1)], blank=True)
    description = models.CharField(max_length=200, blank=True)
    image_obverse = models.ImageField(upload_to='uploads/', blank=True)
    image_reverse = models.ImageField(upload_to='uploads/', blank=True)


class DealHistory(models.Model):
    lhs = models.IntegerField()
    rhs = models.IntegerField()
    coin = models.ForeignKey("Coin", on_delete=models.CASCADE)
    price = models.IntegerField()
    is_finished = models.BooleanField(default=False)
    date_time = models.DateTimeField(blank=True, default=datetime.now)
