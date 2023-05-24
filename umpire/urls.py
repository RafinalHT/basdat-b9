from django.urls import path
from umpire.views import *

app_name = 'umpire'

urlpatterns = [
    path('daftar_atlet/', daftar_atlet, name='daftar_atlet'),
    path('daftar_partai_kompetisi_event/', partai_kompetisi_event, name='partai_kompetisi_event'),
    path('hasil_pertandingan/', hasil_pertandingan, name='hasil_pertandingan'),
]