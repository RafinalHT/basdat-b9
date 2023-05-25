from ast import parse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from utils import query
from django.contrib import messages
import datetime

# Create your views here.
def pilih_stadium(request):
    context={}
    query_stadium = query.query(f"""
    SELECT
        Nama,
        Negara,
        Kapasitas
    FROM STADIUM
    """)
    print(query_stadium)
    list_stadium = [col[0] for col in query_stadium]
    print(list_stadium)
    context['stadium'] = list_stadium
    return render(request, 'pilih_stadium.html', context)

def pilih_event(request):
    return render(request, 'pilih_event.html')

def pilih_kategori(request):
    return render(request, 'pilih_kategori.html')