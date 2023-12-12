from django.urls import path
from . import views

urlpatterns = [
    path('', views.currency_converter, name='index'),
]
