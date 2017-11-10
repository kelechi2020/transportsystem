from django.conf.urls import include, url
from django.contrib import admin
from reservations.view.login_modal import LoginAgain

from django.contrib.auth import authenticate

from reservations.view.logout import logoutpage
from reservations.view.user_reservation import user_reservationpage
from reservations.views import reservationsviewspage, reservationsviewslogpage

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
]
