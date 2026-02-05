from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import is_password_usable
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from User.models import Utilisateur
from django.core.mail import send_mail
from django.conf import settings


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
@login_required
def users(request):
    user= request.user
    return render(request, 'admin/gestionuser/adduser.html',{"user":user})

def register(request):
    if request.method == 'POST':
        #Traitemant pour automatiser le matricule
        def generate_matricule():
            prefix = "EMP"
            numero = Utilisateur.objects.count() + 1
            matricule = f"{prefix}{numero:03d}"
            return matricule
        
        username = request.POST.get('username')
        nom_complet = request.POST.get('nom_complet')
        email = request.POST.get('email')
        sexe = request.POST.get('sexe')
        matricule = generate_matricule()
        telephone = request.POST.get('telephone')
        adresse = request.POST.get('adresse')
        date_naissance = request.POST.get('date_naissance')
        role = request.POST.get('role')
        password = request.POST.get('password')
      
        if Utilisateur.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà utilisé. Veuillez en choisir un autre.")
            return redirect("addusers")
        if Utilisateur.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
            return redirect("addusers")
        if Utilisateur.objects.filter(telephone=telephone).exists():
            messages.error(request, "Ce numéro de téléphone est déjà utilisé.")
            return redirect("addusers")
        
        # Enregistrement de l'utilisateur
        user = Utilisateur.objects.create_user(username=username,email=email,nom_complet=nom_complet,sexe=sexe,telephone=telephone,adresse=adresse,date_naissance=date_naissance,role=role,password=password,matricule=matricule,)
        user.save()
         # ✅ Envoi de mail
        send_mail(
            subject="Bienvenue sur votre espace de travail",
            message=f"Bonjour M/Mme {username},\n\nNous sommes ravis de vous accueillir sur notre plateforme. Votre compte a été activé avec succès.\n\nVoici vos informations de connexion :\n\nNom d'utilisateur : {username}\nMot de passe : {password}\n\nNous vous recommandons de changer votre mot de passe après votre première connexion.\n\nCordialement,\nL'équipe de [Nom de l'entreprise]",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )
        
        messages.success(request, "Utilisateur ajouté avec succès !")
        return redirect('listusers')  # Redirige vers la liste des utilisateurs
    
    return render(request, 'admin/gestionuser/adduser.html')


def update_user(request, id):
    user = get_object_or_404(Utilisateur, id=id)
    if request.method == 'POST':
        if user.password != request.POST.get('password'): # Vérifie si le mot de passe a été modifié
            # Si le mot de passe a été modifié, on le hache avant de l'enregistrer
            user.username = request.POST.get('username')
            user.nom_complet = request.POST.get('nom_complet')
            user.email = request.POST.get('email')
            user.sexe = request.POST.get('sexe')
            user.telephone = request.POST.get('telephone')
            user.adresse = request.POST.get('adresse')
            user.date_naissance = request.POST.get('date_naissance')
            user.role = request.POST.get('role')
            user.password = request.POST.get('password')
            # Hachage du mot de passe avant de l'enregistrer
            user.password=make_password(user.password)
            
            # Enregistrement des modifications
            user.save()
            messages.success(request, "Utilisateur modifié avec succès !")
            return redirect('listusers')  # Redirige vers la liste des utilisateurs
            
        else:
            # Si le mot de passe n'a pas été modifié, on ne le change pas
            user.username = request.POST.get('username')
            user.nom_complet = request.POST.get('nom_complet')
            user.email = request.POST.get('email')
            user.sexe = request.POST.get('sexe')
            user.telephone = request.POST.get('telephone')
            user.adresse = request.POST.get('adresse')
            user.date_naissance = request.POST.get('date_naissance')
            user.role = request.POST.get('role')
            # Enregistrement des modifications
            user.save()
            messages.success(request, "Utilisateur modifié avec succès !")
            return redirect('listusers')  # Redirige vers la liste des utilisateurs
    return render(request, 'admin/gestionuser/edituser.html', {"user":user})

def delete_user(request, id):
    user = get_object_or_404(Utilisateur, id=id)
    
    user.delete()
    messages.success(request, "Utilisateur supprimé avec succès !")
    return redirect('listusers')  # Redirige vers la liste des utilisateurs

@login_required
def listusers(request):
    user= request.user
    users = Utilisateur.objects.all()
    return render (request, 'admin/gestionuser/listuser.html',{"user":user,"users":users})

def edituser(request,id):
    user = get_object_or_404(Utilisateur, id=id)
    return render(request, 'admin/gestionuser/edituser.html', {"user":user})
