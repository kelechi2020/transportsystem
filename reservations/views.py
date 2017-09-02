from django.shortcuts import render
from .models import Customer


def page(request):
    return render(request, 'index.html')
