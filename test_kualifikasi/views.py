from django.shortcuts import render
from test_kualifikasi.forms import *

def data_kualifikasi_view(request):
    context = {
        'data_kualifikasi_form': DataKualifikasiForm(),
    }
    return render(request, 'form_data.html', context)

def pertanyaan_kualifikasi_view(request):
    context = {
        'pertanyaan_kualifikasi_form': PertanyaanKualifikasiForm(),
    }
    return render(request, 'pertanyaan.html', context) 