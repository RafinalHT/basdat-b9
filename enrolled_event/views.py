from django.shortcuts import render, redirect
from utils import query
from django.db import connection
import datetime

# Create your views here.
def enrolled_event_view(request):
    if request.method =='POST':
        action = eval(request.POST.get('action'))
        data2 = {
            'nomor_peserta': action['nomor_peserta'],
            'jenis_peserta': action['jenis_peserta'],
            'nama_event': action['nama_event'],
            'tahun': action['tahun'],
            'nama_stadium': action['nama_stadium'],
            'kategori_superseries': action['kategori_superseries'],
            'tgl_mulai': action['tgl_mulai'],
            'tgl_selesai': action['tgl_selesai']
        }
        print(data2)
        #response = redirect('enrolled_event:unenroll_event')
        response = redirect('enrolled_event:unenroll_event')
        response.set_cookie('nomor_peserta', data2['nomor_peserta'])
        response.set_cookie('nama_event', data2['nama_event'])
        response.set_cookie('tahun', data2['tahun'])
        #return response
        
        
    id = request.COOKIES['id']
    cursor = connection.cursor()
    query = f"""
    (
            SELECT
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
                ak.ID_Atlet = '{id}'
        )
        UNION
        (
            SELECT
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
                or ag.ID_Atlet_Kualifikasi_2 = '{id}'
        );
    """
    cursor.execute(query)  # Eksekusi query
    columns = [col[0] for col in cursor.description]  # Ambil nama kolom dari cursor.description
    data = cursor.fetchall()  # Mendapatkan semua baris hasil query sebagai list of tuples
    print(data)
    list_enrolled_event = []  # Inisialisasi list kosong
    
    if data:
        list_enrolled_event = [{'nomor_peserta' : item[0],
                                'jenis_peserta' : item[1],
                                'nama_event': item[2], 
                                'tahun': item[3], 
                                'nama_stadium': item[4], 
                                'kategori_superseries': item[5], 
                                'tgl_mulai': item[6], 
                                'tgl_selesai': item[7]} for item in data]

    
    return render(request, 'enrolled_events.html', context={'list_enrolled_event':list_enrolled_event})


def unenroll_event(request):
    if request.method == 'POST':
        nomor_peserta = request.COOKIES['nomor_peserta']
        nama_event = request.COOKIES['nama_event']
        tahun = request.COOKIES['tahun']
        
        #cursor = connection.cursor()
        response = query.query(f"""
            DELETE FROM PESERTA_MENDAFTAR_EVENT
            WHERE 
            nomor_peserta = '{nomor_peserta}' AND
            nama_event = '{nama_event}' AND
            tahun = '{tahun}'
        """)
        print(response)
        #cursor.execute(query)
        #connection.commit()
        
        # Setelah unenroll berhasil, redirect kembali ke halaman "Enrolled Event"
        return redirect('enrolled_event:enrolled_event_view')
        
    # Jika metode bukan POST, tidak perlu menampilkan halaman terpisah, langsung redirect ke "Enrolled Event"
    return redirect('enrolled_event:enrolled_event_view')
    
    
        
    

