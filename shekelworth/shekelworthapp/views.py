from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import CurrencyForm
import requests
import json

# Create your views here.

def shekel_worth(request):
    forms = CurrencyForm()
    if request.POST:
        data = request.POST.dict()
        request.session['our_data'] = data
        return redirect('result')
    return render(request, 'index.html', {'forms': forms})

def result(request):

    #request parameters
    MAIN_URL = "https://v6.exchangerate-api.com/v6/"
    API_KEY = "your_api_key"

    data = request.session['our_data']
    _from = data['From']
    to = data['To']
    amount = data['amount']
    FULL_URL = "{main_url}{api_key}/pair/{_from}/{to}/{amount}/".format(
       main_url=MAIN_URL,
       api_key=API_KEY,
       _from=_from,
       to=to,
       amount=amount
    )

    response = requests.get(FULL_URL)
    resp = response.json()
    res = resp['conversion_result']
    conversion_result = "Amount {amount} {_from} to {to} is: {result}".format(
        amount=amount,
        _from=_from,
        to=to,
        result=res
    )
    return HttpResponse(conversion_result)
