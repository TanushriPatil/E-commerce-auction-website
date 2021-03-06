# Generated by Django 3.0.8 on 2020-09-17 09:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_watchlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='soldout',
            old_name='pic_url',
            new_name='photo_url',
        ),
        migrations.RenameField(
            model_name='soldout',
            old_name='start_date',
            new_name='post_date',
        ),
        migrations.RenameField(
            model_name='soldout',
            old_name='starting_price',
            new_name='starting_bid',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='category',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='photo_url',
            field=models.CharField(blank=True, max_length=600),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='starting_bid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlist',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
