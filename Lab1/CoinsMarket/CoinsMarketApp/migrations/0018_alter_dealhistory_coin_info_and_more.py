# Generated by Django 4.2.7 on 2023-11-25 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoinsMarketApp', '0017_balancehistory_coinhistory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealhistory',
            name='coin_info',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='dealhistory',
            name='operation_type',
            field=models.CharField(choices=[('B', 'Buy'), ('S', 'Sell')], max_length=1),
        ),
    ]
