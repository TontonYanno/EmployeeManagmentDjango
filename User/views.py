from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate , login , logout



# Create your views here.

#Les Vues User ou Profils de l'employé
@login_required
def myprofile(request):
    user= request.user
    return render(request, 'emp/profile/profile.html',{"user":user})

@login_required
def editprofile(request):
    user= request.user
    return render(request, 'emp/profile/editprofile.html', {"user":user})


# @login_required
def change_password(request):
    if request.method == "POST":
        
        password = request.POST.get("password")
        user= request.user
        password_hashed = user.password
        
        # Vérifie si le mot de passe actuel est correct
        if not check_password(password, password_hashed):
            messages.error(request, "Mot de passe actuel incorrect.")
            return redirect("editprofile")  # Redirige vers la page de changement de mot de passe
        else:
            # Si le mot de passe actuel est correct, on peut changer le mot de passe
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")

            if new_password == confirm_password:
                request.user.set_password(new_password)
                request.user.save()
                # Garde l'utilisateur connecté après le changement de mot de passe
                # update_session_auth_hash(request, request.user)
                messages.success(request, "Mot de passe changé avec succès !")
                return redirect("editprofile")  # Redirige vers le dashboard après changement
            else:
                messages.error(request, "Les mots de passe ne correspondent pas.")
    return render(request, "emp/profile/editprofile.html")


#Les Vues Admin
def users(request):
    return render(request, 'admin/gestionuser/adduser.html')

def listusers(request):
    return render (request, 'admin/gestionuser/listuser.html')

def edituser(request):
    return render(request, 'admin/gestionuser/edituser.html')
