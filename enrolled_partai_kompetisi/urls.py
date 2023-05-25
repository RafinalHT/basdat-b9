from django.urls import path
from enrolled_partai_kompetisi.views import *

app_name = 'enrolled_partai_kompetisi'

urlpatterns = [
    path('', enrolled_partai_kompetisi_view, name='enrolled_partai_kompetisi'),
]