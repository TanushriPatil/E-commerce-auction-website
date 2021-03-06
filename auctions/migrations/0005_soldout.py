# Generated by Django 3.0.8 on 2020-09-11 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='soldOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('starting_price', models.IntegerField()),
                ('end_bid', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('busername', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bidderso', to=settings.AUTH_USER_MODEL)),
                ('ousername', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ownerso', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
