from django.shortcuts import render

from sponsor.forms import SponsorForm

# Create your views here.

def daftar_sponsor(request):
    if request.method == 'POST':
        form = SponsorForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = SponsorForm()
        
    context = {'form':form}
    return render(request, 'daftar_sponsor.html', context)
