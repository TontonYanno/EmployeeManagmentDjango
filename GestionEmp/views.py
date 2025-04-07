from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.timezone import now
from django.db.models import Q
from Taches.models import Tache
from User.models import Utilisateur

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
                return redirect("userdashboard" ) # Vers dashboard employe
        else:
            messages.error(request, "Email ou mot de passe incorrecte")        
            
    return render(request, 'login.html')

@login_required
def deconnexion(request):
    logout (request)
    return redirect ("login")

#----------------------------------------------------------------------------------------------

@login_required
def userdashboard(request):
    total=Tache.objects.filter(user=request.user).count()
    en_attente=Tache.objects.filter(user=request.user, statut='en_attente').count()
    en_cours=Tache.objects.filter(user=request.user, statut='en_cours').count()
    en_retard=Tache.objects.filter(user=request.user, date_limite__lt=now().date()).filter(Q( statut='en_attente')|Q( statut='en_cours')).count()
    return render(request, 'emp/dashboard.html', {'total':total, 'en_attente':en_attente, 'en_cours':en_cours, 'en_retard':en_retard})

@login_required
def dashboard(request):
    emp=Utilisateur.objects.filter( role="employe").count()
    all_task=Tache.objects.all().count()
    retard= Tache.objects.filter(date_limite__lt=now().date()).filter(Q( statut='en_attente')|Q( statut='en_cours')).count()
    en_attente=Tache.objects.filter( statut='en_attente').count()
    en_cours=Tache.objects.filter( statut='en_cours').count()
    termine= Tache.objects.filter(statut="terminee").count()
    return render(request, 'admin/dashboard.html', {'emp':emp, 'all_task':all_task, "retard":retard , 'en_attente':en_attente, 'en_cours':en_cours,'termine':termine,})