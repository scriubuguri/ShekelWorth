from django.urls import path
from . import views

urlpatterns = [
    path('', views.shekel_worth, name='index'),
    path('result/', views.result, name='result'),
]
