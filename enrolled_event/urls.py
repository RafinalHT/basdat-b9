from django.urls import path
from enrolled_event.views import *

app_name = 'enrolled_event'

urlpatterns = [
    path('', enrolled_event_view, name='enrolled_event'),
]