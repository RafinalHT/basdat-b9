from django.shortcuts import render
from utils import query
from django.db import connection

# Create your views here.
def daftar_atlet(request):
    if request.COOKIES['role']=='umpire':
        dataAtletKualifikasi = query.query(f"select m.nama, a.tgl_lahir, a.negara_asal, a.play_right, a.height, k.world_rank, k.world_tour_rank, " +
                                        "a.jenis_kelamin, sum(p.total_point) as total_point " +
                                        "from member m, atlet a, atlet_kualifikasi k, point_history p " +
                                        "where m.id = a.id and a.id = k.id_atlet and p.id_atlet = a.id " +
                                        "group by m.nama, a.tgl_lahir, a.negara_asal, a.play_right, a.height, k.world_rank, k.world_tour_rank, a.jenis_kelamin;")
        
        dataAtletNonKualifikasi = query.query(f"select m.nama, a.tgl_lahir, a.negara_asal, a.play_right, a.height, a.world_rank, a.jenis_kelamin, " +
                                            "sum(p.total_point) as total_point " +
                                            "from member m, atlet a, atlet_non_kualifikasi k, point_history p " +
                                            "where m.id = a.id and a.id = k.id_atlet and p.id_atlet = a.id " +
                                            "group by m.nama, a.tgl_lahir, a.negara_asal, a.play_right, a.height, a.world_rank, a.jenis_kelamin;")
        
        dataAtletGanda = query.query(f"select g.id_atlet_ganda, m1.nama AS nama_atlet_kualifikasi, m2.nama AS nama_atlet_kualifikasi_2, " +
                                    "(sum(p1.total_point) + sum(p2.total_point)) as total_point " + 
                                    "from atlet_ganda g " +
                                    "join atlet a1 on g.id_atlet_kualifikasi = a1.id " +
                                    "join atlet a2 on g.id_atlet_kualifikasi_2 = a2.id " +
                                    "join point_history p1 on a1.id = p1.id_atlet " +
                                    "join point_history p2 on a2.id = p2.id_atlet " +
                                    "join member m1 on a1.id = m1.id " +
                                    "join member m2 on a2.id = m2.id " +
                                    "group by g.id_atlet_ganda, m1.nama, m2.nama;")
                                                    
        nama_k = [record[0] for record in dataAtletKualifikasi]
        tgl_lahir_k = [record[1] for record in dataAtletKualifikasi]
        negara_asal_k = [record[2] for record in dataAtletKualifikasi]
        play_right_k = [record[3] for record in dataAtletKualifikasi]
        height_k = [record[4] for record in dataAtletKualifikasi]
        world_rank_k = [record[5] for record in dataAtletKualifikasi]
        world_tour_rank_k = [record[6] for record in dataAtletKualifikasi]
        jenis_kelamin_k = [record[7] for record in dataAtletKualifikasi]
        total_point_k = [record[8] for record in dataAtletKualifikasi]

        nama_nk = [record[0] for record in dataAtletNonKualifikasi]
        tgl_lahir_nk = [record[1] for record in dataAtletNonKualifikasi]
        negara_asal_nk = [record[2] for record in dataAtletNonKualifikasi]
        play_right_nk = [record[3] for record in dataAtletNonKualifikasi]
        height_nk = [record[4] for record in dataAtletNonKualifikasi]
        world_rank_nk = [record[5] for record in dataAtletNonKualifikasi]
        jenis_kelamin_nk = [record[5] for record in dataAtletNonKualifikasi]
        total_point_nk = [record[7] for record in dataAtletNonKualifikasi]

        id_g = [record[0] for record in dataAtletGanda]
        nama_1 = [record[1] for record in dataAtletGanda]
        nama_2 = [record[2] for record in dataAtletGanda]
        total_point_g = [record[3] for record in dataAtletGanda]
        
        data_k = {
            'nama' : nama_k,
            'tgl_lahir' : tgl_lahir_k,
            'negara_asal' : negara_asal_k,
            'play_right' : play_right_k,
            'height' : height_k,
            'world_rank' : world_rank_k,
            'world_tour_rank' : world_tour_rank_k,
            'jenis_kelamin' : jenis_kelamin_k,
            'total_point' : total_point_k,
        }

        data_nk = {
            'nama' : nama_nk,
            'tgl_lahir' : tgl_lahir_nk,
            'negara_asal' : negara_asal_nk,
            'play_right' : play_right_nk,
            'height' : height_nk,
            'world_rank' : world_rank_nk,
            'jenis_kelamin' : jenis_kelamin_nk,
            'total_point' : total_point_nk,
        }

        data_g = {
            'id' : id_g,
            'nama_1' : nama_1,
            'nama_2' : nama_2,
            'total_point' : total_point_g,
        }

        data = {
            'data_k': data_k,
            'data_nk': data_nk,
            'data_g': data_g
        }

        data_k = convert_dict_to_list_k(data_k)
        data_nk = convert_dict_to_list_nk(data_nk)
        data_g = convert_dict_to_list_g(data_g)

        return render(request, 'daftar_atlet.html', {'data_k': data_k, 'data_nk': data_nk, 'data_g': data_g})
    else:
        return render(request, 'daftar_atlet.html')
    

