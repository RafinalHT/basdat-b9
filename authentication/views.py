from django.shortcuts import render
from authentication.forms import *

def login(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        pass
    context = {'login_form': LoginForm()}
    return render(request, 'login.html', context)


def register_atlet(request):
    context = {
        'atlet_form': RegisterAtletForm(),
    }
    return render(request, 'register_atlet.html', context)

def register_pelatih(request):
    context = {
        'pelatih_form': RegisterPelatihForm(),
    }
    return render(request, 'register_pelatih.html', context)
def register_umpire(request):
    context = {
        'umpire_form': RegisterUmpireForm(),
    }
    return render(request, 'register_umpire.html', context)

def register(request):
    return render(request, 'register.html')
