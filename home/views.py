from django.shortcuts import render, redirect

def main(request):
    is_atlet = False
    is_pelatih = False
    is_umpire = False
    
    request.session['is_atlet'] = is_atlet
    request.session['is_pelatih'] = is_pelatih
    request.session['is_umpire'] = is_umpire
    
    # Redirect to dashboard if user has a role
    if is_atlet or is_pelatih or is_umpire:
        return redirect('dashboard:dashboard')
    
    return render(request, 'index.html')