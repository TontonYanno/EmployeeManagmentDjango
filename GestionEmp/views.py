from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login , logout

from django.contrib import messages

#La fonction de login

def conexion(request):
    if request.method == "POST":
        username= request.POST.get('username')
        # email = request.POST.get("email")
        password = request.POST.get("password")
        # print( username +"|"+ password)
        user = authenticate(request, username=username , password= password)
        print(user)
        
        if user is not None:
            login(request, user)
            if user.role == 'manager':
                return redirect("dashboard") # Vers dasbord admin 
            else:
                return redirect("userdashboard") # Vers dashboard employe
        else:
            messages.error(request, "Email ou mot de passe incorrecte")        
            
    return render(request, 'login.html')


def deconnexion(request):
    logout (request)
    return redirect ("login")

#----------------------------------------------------------------------------------------------

def userdashboard(request):
    return render(request, 'emp/dashboard.html')

def dashboard(request):
    return render(request, 'admin/dashboard.html')