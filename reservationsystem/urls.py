from django.conf.urls import include, url
from django.contrib import admin
from reservations.view.login_modal import LoginAgain

from django.contrib.auth import authenticate

urlpatterns = [
    # Examples:
    # url(r'^$', 'reservationsystem.view.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^modal/', include('reservations.urls')),
    url(r'^$', 'reservations.views.page', name='home'),
    url(r'^connection-Tasksmanager$', 'reservations.views.logpage', name="public_connection"),
    url(r'^myreserve$', 'reservations.view.user_reservation.page', name="distinct-reservations"),
    url(r'^logout$','reservations.view.logout.page', name="logout"),
    url(r'^login-again$',LoginAgain.as_view(), name="login-again"),
]
