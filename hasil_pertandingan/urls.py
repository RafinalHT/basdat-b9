from django.urls import path
from hasil_pertandingan.views import *

app_name = 'hasil_pertandingan'

urlpatterns = [
    #path('hasil', hasil_pertandingan_view, name='main'),
    #path('', detail_hasil_pertandingan_view, name='detail_hasil_pertandingan_view'),
    #path('hasil/', hasil_pertandingan_view, name='hasil_pertandingan_view'),
    path('', hasil_pertandingan_view, name='hasil_pertandingan_view'),
    path('detailpertandingan/', detail_hasil_pertandingan_view, name='detail_hasil_pertandingan_view'),
]