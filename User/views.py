from django.shortcuts import render

# Create your views here.

#Les Vues User ou Profils de l'employé

# def myprofile(request):
#     return render(request, 'emp/profile/profile.html')

# def changepassword(request):
#     return render(request, 'emp/profile/editprofile.html')

# #Les Vues Admin
# def users(request):
#     return render(request, 'admin/gestionuser/adduser.html')

# def listusers(request):
#     return render (request, 'admin/gestionuser/listuser.html')

# def edituser(request):
#     return render(request, 'admin/gestionuser/edituser.html')
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def redirect_user(request):
    # Vérifie le rôle de l'utilisateur et redirige vers le bon tableau de bord
    if request.user.is_employee:  # Si l'utilisateur est un employé
        return redirect('employee_dashboard')  # Redirige vers le tableau de bord de l'employé
    else:  # Si ce n'est pas un employé, c'est un manager
        return redirect('manager_dashboard')  # Redirige vers le tableau de bord du manager



@login_required
def employee_dashboard(request):
    return render(request, 'emp/dashboard.html')

@login_required
def manager_dashboard(request):
    return render(request, 'admin/dashboard.html')

