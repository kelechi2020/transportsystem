from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from reservations import forms
from reservations.models import Reservation, Bus, Route


def reserve_seatpage(request, route, bus, name):
    from pprint import pprint
    a = Reservation.objects.filter(destination=route)
    e = [any.seat_number for any in a]
    created_seats = Bus.objects.get(id=bus).bus_seats.values()
    available_seats = Bus.objects.get(id=bus).bus_seats.values().exclude(seat_number__in=e)
    remaining_seats = [ahr['seat_number'] for ahr in available_seats]
    remaining_seats_description = [ahr['seat_description']  for ahr in available_seats]
    select_options = zip(remaining_seats,remaining_seats_description)
    pprint(created_seats.count())
    pprint(available_seats.count())
    pprint(remaining_seats)
    pprint(request)
    return render(request, 'make_reservations.html', {'route': route ,'bus': bus, 'name': name, 'remaining_seats': remaining_seats, 'select_options': select_options})


def formsubmit(request):

    if request.POST:
        seat = request.POST.get('seat')
        route = request.POST.get('route')
        route_instance = Route.objects.get(id=route)
        reserve = Reservation.objects.create(destination=route_instance, seat_number=seat, user=request.user.username)
        reserve.save()
        return redirect('distinct-reservations')
    else:
        return render(request, 'make_reservations.html')


