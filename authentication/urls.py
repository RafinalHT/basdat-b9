from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('register_pelatih/', register_pelatih, name='register_pelatih'),
    path('register_atlet/', register_atlet, name='register_atlet'),
    path('register_umpire/', register_umpire, name='register_umpire'),
]