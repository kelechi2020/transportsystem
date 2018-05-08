import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from reservations.buisness_logic.seat_chart_diagram import seat_chart as seat_charts
from reservations.models import Reservation, Bus, Route


def reserve_seatpage(request, route, bus, name):
    a = Reservation.objects.filter(destination=route).values('seat_number')
    bus_object = Bus.objects.get(id=bus)
    available_seats = bus_object.bus_seats.values('seat_number', 'seat_description').exclude(seat_number__in=a)
    car_chart_name = bus_object.seat_chart.car_type
    car_chart = json.dumps(seat_charts[car_chart_name])

    remaining_seats = [[ahr['seat_number'], ahr['seat_description']] for ahr in available_seats]
    if request.POST:
        pass
    else:
        pass
    return render(request, 'reservations/reserve_seat_chart_toyota.html', {'route': route, 'car_chart': car_chart, 'bus': bus, 'name': name, 'remaining_seats': remaining_seats, })
    # return render(request, 'make_reservations.html', {'route': route, 'bus': bus, 'name': name, 'remaining_seats': remaining_seats, 'select_options': remaining_seats})


def check_get_seat_availabilty_and_chart(request,route):
    """
    Gets available seats for a particular route and update chart with it.
    """
    booked_seats = Reservation.objects.filter(destination=route).values('seat_number')
    route_instance = get_object_or_404(Route, id=route)
    seat_chart_list = [seat_charts[route_instance.bus.seat_chart.car_type][str(seat['seat_number'])] for seat in booked_seats]
    return JsonResponse(seat_chart_list, safe=False)


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


def book_ticket_chart(request):

    return render(request, 'reservations/reserve_seat_chart_toyota.html')



@csrf_exempt
def make_reserve_ajax(request, route):
    data = dict()
    already_booked = []
    booked_successful = []
    price_list = []

    booked_seats = Reservation.objects.filter(destination=route).values('seat_number')
    for an in json.loads(request.POST['data']):
        if an in [seat['seat_number'] for seat in booked_seats]:
            already_booked.append(str(an))
        else:
            route_instance = Route.objects.get(id=route)
            Reservation.objects.create(destination=route_instance, seat_number=an, user=request.user.username)
            booked_successful.append(str(an))
            price_list.append(route_instance.price)

    booked_successful_list = ' ,'.join(booked_successful)
    already_booked_list = '  ,'.join(already_booked)
    ammount_payable = sum(price_list)
    print(ammount_payable)
    data['already_booked'] = "The following seat {0} has already been booked".format(already_booked_list)
    data['message'] = "This following seat {0} was booked successfully".format(booked_successful_list)
    data['ammount_payable'] = ammount_payable
    return JsonResponse(data)
