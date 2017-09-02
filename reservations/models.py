import os
import uuid
from django.utils.timezone import now as timezone_now
from django.db import models
from utils.models import CreationModificationDateMixin

TYPE_CHOICES = (
        ('o+', "O+"),
        ('A+', "A+")
    )

def upload_to(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    return "quotes/%s%s" % (now.strftime("%Y/%m/%Y%m%d%H%M%S"), filename_ext.lower(),)


class Customer(models.Model):

    name = models.CharField(max_length=55, verbose_name="Customer Name")
    email = models.EmailField(max_length=75, verbose_name="Email")
    phone = models.CharField(max_length=14, verbose_name="Contact")
    address = models.CharField(max_length=150, verbose_name="Address", blank=True)
    blood_group = models.CharField(max_length=50, choices=TYPE_CHOICES)


class Bus(models.Model):
    bus_plate_number = models.CharField(max_length=60, verbose_name="Registration Number")
    colour = models.CharField(max_length=50, verbose_name="Bus Colour")
    engine_number = models.CharField(max_length=50, verbose_name="Engine Number")
    bus_image = models.ImageField(verbose_name="Bus Image", upload_to=upload_to)


class Route(CreationModificationDateMixin):
    route_name = models.CharField(max_length=200, verbose_name="PICK ROUTE")
    route_description = models.CharField(verbose_name="Route Description", max_length=150)
    price = models.IntegerField(verbose_name="Price")
    stop_point = models.CharField(verbose_name="Stop Point 1", max_length=150)
    stop_point1 = models.CharField(verbose_name="Stop Point 2", max_length=150)
    stop_point2 = models.CharField(verbose_name="Stop Point 3", max_length=150, blank=True)
    stop_point3 = models.CharField(verbose_name="Stop Point 4", max_length=150, blank=True)
    stop_point4 = models.CharField(verbose_name="Stop Point 5", max_length=150, blank=True)
    status = models.BooleanField(verbose_name="Route Status")
    bus = models.OneToOneField(Bus, verbose_name="Going Bus")
    departure_time = models.DateTimeField(verbose_name="Departure Time")


class Seat(models.Model):
    seat_number = models.IntegerField(verbose_name="SEAT NUMBER")
    seat_description = models.CharField(verbose_name="SEAT DESCRIPTION", max_length=50)
    bus_seat = models.OneToOneField(Bus, verbose_name="Bus")


class Reservation(CreationModificationDateMixin):
    reservation_number = models.UUIDField(default=uuid.uuid4, editable=False)
    destination = models.ForeignKey(Route, verbose_name="Select A Route")
    seat_number = models.OneToOneField(Seat, verbose_name="PICK A SEAT")

    def __str__(self):
        return str(self.reservation_number)
