from ast import parse
from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from utils import query
from django.contrib import messages
import datetime

# Create your views here.
def pilih_stadium(request):
    context = {}
    cursor = connection.cursor()
    query = f"""
    SELECT
        Nama,
        Negara,
        Kapasitas
    FROM STADIUM;
    """
    cursor.execute(query)
    # list_stadium = []
    # column = [col[0] for col in cursor.description]
    # test = [dict(zip(column, row)) for row in cursor.fetchall()]
    # print(test)
    # for i in column:
    #     list_stadium.append(i)
    # print(list_stadium)
    data = cursor.fetchall()  
    stadium = []  
    if data:
        stadium = [{'nama': item[0],
                            'negara': item[1],
                            'kapasitas': item[2]} for item in data]
        
    context['stadium'] = stadium
    return render(request, 'pilih_stadium.html', context)

def pilih_event(request, stadium):
    context = {}
    cursor = connection.cursor()
    query = f"""
    SELECT
        Nama_Event,
        Total_Hadiah,
        Tgl_Mulai,
        Kategori_Superseries
    FROM EVENT
    WHERE Nama_Stadium = '{stadium}' AND Tgl_Mulai > NOW();
    """
    cursor.execute(query)
    data = cursor.fetchall()
    event = []
    if data:
        event = [{'nama_event': item[0],
                            'total_hadiah': item[1],
                            'tgl_mulai': item[2],
                            'kategori_superseries': item[3]} for item in data]
    print(event)
    context['event'] = event
    return render(request, 'pilih_event.html', context)

def pilih_kategori(request, stadium, event):
    context = {}
    cursor = connection.cursor()
    query = f"""
    SELECT
        E.Nama_Event,
        E.Total_Hadiah,
        E.Tgl_Mulai,
        E.Tgl_Selesai,
        E.Kategori_Superseries,
        S.Kapasitas,
        S.Nama as nama_stadium,
        S.Negara
    FROM EVENT E JOIN STADIUM S ON E.Nama_Stadium = S.Nama
    WHERE E.Nama_Event = '{event}';
    """
    cursor.execute(query)
    data = cursor.fetchall()

    return render(request, 'pilih_kategori.html')