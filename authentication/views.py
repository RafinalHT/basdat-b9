from django.http import HttpResponse, HttpResponseRedirect
import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from utils import query
from django.views.decorators.csrf import csrf_exempt

def get_role(id):
    if query.query(f"select * from pelatih where id = '{id}'"):
        return "pelatih"
    elif query.query(f"select * from atlet where id = '{id}'"):
        return "atlet"
    elif query.query(f"select * from umpire where id = '{id}'"):
        return "umpire"
    
@csrf_exempt 
def login(request):
    if request.method == "POST":
        nama = request.POST.get("nama")
        email = request.POST.get("email")
        request.session['is_atlet'] = False
        request.session['is_pelatih'] = False
        request.session['is_umpire'] = False
        print(query.query(f"select id from member where email = '{email}' and nama='{nama}'"))
        if query.query(f"select*from member where email = '{email}' and nama='{nama}'"):
            id=query.query(f"select id from member where email = '{email}' and nama='{nama}'")
            x=(id[0][0])
            role=get_role(x)
            print(role)
            if role=="atlet":
                 request.session['is_atlet'] = True
            elif role=="pelatih":
                 request.session['is_pelatih'] = True
            elif role=="umpire":
                 print(2)
                 request.session['is_umpire'] = True
            response= HttpResponseRedirect("/dashboard")
            response.set_cookie('id',x)
            response.set_cookie('role',role)
            print(request.session['is_umpire'])
            print(request.session['is_atlet'])
            print(request.session['is_pelatih'])
            return response
        else: 
            return render(request, "login.html", {"Error": "Nama atau Email salah"})
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

@csrf_exempt
def register_atlet(request):
    if request.method == 'POST':
        print(3)
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        negara = request.POST.get('negara')
        tanggal_lahir = request.POST.get('tanggal_lahir')
        play = request.POST.get('play')
        tinggi_badan = request.POST.get('tinggi_badan')
        jenis_kelamin = request.POST.get('jenis_kelamin')
        id = uuid.uuid4()
        context = {}
        response = query.query(
        f"""insert into member (id,nama,email)
        values ('{id}','{nama}','{email}')""")
    
        if type(response) is not str:
            context['error'] = 'Error: Email sudah terdaftar' 
            return render(request, "register_atlet.html", context)

                
            
        response = query.query(
        f"""insert into atlet(id, tgl_lahir, negara_asal, play_right, height, jenis_kelamin)
        values ('{id}','{tanggal_lahir}','{negara}', '{eval(play)}', '{tinggi_badan}', '{eval(jenis_kelamin)}')""")
        print(response)
        
        if type(response) is not str:
            return HttpResponse(f"Error: {response}")
        

        return redirect("authentication:login")
    return render(request, "register_atlet.html")

@csrf_exempt
def register_pelatih(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        kategori = request.POST.getlist('kategori')
        tanggal_mulai = request.POST.get('tanggal_mulai')
        print(nama)
        print(email)
        print(kategori)
        print(tanggal_mulai)
        id = uuid.uuid4()
        context = {}
        response = query.query(
        f"""insert into member (id,nama,email)
        values ('{id}','{nama}','{email}')""")
    
        if type(response) is not str:
            context['error'] = 'Error: Email sudah terdaftar' 
            return render(request, "register_pelatih.html", context)
            
        response = query.query(
        f"""insert into pelatih(id, tanggal_mulai)
        values ('{id}','{tanggal_mulai}')""")
    
        if type(response) is not str:
            return HttpResponse(f"Error: {response}")
        print(kategori)
        for i in kategori:
            print(i)
            response = query.query(
            f"""insert into pelatih_spesialisasi(id_pelatih, id_spesialisasi)
            select '{id}', id from spesialisasi where spesialisasi='{i}'""")
    
            if type(response) is not str:
                return HttpResponse(f"Error: {response}")
            
        
        return redirect("authentication:login")
    return render(request, "register_pelatih.html")
           
@csrf_exempt
def register_umpire(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        negara = request.POST.get('negara')
        print(nama)
        print(email)
        print(negara)
        id = uuid.uuid4()
        context = {}
        response = query.query(
        f"""insert into member (id,nama,email)
        values ('{id}','{nama}','{email}')""")
    
        if type(response) is not str:
            context['error'] = 'Error: Email sudah terdaftar' 
            return render(request, "register_umpire.html", context)
                
            
        response = query.query(
        f"""insert into umpire(id, negara)
        values ('{id}','{negara}')""")
    
        if type(response) is not str:
            return HttpResponse(f"Error: {response}")
       
        
        
        return redirect("authentication:login")
    return render(request, "register_umpire.html")
           
    
@csrf_exempt
def logout(request):
    response = HttpResponseRedirect("/")
    response.delete_cookie('id')
    response.delete_cookie('role')
    request.session['is_atlet'] = False
    request.session['is_pelatih'] = False
    request.session['is_umpire'] = False
    return response
