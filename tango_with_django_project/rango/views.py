from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey dumbfuck!!!!<br/> <a href='/rango/about/'>About</a>" )

def about(request):
    return HttpResponse("Rango says here is the fucking about pagggeee!!! <a href='/rango/'>Index</a>")
