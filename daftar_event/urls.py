from django.urls import path
from daftar_event.views import *

app_name = 'daftar_event'

urlpatterns = [
    path('pilih_stadium/', pilih_stadium, name='pilih_stadium'),
    path('pilih_event/', pilih_event, name='pilih_event'),
    path('pilih_kategori/', pilih_kategori, name='pilih_kategori'),
]