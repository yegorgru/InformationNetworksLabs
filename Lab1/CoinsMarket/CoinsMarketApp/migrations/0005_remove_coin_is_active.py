# Generated by Django 4.2.7 on 2023-11-23 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoinsMarketApp', '0004_dealhistory_date_time_dealhistory_is_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coin',
            name='is_active',
        ),
    ]
