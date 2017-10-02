from django.shortcuts import render
from .models import Customer, Seat, Route, Reservation, Bus


def page(request):
    route = Route.objects.all()
    from pprint import pprint
    pprint(route)
    return render(request, 'index.html', {'route': route})


def activeroutes(request):
    route = Route.objects.all()
    from pprint import pprint
    pprint(route)
    return render(request, 'active.html', {'route': route})
