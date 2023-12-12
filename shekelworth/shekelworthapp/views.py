from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def currency_converter(request):
    return HttpResponse("Hello! You're at the ShekelWorth page.")
