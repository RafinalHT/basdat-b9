from django.urls import path
from umpire.views import *

app_name = 'umpire'

urlpatterns = [
    path('daftar_atlet/', daftar_atlet, name='daftar_atlet'),
    path('daftar_partai_kompetisi_event/', partai_kompetisi_event, name='partai_kompetisi_event'),
    path('hasil_pertandingan/', hasil_pertandingan, name='hasil_pertandingan'),
    path('perempat_final/', perempat_final, name='perempat_final'),
    path('semifinal/', semifinal, name='semifinal'),
    path('juara3/', juara3, name='juara3'),
    path('pertandingan/', pertandingan, name='pertandingan'),
]