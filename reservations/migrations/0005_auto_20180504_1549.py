# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-04 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_auto_20180503_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='seat_chart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reservations.SeatChart'),
        ),
    ]
