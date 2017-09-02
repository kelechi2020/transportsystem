from django.contrib import admin
from .models import Reservation, Seat, Customer, Bus, Route
# Register your models here.
admin.site.register(Reservation)
admin.site.register(Seat)
admin.site.register(Customer)
admin.site.register(Bus)
admin.site.register(Route)