# Generated by Django 3.0.8 on 2020-09-10 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_remove_bids_bid_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='bid_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
