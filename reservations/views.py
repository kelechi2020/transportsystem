from django.conf import settings
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Customer, Seat, Route, Reservation, Bus
from django.contrib.auth import authenticate, login

def reservationsviewspage(request):

    route = Route.objects.all()
    from pprint import pprint
    pprint(request.user.username)
    return render(request, 'index.html', {'route': route})



def activeroutes(request):
    route = Route.objects.all()
    from pprint import pprint
    pprint(route)
    return render(request, 'active.html', {'route': route})

class Form_login(forms.Form):
    email = forms.CharField()
    password = forms.CharField()


def reservationsviewslogpage(request):
	if request.POST:
	# This line is used to check if the Form_connection form has been posted. If mailed, the form will be treated, otherwise it will be displayed to the user.
		form = Form_login(request.POST)
		if form.is_valid():
			username = form.cleaned_data["email"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)
			# This line verifies that the username exists and the password is correct.
			if settings.DEBUG:
				from pprint import pprint
				pprint(user)

			if user:
				# In this line, the authenticate function returns None if authentication has failed, otherwise it returns an object that validate the condition.
				login(request, user)
				# In this line, the login() function allows the user to connect.
				if request.GET.get('next') is not None:
					return redirect(request.GET['next'])

		else:
			return render(request, 'connection.html', {'form' : form})
	else:
		form = Form_login()
	return render(request, 'connection.html', {'form' : form})
