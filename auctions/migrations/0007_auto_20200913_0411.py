# Generated by Django 3.0.8 on 2020-09-13 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20200911_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldout',
            name='category',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AddField(
            model_name='soldout',
            name='pic_url',
            field=models.CharField(blank=True, max_length=600),
        ),
        migrations.AddField(
            model_name='soldout',
            name='title',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
