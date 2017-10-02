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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('bus_plate_number', models.CharField(max_length=60, verbose_name='Registration Number')),
                ('colour', models.CharField(max_length=50, verbose_name='Bus Colour')),
                ('engine_number', models.CharField(max_length=50, verbose_name='Engine Number')),
                ('bus_image', models.ImageField(upload_to=reservations.models.upload_to, verbose_name='Bus Image')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=55, verbose_name='Customer Name')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
                ('phone', models.CharField(max_length=14, verbose_name='Contact')),
                ('address', models.CharField(max_length=150, verbose_name='Address', blank=True)),
                ('blood_group', models.CharField(max_length=50, choices=[('o+', 'O+'), ('A+', 'A+')])),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(verbose_name='creation date and time', editable=False)),
                ('modified', models.DateTimeField(verbose_name='modification date and time', editable=False, null=True)),
                ('reservation_number', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('seat_number', models.IntegerField(verbose_name='PICK A SEAT', null=True)),
                ('car_class', models.CharField(max_length=200, verbose_name='CAR Class', blank=True)),
                ('car_plate_num', models.CharField(max_length=200, verbose_name='CAR Plate Num', blank=True)),
                ('car_type', models.CharField(max_length=200, verbose_name='CAR TYPE', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(verbose_name='creation date and time', editable=False)),
                ('modified', models.DateTimeField(verbose_name='modification date and time', editable=False, null=True)),
                ('route_name', models.CharField(max_length=200, verbose_name='PICK ROUTE')),
                ('route_description', models.CharField(max_length=150, verbose_name='Route Description')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('stop_point', models.CharField(max_length=150, verbose_name='Stop Point 1')),
                ('stop_point1', models.CharField(max_length=150, verbose_name='Stop Point 2')),
                ('stop_point2', models.CharField(max_length=150, verbose_name='Stop Point 3', blank=True)),
                ('stop_point3', models.CharField(max_length=150, verbose_name='Stop Point 4', blank=True)),
                ('stop_point4', models.CharField(max_length=150, verbose_name='Stop Point 5', blank=True)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('seat_number', models.IntegerField(verbose_name='SEAT NUMBER')),
                ('car_type', models.CharField(default=None, verbose_name='CAR TYPE', blank=True, max_length=200)),
                ('seat_description', models.CharField(max_length=50, verbose_name='SEAT DESCRIPTION')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='destination',
            field=models.ForeignKey(to='reservations.Route', verbose_name='Select A Route'),
        ),
        migrations.AddField(
            model_name='bus',
            name='bus_seats',
            field=models.ManyToManyField(to='reservations.Seat', db_constraint='Add Seats To Bus'),
        ),
    ]
