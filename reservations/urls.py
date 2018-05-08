from django.conf.urls import  url

from reservations.view.printticket import print_ticket
from reservations.view.reserve_seat import reserve_seatpage, formsubmit, check_get_seat_availabilty_and_chart
from reservations.views import activeroutes
from .view.register_modal import SmilesView
from .view.login_modal import LoginView


urlpatterns = [
    url(r'new-user', SmilesView.as_view(), name='register'),
    url(r'login-user', LoginView.as_view(), name='login'),
    url(r'^localgov/(?P<route>\d+)/(?P<bus>\d+)/(?P<name>[^/]+)$', reserve_seatpage, name='reserve'),
    url(r'^form_submit$', formsubmit, name='book'),
    url(r'^active-route$', activeroutes, name='route'),
    url(r'^(?P<reservation_id>\d+)/$', print_ticket, name="print_ticket"),

    #url(r'create-reservation',CreateReservation.as_view(), name='reserve')
]