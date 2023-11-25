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
    par = models.IntegerField(validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY)
    year = models.IntegerField()
    material = models.CharField(max_length=2, choices=MATERIAL, null=True)
    weight = models.FloatField(validators=[MinValueValidator(0)], null=True)
    diameter = models.FloatField(validators=[MinValueValidator(0)], null=True)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    description = models.CharField(max_length=200, null=True)
    image_obverse = models.ImageField(upload_to='uploads/', null=True)
    image_reverse = models.ImageField(upload_to='uploads/', null=True)


class BaseHistory(models.Model):
    date_time = models.DateTimeField(blank=True, default=datetime.now)

    class Meta:
        abstract = True


class DealHistory(BaseHistory):
    DEAL_TYPE = [
        ("B", "Buy"),
        ("S", "Sell"),
    ]
    user = models.IntegerField()
    rhs = models.CharField(max_length=30)
    operation_type = models.CharField(max_length=1, choices=DEAL_TYPE)
    coin_info = models.CharField(max_length=30)
    price = models.IntegerField()


class BalanceHistory(BaseHistory):
    OPERATION_TYPE = [
        ("A", "Add"),
        ("W", "Withdraw"),
    ]
    user = models.IntegerField()
    operation_type = models.CharField(max_length=1, choices=OPERATION_TYPE)
    amount = models.IntegerField()
    balance = models.IntegerField()


class CoinHistory(BaseHistory):
    OPERATION_TYPE = [
        ("A", "Add"),
        ("E", "Edit"),
        ("D", "Delete"),
    ]
    user = models.IntegerField()
    operation_type = models.CharField(max_length=1, choices=OPERATION_TYPE)
    coin_info = models.CharField(max_length=30)
