from django.urls import path
from daftar_event.views import *

app_name = 'daftar_event'

urlpatterns = [
    path('pilih_event/', pilih_stadium, name='pilih_stadium'),
    path('pilih_event/<stadium>/', pilih_event, name='pilih_event'),
    path('pilih_event/<stadium>/<event>/', pilih_kategori, name='pilih_kategori'),
]