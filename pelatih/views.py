from http.client import HTTPResponse
import re
from django.shortcuts import redirect, render
from utils import query
from django.db import connection

from pelatih.forms import AtletPelatihForm

# Create your views here.

def list_atlet(request):
    if request.COOKIES['role']=='pelatih':
        daftar_atlet = query.query(f'''SELECT m.nama, m.email, a.world_rank
                                    FROM atlet_pelatih ap, member m, atlet a
                                    WHERE ap.id_pelatih = '{request.COOKIES['id']}' and m.id = ap.id_atlet and a.id = ap.id_atlet;
                                    ''')
        
        nama = [record[0] for record in daftar_atlet]
        email = [record[1] for record in daftar_atlet]
        world_rank = [record[2] for record in daftar_atlet]
        
        data = {
            'nama': nama,
            'email': email,
            'world_rank': world_rank,
        }

        data = convert_dict_to_list_a(data)

        return render(request, 'list_atlet.html', {'data': data})
    else:
        return render(request, 'list_atlet.html')
    
def convert_dict_to_list_a(data_dict):
    data_list = []
    
    for i in range(len(data_dict['nama'])):
        data = {
            'nama' : data_dict['nama'][i],
            'email' : data_dict['email'][i],
            'world_rank' : data_dict['world_rank'][i],
        }
        data_list.append(data)
    
    return data_list


def daftar_atlet_pelatih(request):
    if request.COOKIES['role']=='pelatih':
        datar_atlet = query.query(f"select a.id, m.nama from member m, atlet a where m.id = a.id;")
                                                    
        id = [record[0] for record in datar_atlet]
        nama = [record[1] for record in datar_atlet]
        
        data = {
            'id' : id,
            'nama' : nama,
        }

        list_atlet = convert_dict_to_list(data)

        if request.method=='POST':
            print("OK")
            data = request.POST.get('atlet')
            if data:
                print(data)
                uuid = ""

                for element in range(0, len(data)):
                    if (data[element] == ','):
                        if (data[element + 1] == ' '):
                            for e in range(element + 8, len(data)):
                                if (data[e] == "'"):
                                    break

                                uuid += data[e]


                print(uuid)
                context = {}
                response = query.query(
                f"""insert into atlet_pelatih (id_pelatih, id_atlet)
                values ('{request.COOKIES['id']}','{uuid}');""")  

                if type(response) is not str:
                    context = ['Error: Atlet sudah terdaftar']
                    print(f"""insert into atlet_pelatih (id_pelatih, id_atlet)
                        values ('{request.COOKIES['id']}','{uuid}');""")  
                    return render(request, "daftar_atlet_pelatih.html", {'atlet_list': list_atlet, 'context': context})          

                return redirect('pelatih:list_atlet')
            else:
                context = ['Error: Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu']
                return render(request, 'daftar_atlet_pelatih.html', {'atlet_list': list_atlet, 'context': context})

        return render(request, 'daftar_atlet_pelatih.html', {'atlet_list': list_atlet})

    else:
        return render(request, 'daftar_atlet_pelatih.html')
    
def convert_dict_to_list(data_dict):
    data_list = []
    
    for i in range(len(data_dict['id'])):
        data = []
        data.append(data_dict['nama'][i])
        data.append(data_dict['id'][i])
        data_list.append(data)
    
    return data_list