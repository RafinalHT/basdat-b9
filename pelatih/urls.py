from django.urls import path
from pelatih.views import *

app_name = 'pelatih'

urlpatterns = [
    path('daftar-atlet-pelatih/', daftar_atlet_pelatih, name='daftar_atlet_pelatih'),
    path('list-atlet/', list_atlet, name='list_atlet'),
]