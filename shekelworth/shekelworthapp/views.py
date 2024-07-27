from django.shortcuts import render
from django.http import HttpResponse
from .forms import CurrencyForm
import requests
import json

# Create your views here.

def shekel_worth(request):
    forms = CurrencyForm()
    conversion_result = None

    if request.POST:
        data = request.POST.dict()
        _from = data['From']
        to = data['To']
        amount = data['amount']

        # Request parameters
        MAIN_URL = "https://v6.exchangerate-api.com/v6/"
        API_KEY = ""
        FULL_URL = f"{MAIN_URL}{API_KEY}/pair/{_from}/{to}/{amount}/"

        response = requests.get(FULL_URL)
        resp = response.json()
        res = resp['conversion_result']
        conversion_result = f"{amount} {_from} is equivalent to {res} {to}"

    return render(request, 'index.html', {'forms': forms, 'conversion_result': conversion_result})
