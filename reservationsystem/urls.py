from django.conf.urls import include, url
from django.contrib import admin
from reservations.view.login_modal import LoginAgain

from django.contrib.auth import authenticate

from reservations.view.logout import logoutpage
from reservations.view.reserve_seat import book_ticket_chart, make_reserve_ajax, check_get_seat_availabilty_and_chart
from reservations.view.user_reservation import user_reservationpage
from reservations.views import reservationsviewspage, reservationsviewslogpage
import debug_toolbar
urlpatterns = [
    # Examples:
    # url(r'^$', 'reservationsystem.view.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^modal/', include('reservations.urls')),
    url(r'^$', reservationsviewspage, name='home'),
    url(r'^connection-Tasksmanager$', reservationsviewslogpage, name="public_connection"),
    url(r'^myreserve$', user_reservationpage, name="distinct-reservations"),
    url(r'^logout$',logoutpage, name="logout"),
    url(r'^login-again$',LoginAgain.as_view(), name="login-again"),
    url(r'^ticket_chart$', book_ticket_chart, name="ticket-chart"),
    url(r'^make_reserve_ajax/(?P<route>\d+)$',make_reserve_ajax, name="make_reserve_ajax"),
    url(r'^get_booked_seats/(?P<route>\d+)/$', check_get_seat_availabilty_and_chart, name="get_booked_seats"),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^paystack/', include('paystack.urls',namespace='paystack')),
]
