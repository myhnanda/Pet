from django.urls import path
from reserva.views import *

urlpatterns = [
    path('reserva/', criar_reserva, name = 'criar_reserva'),
    
]
