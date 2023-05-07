from django.urls import path
from pertandingan.views import *

app_name = 'pertandingan'

urlpatterns = [
    path('', lihat_event_view, name='lihat_event_view'),
    path('perempatfinal/', perempat_final_view, name='perempat_final'),
    path('semifinal/', semifinal_view, name='semifinal'),
    path('final/', final_view, name='final'),
]