from django.urls import path
from test_kualifikasi.views import *

app_name = 'tes_kualifikasi'

urlpatterns = [
    path('form_data/', data_kualifikasi_view, name='form_data'),
    path('pertanyaan/', pertanyaan_kualifikasi_view, name='pertanyaan'),
]