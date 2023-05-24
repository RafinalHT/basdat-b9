from django.shortcuts import render

def lihat_event_view(request):
    return render(request, 'lihat_event.html')

def perempat_final_view(request):
    return render(request, 'perempat_final.html')

def semifinal_view(request):
    return render(request, 'semifinal.html')

def final_view(request):
    return render(request, 'final.html')