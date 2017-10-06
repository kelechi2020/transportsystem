from django.conf.urls import  url
from .view.register_modal import SmilesView
from .view.login_modal import LoginView


urlpatterns = [
    url(r'new-user', SmilesView.as_view(), name='register'),
    url(r'login-user', LoginView.as_view(), name='login'),
    url(r'^localgov/(?P<route>\d+)/(?P<bus>\d+)/(?P<name>[^/]+)$', 'reservations.view.reserve_seat.page', name='reserve'),
    url(r'^form_submit$', 'reservations.view.reserve_seat.formsubmit', name='book'),
    url(r'^active-route$', 'reservations.views.activeroutes', name='route'),

    #url(r'create-reservation',CreateReservation.as_view(), name='reserve')
]