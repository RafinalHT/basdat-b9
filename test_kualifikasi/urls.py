from django.urls import path
from test_kualifikasi.views import *

app_name = 'tes_kualifikasi'

urlpatterns = [
    path('pertanyaan/', pertanyaan_kualifikasi_view, name='pertanyaan'),
    path('buat_ujian/', buat_ujian, name='buat_ujian'),
    path('list_ujian/', list_ujian, name='list_ujian'),
    path('riwayat/', riwayat, name='riwayat'),
]