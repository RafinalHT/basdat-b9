from django.shortcuts import render
from utils import query
from django.db import connection


def dashboard(request):
    if request.COOKIES['role']=='atlet':
        dataPengguna = query.query(f"Select*from {request.COOKIES['role']} where id='{request.COOKIES['id']}'")
        dataMember =query.query(f"Select*from member where id='{request.COOKIES['id']}'")
        dataStatus=query.query(f"""select a.id,
        case
            when n.id_atlet IS NOT NULL then 'Not Qualified'
            when k.id_atlet IS NOT NULL then 'Qualified'
        end as status
        from
        atlet a
            left join atlet_kualifikasi k on a.id = k.id_atlet
            left join atlet_non_kualifikasi n on a.id = n.id_atlet
        where a.id= '{request.COOKIES['id']}'""")
        dataPelatih = query.query(f""" SELECT string_agg(m.Nama,', ') as pelatih
        from atlet_pelatih p
            join atlet a on a.id = p.id_atlet
            join pelatih pe on p.id_pelatih = pe.id
            join member m on pe.id = m.id
        where
            a.id= '{request.COOKIES['id']}'""")
        dataPoin = query.query(f""" select sum(p.total_point) as tot
        from point_history p
        join atlet a on p.id_atlet = a.id
        where a.id= '{request.COOKIES['id']}'""")
        poin = dataPoin[0][0]
        pelatih =dataPelatih[0][0]
        print(dataPelatih[0][0])
        status = dataStatus[0][1]
        nama= dataMember[0][1]
        email = dataMember[0][2]
        tanggalLahir = dataPengguna[0][1]
        negaraAsal = dataPengguna[0][2]
        play = dataPengguna[0][3]
        height = dataPengguna[0][4]
        worldRank = dataPengguna[0][5]
        jenisKelamin = dataPengguna[0][6]
        if(status == None):
            status ='Not Qualified'
        if(play== True):
            play ='Right'
        else:
            play='Left'
        if(jenisKelamin== True):
            jenisKelamin ='Putra'
        else:
            jenisKelamin='Putri'
        data={'poin' : poin,
              'pelatih' : pelatih,
              'status' : status,
              'nama' : nama,
              'email' : email,
              'tanggalLahir' : tanggalLahir,
              'negaraAsal' : negaraAsal,
              'play' : play,
              'height': height,
              'worldRank': worldRank,
              'jenisKelamin': jenisKelamin,
              }
    elif request.COOKIES['role']=='pelatih':
        dataPengguna = query.query(f"Select*from {request.COOKIES['role']} where id='{request.COOKIES['id']}'")
        dataMember =query.query(f"Select*from member where id='{request.COOKIES['id']}'")
        dataSpesialisasi = query.query(f"""  SELECT
            string_agg(s.Spesialisasi, ', ')
        FROM
            PELATIH_SPESIALISASI ps
            JOIN SPESIALISASI s ON ps.ID_Spesialisasi = s.ID
        WHERE
            ps.ID_Pelatih = '{request.COOKIES['id']}';""")
        nama= dataMember[0][1]
        email = dataMember[0][2]
        tanggalMulai = dataPengguna[0][1]
        spesialisasi = dataSpesialisasi[0][0]
        data={
              'nama' : nama,
              'email' : email,
              'tanggalMulai' : tanggalMulai,
              'spesialisasi' : spesialisasi,
              }
    elif request.COOKIES['role']=='umpire':
        dataPengguna = query.query(f"Select*from {request.COOKIES['role']} where id='{request.COOKIES['id']}'")
        dataMember =query.query(f"Select*from member where id='{request.COOKIES['id']}'")
        nama= dataMember[0][1]
        email = dataMember[0][2]
        negara = dataPengguna[0][1]
        data={
              'nama' : nama,
              'email' : email,
              'negara' : negara,
              }
    return render(request, 'dashboard.html', {'data': data})
