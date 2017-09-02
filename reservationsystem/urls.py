from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import authenticate

urlpatterns = [
    # Examples:
    # url(r'^$', 'reservationsystem.view.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^modal/', include('reservations.urls')),
    url(r'^index$', 'reservations.views.page', name='home'),

]
