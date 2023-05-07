from django.shortcuts import render

# Create your views here.
def pilih_stadium(request):
    return render(request, 'pilih_stadium.html')

def pilih_event(request):
    return render(request, 'pilih_event.html')

def pilih_kategori(request):
    return render(request, 'pilih_kategori.html')