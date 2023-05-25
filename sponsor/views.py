from django.shortcuts import render,redirect
from django.db import InternalError, connection
from django.contrib import messages
from utils import query
from sponsor.forms import SponsorForm

# Create your views here.

def daftar_sponsor(request):
    # mengambil daftar sponsor untuk ditampilkan di dropdown nama sponsor
    data_sponsor = query.query(f""" SELECT nama_brand FROM SPONSOR""")
    #print(data_sponsor)
    context = {'sponsor_list': data_sponsor}
    
    if request.method == 'POST':
        nama = request.POST.get('nama')
        tgl_mulai = request.POST.get('tgl_mulai')
        tgl_selesai = request.POST.get('tgl_selesai')
        print(nama)
        print(tgl_mulai)
        print(tgl_selesai)
        
        # query untuk dapat id_atlet dan id_sponsor
        id = request.COOKIES['id']
        get_id_sponsor = query.query(f"""
            SELECT id 
            FROM SPONSOR
            WHERE nama_brand = '{nama}'
        """)
        id_sponsor = get_id_sponsor[0][0]
        print("id:", id)
        print("id sponsor:", id_sponsor)
        data = query.query(f"""
            INSERT INTO ATLET_SPONSOR(id_atlet, id_sponsor, tgl_mulai, tgl_selesai) 
            VALUES ('{id}','{id_sponsor}', '{tgl_mulai}', '{tgl_selesai}')
        """)
        print(data)
        # daftar_sponsor= f"""
        
        # """
        # try:
        #     cursor.execute('set search_path to babadu')
        #     cursor.execute(daftar_sponsor)
        #     return redirect('sponsor:list_sponsor')
        # except InternalError as e:
        #     messages.info(request, str(e.args))

    return render(request, 'daftar_sponsor.html', context)

def list_sponsor(request):
    id = request.COOKIES['id']
    data = query.query(f"""
                SELECT 
                    s.nama_brand, 
                    a.tgl_mulai, 
                    a.tgl_selesai
                FROM 
                    SPONSOR s, 
                    ATLET_SPONSOR a
                WHERE 
                    s.id = a.id_sponsor AND
                    a.id_atlet = '{id}'
        """)
    print(data)
    print(data==[])
    if data==[]:
        print(4)
        result={}
        status={'status': True }
    else:
        result = [{'tahun': item[0], 'batch': item[1], 'tempat': item[2], 'tanggal': item[3],'hasil': item[4]} for item in data]
        status={}
    return render(request, 'list_sponsor.html')