def partai_kompetisi_event(request):
    if request.COOKIES['role']=='umpire':
        data_partai_kompetisi_event = query.query(f'''SELECT
                                                    e.nama_event,
                                                    e.tahun,
                                                    e.nama_stadium,
                                                    STRING_AGG(DISTINCT p.jenis_partai, ', ') AS aggregated_jenis_partai,
                                                    e.kategori_superseries,
                                                    e.tgl_mulai,
                                                    e.tgl_selesai,
                                                    COUNT(pme.nama_event) AS peserta_count,
                                                    s.kapasitas
                                                    FROM
                                                    event e
                                                    JOIN
                                                    partai_kompetisi p ON p.nama_event = e.nama_event AND p.tahun_event = e.tahun
                                                    JOIN
                                                    stadium s ON e.nama_stadium = s.nama
                                                    JOIN
                                                    peserta_mendaftar_event pme ON pme.nama_event = e.nama_event AND pme.tahun = e.tahun
                                                    GROUP BY
                                                    e.nama_event,
                                                    e.tahun,
                                                    e.nama_stadium,
                                                    e.kategori_superseries,
                                                    e.tgl_mulai,
                                                    e.tgl_selesai,
                                                    s.kapasitas;
                                                    ''')
        
        nama_event = [record[0] for record in data_partai_kompetisi_event]
        tahun = [record[1] for record in data_partai_kompetisi_event]
        nama_stadium = [record[2] for record in data_partai_kompetisi_event]
        aggregated_jenis_partai = [record[3] for record in data_partai_kompetisi_event]
        kategori_superseries = [record[4] for record in data_partai_kompetisi_event]
        tgl_mulai = [record[5] for record in data_partai_kompetisi_event]
        tgl_selesai = [record[6] for record in data_partai_kompetisi_event]
        peserta_count = [record[7] for record in data_partai_kompetisi_event]
        kapasitas = [record[8] for record in data_partai_kompetisi_event]

        data = {
            'nama_event' : nama_event,
            'tahun' : tahun,
            'nama_stadium' : nama_stadium,
            'aggregated_jenis_partai' : aggregated_jenis_partai,
            'kategori_superseries' : kategori_superseries,
            'tgl_mulai' : tgl_mulai,
            'tgl_selesai' : tgl_selesai,
            'peserta_count' : peserta_count,
            'kapasitas' : kapasitas,
        }

        data = convert_dict_to_list_pke(data)
        print(data)

        return render(request, 'data_partai_kompetisi_event.html', {'data': data})
    else:
        return render(request, 'data_partai_kompetisi_event.html')
    

