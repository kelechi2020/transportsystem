from django.conf.urls import  url
from .view.register_modal import SmilesView
from .view.login_modal import LoginView

urlpatterns = [
    url(r'new-user', SmilesView.as_view(), name='register'),
    url(r'login-user', LoginView.as_view(), name='login')
]