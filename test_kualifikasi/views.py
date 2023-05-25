from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from utils import query
from django.contrib import messages
import datetime
def buat_ujian(request):
    if request.method == 'POST':
        tahun = request.POST.get('tahun')
        batch = request.POST.get('batch')
        tempat = request.POST.get('tempat')
        tanggal = request.POST.get('tanggal')
        context={}
        print(tahun)
        print(batch)
        print(tempat)
        print(tanggal)
        check =query.query(f"""select tahun,batch,tempat,tanggal from ujian_kualifikasi 
                           where tahun = '{tahun}' and batch = '{batch}' and tempat = '{tempat}' 
                            and tanggal = '{tanggal}'  """)
        if check==[]:
            response = query.query(
                f"""insert into ujian_kualifikasi (tahun,batch,tempat, tanggal)
                values ('{tahun}','{batch}','{tempat}','{tanggal}')""")
            
            if type(response) is not str:
                return HttpResponse(f"Error: {response}")
            response= redirect('tes_kualifikasi:list_ujian')
           
            return response
        else:
            context['error'] = 'Error: Ujian sudah terdaftar' 
            return render(request, "form_data.html", context)
    return render(request, 'form_data.html')

def list_ujian(request):
    if request.method == 'POST':
          data = eval(request.POST.get('action'))
          
          tahun = data['tahun']
          batch = data['batch']
          tempat = data['tempat']
          tanggal = data['tanggal']
          print(tahun)
          print(batch)
          print(tempat)
          print(tanggal)
          response= redirect('tes_kualifikasi:pertanyaan')
          response.set_cookie('tahun', tahun)
          response.set_cookie('batch', batch)
          response.set_cookie('tempat', tempat)
          response.set_cookie('tanggal', tanggal)
          return response
    data = query.query(f"select tahun,batch,tempat,tanggal from ujian_kualifikasi")
    print("data s:", data)
    result = [{'tahun': item[0], 'batch': item[1], 'tempat': item[2], 'tanggal': item[3]} for item in data]

    return render(request, 'list_ujian.html', context = {'list_ujian': result})




def pertanyaan_kualifikasi_view(request):
    if request.method == 'POST':
        result=0
        pertanyaan1 =request.POST.get('pertanyaan1')
        pertanyaan2 =request.POST.get('pertanyaan2')
        pertanyaan3 =request.POST.get('pertanyaan3')
        pertanyaan4 =request.POST.get('pertanyaan4')
        pertanyaan5 =request.POST.get('pertanyaan5')
        context={}
        id = request.COOKIES['id']
        tahun = request.COOKIES['tahun']
        batch = request.COOKIES['batch']
        tempat = request.COOKIES['tempat']
        tanggal = request.COOKIES['tanggal']
        if(pertanyaan1 == None):
            pertanyaan1=0
        if(pertanyaan2 == None):
            pertanyaan2=0
        if(pertanyaan3 == None):
            pertanyaan3=0
        if(pertanyaan4 == None):
            pertanyaan4=0
        if(pertanyaan5 == None):
            pertanyaan5=0
        result= int(pertanyaan1)+int(pertanyaan2)+int(pertanyaan3)+int(pertanyaan4)+int(pertanyaan5)
        print(result)
        status = False
        if result>=4:
            status = True
        print(id)
        print(tahun)
        print(batch)
        print(tempat)
        print(tanggal)
        print(status)
        response = query.query(
                f"""insert into atlet_nonkualifikasi_ujian_kualifikasi
                (id_atlet,tahun,batch,tempat, tanggal,hasil_lulus)
                 values ('{id}','{tahun}','{batch}','{tempat}','{tanggal}','{status}')""")
        print(response)
        if type(response) is not str:
            context['error'] = 'Maaf, Anda tidak dapat mengikuti ujian kualifikasi ini.'
            return render(request, "pertanyaan.html", context)
        response= redirect('tes_kualifikasi:riwayat')
        response.set_cookie('hasil', status)
        return response
        
    return render(request, 'pertanyaan.html')

def riwayat(request):
    if request.COOKIES['role']=='atlet':
        id = request.COOKIES['id']
        data = query.query(f"""select tahun,batch,tempat,tanggal,
        case
        when hasil_lulus = true THEN 'Lulus'
        when hasil_lulus = false THEN 'Tidak Lulus'
        end as hasil_lulus
        from atlet_nonkualifikasi_ujian_kualifikasi 
        where id_atlet = '{id}'
                           """)
        print(data==[])
        if data==[]:
            print(4)
            result={}
            status={'status': True }
        else:
            result = [{'tahun': item[0], 'batch': item[1], 'tempat': item[2], 'tanggal': item[3],'hasil': item[4]} for item in data]
            status={}
    elif request.COOKIES['role']=='umpire':
        data = query.query(f"""select nama,tahun,batch,tempat,tanggal,
        case
        when hasil_lulus = true THEN 'Lulus'
        when hasil_lulus = false THEN 'Tidak Lulus'
        end as hasil_lulus
        from atlet_nonkualifikasi_ujian_kualifikasi an, member m, atlet_non_kualifikasi a, atlet at
        where an.id_atlet = a.id_atlet and a.id_atlet = at.id and at.id = m.id
                           """)
        print(data)
        result = [{'nama': item[0],'tahun': item[1], 'batch': item[2], 'tempat': item[3], 'tanggal': item[4],'hasil': item[5]} for item in data]
        print(result)
        status={}
        
    return render(request, 'riwayat.html',context = {'list': result, 'status':status})

