# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import reservations.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('bus_plate_number', models.CharField(max_length=60, verbose_name='Registration Number')),
                ('colour', models.CharField(max_length=50, verbose_name='Bus Colour')),
                ('engine_number', models.CharField(max_length=50, verbose_name='Engine Number')),
                ('bus_image', models.ImageField(upload_to=reservations.models.upload_to, verbose_name='Bus Image')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Customer Name')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
                ('phone', models.CharField(max_length=14, verbose_name='Contact')),
                ('Address', models.CharField(blank=True, max_length=150, verbose_name='Address')),
                ('blood_group', models.CharField(max_length=50, choices=[('o+', 'O+'), ('A+', 'A+')])),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, verbose_name='creation date and time')),
                ('modified', models.DateTimeField(null=True, editable=False, verbose_name='modification date and time')),
                ('reservation_number', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, verbose_name='creation date and time')),
                ('modified', models.DateTimeField(null=True, editable=False, verbose_name='modification date and time')),
                ('route_name', models.CharField(max_length=200, verbose_name='PICK ROUTE')),
                ('route_description', models.CharField(max_length=150, verbose_name='Route Description')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('stop_point', models.CharField(max_length=150, verbose_name='Stop Point 1')),
                ('stop_point1', models.CharField(max_length=150, verbose_name='Stop Point 2')),
                ('stop_point2', models.CharField(blank=True, max_length=150, verbose_name='Stop Point 3')),
                ('stop_point3', models.CharField(blank=True, max_length=150, verbose_name='Stop Point 4')),
                ('stop_point4', models.CharField(blank=True, max_length=150, verbose_name='Stop Point 5')),
                ('status', models.BooleanField(verbose_name='Route Status')),
                ('departure_time', models.DateTimeField(verbose_name='Departure Time')),
                ('bus', models.OneToOneField(to='reservations.Bus', verbose_name='Going Bus')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('seat_number', models.IntegerField(verbose_name='SEAT NUMBER')),
                ('seat_description', models.CharField(max_length=50, verbose_name='SEAT DESCRIPTION')),
                ('bus_seat', models.OneToOneField(to='reservations.Bus', verbose_name='Bus')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='destination',
            field=models.ForeignKey(to='reservations.Route'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='seat_number',
            field=models.OneToOneField(to='reservations.Seat', verbose_name='PICK A SEAT'),
        ),
    ]
