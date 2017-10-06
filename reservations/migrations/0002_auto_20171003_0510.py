# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.CharField(verbose_name='Reservation Owner', default='Admin', max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='blood_group',
            field=models.CharField(choices=[('o+', 'O+'), ('A+', 'A+'), ('abia state', 1)], max_length=50),
        ),
    ]
