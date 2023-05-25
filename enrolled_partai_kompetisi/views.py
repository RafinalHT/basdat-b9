from django.shortcuts import render, redirect
from utils import query
from django.db import connection
import datetime

# Create your views here.
def enrolled_partai_kompetisi_view(request):
                
    id = request.COOKIES['id']
    cursor = connection.cursor()
    query = f"""
        (SELECT
            pk.nomor_peserta,
            ppk.jenis_partai,
            e.*
        FROM
            EVENT e
            JOIN PESERTA_MENDAFTAR_EVENT pme ON e.Nama_Event = pme.Nama_Event
            AND e.Tahun = pme.Tahun
            JOIN PESERTA_KOMPETISI pk ON pme.Nomor_Peserta = pk.Nomor_Peserta
            JOIN PARTAI_PESERTA_KOMPETISI ppk on ppk.nomor_peserta = pk.nomor_peserta 
                and ppk.nama_event = e.nama_event 
                and ppk.tahun_event = e.tahun
            JOIN ATLET_KUALIFIKASI ak ON pk.ID_Atlet_Kualifikasi = ak.ID_Atlet
        WHERE
            ak.ID_Atlet = '{id}')
        UNION
        (SELECT
            pk.nomor_peserta,
            ppk.jenis_partai,
            e.*
        FROM
            EVENT e
            JOIN PESERTA_MENDAFTAR_EVENT pme ON e.Nama_Event = pme.Nama_Event
            AND e.Tahun = pme.Tahun
            JOIN PESERTA_KOMPETISI pk ON pme.Nomor_Peserta = pk.Nomor_Peserta
            JOIN PARTAI_PESERTA_KOMPETISI ppk on ppk.nomor_peserta = pk.nomor_peserta  
                and ppk.nama_event = e.nama_event 
                and ppk.tahun_event = e.tahun
            JOIN ATLET_GANDA ag ON pk.ID_Atlet_Ganda = ag.ID_Atlet_Ganda
        WHERE
            ag.ID_Atlet_Kualifikasi = '{id}'
            or ag.ID_Atlet_Kualifikasi_2 = '{id}');
    """
    cursor.execute(query)  # Eksekusi query
    columns = [col[0] for col in cursor.description]  # Ambil nama kolom dari cursor.description
    data = cursor.fetchall()  # Mendapatkan semua baris hasil query sebagai list of tuples
    print(data)
    list_enrolled_partai_kompetisi = []  # Inisialisasi list kosong
    
    if data:
        list_enrolled_partai_kompetisi = [{'nomor_peserta' : item[0],
                                'jenis_peserta' : item[1],
                                'nama_event': item[2], 
                                'tahun': item[3], 
                                'nama_stadium': item[4], 
                                'negara': item[5], 
                                'tgl_mulai': item[6], 
                                'tgl_selesai': item[7],
                                'kategori_superseries': item[8],
                                'hadiah' : item[9]} for item in data]

    
    return render(request, 'enrolled_partai_kompetisi.html', context={'list_enrolled_partai_kompetisi':list_enrolled_partai_kompetisi})