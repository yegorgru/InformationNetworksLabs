from django.db import models


class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    balance = models.IntegerField()
