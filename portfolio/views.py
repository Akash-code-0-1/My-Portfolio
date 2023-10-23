from django.shortcuts import render,redirect
from .models import*



# Create your views here.

def port_front_page(request):
    return render(request, 'portFrontpage.html')