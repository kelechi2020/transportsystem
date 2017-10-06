from django.shortcuts import render

from reservations.models import Reservation


def page(request):
    my_reservation = Reservation.objects.filter(user=request.user.username)
    from pprint import pprint

    pprint(my_reservation)
    return render(request, 'user_reservation.html', {'my_reservation':my_reservation})