def hasil_pertandingan(request):
    if request.COOKIES['role']=='umpire':
        nama_event = request.GET.get('nama_event')
        tahun = request.GET.get('tahun')
        data_partai_kompetisi_event = query.query(f'''SELECT
                                                    e.nama_event,
                                                    e.tahun,
                                                    e.nama_stadium,
                                                    STRING_AGG(DISTINCT p.jenis_partai, ', ') AS aggregated_jenis_partai,
                                                    e.kategori_superseries,
                                                    e.tgl_mulai,
                                                    e.tgl_selesai,
                                                    COUNT(pme.nama_event) AS peserta_count,
                                                    s.kapasitas,
                                                    e.total_hadiah
                                                    FROM
                                                    event e
                                                    JOIN
                                                    partai_kompetisi p ON p.nama_event = e.nama_event AND p.tahun_event = e.tahun
                                                    JOIN
                                                    stadium s ON e.nama_stadium = s.nama
                                                    JOIN
                                                    peserta_mendaftar_event pme ON pme.nama_event = e.nama_event AND pme.tahun = e.tahun
                                                    WHERE e.nama_event = '{nama_event}' and e.tahun = {tahun}
                                                    GROUP BY
                                                    e.nama_event,
                                                    e.tahun,
                                                    e.nama_stadium,
                                                    e.kategori_superseries,
                                                    e.tgl_mulai,
                                                    e.tgl_selesai,
                                                    s.kapasitas,
                                                    e.total_hadiah;
                                                    ''')
        
        nama_event = [record[0] for record in data_partai_kompetisi_event]
        tahun = [record[1] for record in data_partai_kompetisi_event]
        nama_stadium = [record[2] for record in data_partai_kompetisi_event]
        aggregated_jenis_partai = [record[3] for record in data_partai_kompetisi_event]
        kategori_superseries = [record[4] for record in data_partai_kompetisi_event]
        tgl_mulai = [record[5] for record in data_partai_kompetisi_event]
        tgl_selesai = [record[6] for record in data_partai_kompetisi_event]
        peserta_count = [record[7] for record in data_partai_kompetisi_event]
        kapasitas = [record[8] for record in data_partai_kompetisi_event]
        total_hadiah = [record[9] for record in data_partai_kompetisi_event]

        data = {
            'nama_event' : nama_event,
            'tahun' : tahun,
            'nama_stadium' : nama_stadium,
            'aggregated_jenis_partai' : aggregated_jenis_partai,
            'kategori_superseries' : kategori_superseries,
            'tgl_mulai' : tgl_mulai,
            'tgl_selesai' : tgl_selesai,
            'peserta_count' : peserta_count,
            'kapasitas' : kapasitas,
            'total_hadiah' : total_hadiah,
        }

        print(data)

        return render(request, 'hasil_pertandingan_2.html', {'data': data})
    else:
        return render(request, 'hasil_pertandingan_2.html')



def convert_dict_to_list_k(data_dict):
    data_list = []
    
    for i in range(len(data_dict['nama'])):
        data = {
            'nama': data_dict['nama'][i],
            'tgl_lahir': data_dict['tgl_lahir'][i],
            'negara_asal': data_dict['negara_asal'][i],
            'play_right': data_dict['play_right'][i],
            'height': data_dict['height'][i],
            'world_rank': data_dict['world_rank'][i],
            'world_tour_rank': data_dict['world_tour_rank'][i],
            'jenis_kelamin': data_dict['jenis_kelamin'][i],
            'total_point': data_dict['total_point'][i]
        }
        data_list.append(data)
    
    return data_list

def convert_dict_to_list_nk(data_dict):
    data_list = []
    
    for i in range(len(data_dict['nama'])):
        data = {
            'nama': data_dict['nama'][i],
            'tgl_lahir': data_dict['tgl_lahir'][i],
            'negara_asal': data_dict['negara_asal'][i],
            'play_right': data_dict['play_right'][i],
            'height': data_dict['height'][i],
            'world_rank': data_dict['world_rank'][i],
            'jenis_kelamin': data_dict['jenis_kelamin'][i],
            'total_point': data_dict['total_point'][i]
        }
        data_list.append(data)
    
    return data_list

def convert_dict_to_list_g(data_dict):
    data_list = []
    
    for i in range(len(data_dict['id'])):
        data = {
            'id' : data_dict['id'][i],
            'nama_1' : data_dict['nama_1'][i],
            'nama_2' : data_dict['nama_2'][i],
            'total_point' : data_dict['total_point'][i],
        }
        data_list.append(data)
    
    return data_list

def convert_dict_to_list_pke(data_dict):
    data_list = []
    
    for i in range(len(data_dict['nama_event'])):
        data = {
            'nama_event' : data_dict['nama_event'][i],
            'tahun' : data_dict['tahun'][i],
            'nama_stadium' : data_dict['nama_stadium'][i],
            'aggregated_jenis_partai' : data_dict['aggregated_jenis_partai'][i],
            'kategori_superseries' : data_dict['kategori_superseries'][i],
            'tgl_mulai' : data_dict['tgl_mulai'][i],
            'tgl_selesai' : data_dict['tgl_selesai'][i],
            'peserta_count' : data_dict['peserta_count'][i],
            'kapasitas' : data_dict['kapasitas'][i],
        }
        data_list.append(data)
    
    return data_list