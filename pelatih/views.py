from django.shortcuts import redirect, render
from utils import query
from django.db import connection

from pelatih.forms import AtletPelatihForm

# Create your views here.
def daftar_atlet_pelatih(request):
    atlet_list = ["Dummy Atlet 1", "Dummy Atlet 2", "Dummy Atlet 3"]
    if request.method == 'POST':
        form = AtletPelatihForm(request.POST)
        if form.is_valid():
            pass
        return redirect('pelatih:list_atlet')
    else:
        form = AtletPelatihForm()

    context = {'form':form, 'atlet_list':atlet_list}
    return render(request, 'daftar_atlet_pelatih.html', context)

def list_atlet(request):
    atlet_list = [
        {'name': 'John', 'email': 'john@example.com', 'world_rank': 1},
        {'name': 'Jane', 'email': 'jane@example.com', 'world_rank': 2},
        {'name': 'Bob', 'email': 'bob@example.com', 'world_rank': 3},
        {'name': 'Alice', 'email': 'alice@example.com', 'world_rank': 4},
    ]
    context = {'atlet_list': atlet_list}
    return render(request, 'list_atlet.html', context)


def daftar_atlet(request):
    if request.COOKIES['role']=='umpire':
        datar_atlet = query.query(f"select a.id, m.nama from member m, atlet a where m.id = a.id;")
                                                    
        id = [record[0] for record in datar_atlet]
        nama = [record[1] for record in datar_atlet]
        
        data = {
            'id' : id,
            'nama' : nama,
        }

        return render(request, 'daftar_atlet.html', {'data': data})
    else:
        return render(request, 'daftar_atlet.html')