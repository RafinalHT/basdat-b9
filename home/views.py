from django.shortcuts import render, redirect

def main(request):
    # Temporary role authorization logic
    email = 'babadu@ui.ac.id'
    is_atlet = True
    is_pelatih = False
    is_umpire = False
    
    # Set session variables based on role
    request.session['email'] = email
    request.session['is_atlet'] = is_atlet
    request.session['is_pelatih'] = is_pelatih
    request.session['is_umpire'] = is_umpire
    
    # Redirect to dashboard if user has a role
    if is_atlet or is_pelatih or is_umpire:
        return redirect('dashboard:dashboard')
    
    return render(request, 'index.html')