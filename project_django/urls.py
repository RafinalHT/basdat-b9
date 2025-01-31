"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hasil_pertandingan/', include('hasil_pertandingan.urls')),
    path('pertandingan/', include('pertandingan.urls')),
    path('', include('home.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('authentication/', include('authentication.urls')),
    path('test_kualifikasi/', include('test_kualifikasi.urls')),
    path('daftar_event/', include('daftar_event.urls')),
    path('enrolled_event/', include('enrolled_event.urls')),
    path('sponsor/', include('sponsor.urls')),
    path('pelatih/', include('pelatih.urls')),
    path('enrolled_partai_kompetisi/', include('enrolled_partai_kompetisi.urls')),
    path('umpire/', include('umpire.urls')),
]
