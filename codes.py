from reservations.models import Route, Reservation, Bus, Customer, Seat
a = Reservation.objects.all()
b = [c.seat_number for c in a]
e = [r.all() for r in b ]
r = Route.objects.all()
for any in b :
    seats = Seat.objects.all().exclude(seat_number=any)



