from django.urls import path
from sponsor.views import *

app_name = 'sponsor'

urlpatterns = [
    path('daftar-sponsor/', daftar_sponsor, name='daftar_sponsor'),
]