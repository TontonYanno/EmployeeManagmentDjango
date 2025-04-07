from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from Conges.models import Conges
from User.models import Utilisateur
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def mesconges(request):
    conges= Conges.objects.all()
    users = Utilisateur.objects.all()
    return render(request, 'emp/conges/conges.html' , {"conges":conges, "users":users}) #affichage de la page d'édition de la tâche

def mes_conges(request ):
    if request.method == 'POST':
        type = request.POST.get('type')
        description = request.POST.get('description')
        debut = request.POST.get('debut')
        fin = request.POST.get('fin')
     
        conge = Conges(type=type, description=description, debut=debut, fin=fin, user=request.user)  # Utiliser request.user pour l'utilisateur connecté
        conge.save()
        
        messages.success(request, "Demande de congé envoyée avec succès.")
    return render(request, 'emp/conges/conges.html' ) #affichage de la page d'édition de la tâche

@login_required
def historique(request):
    conges= Conges.objects.filter(user=request.user)
    return render(request, 'emp/conges/congeshistorique.html', {"conges":conges})

@login_required
def detail(request , id):
    conge = get_object_or_404(Conges, id=id , user=request.user)  # Filtrer par utilisateur
    return render(request, 'emp/conges/congesdetails.html' , {"conge":conge}) #affichage de la page d'édition de la tâche

#Les Vues de l'admin

def listconges (request):
    conges= Conges.objects.all()
    users = Utilisateur.objects.all()
    return render (request, 'admin/gestionconges/conges.html', {"conges":conges, "users":users}) #affichage de la page d'édition de la tâche

def detailconges(request, id):
    conges = get_object_or_404(Conges, id=id)  # Filtrer par utilisateur
    users= get_object_or_404(Utilisateur, id=conges.user.id)  # Filtrer par utilisateur
    return  render (request, 'admin/gestionconges/congesdetails.html' , {"conges":conges, "users":users}) #affichage de la page d'édition de la tâche

def detail_conges(request, id):
    conge= get_object_or_404(Conges, id=id)
    if request.method== 'POST':
        if 'valider' in request.POST:
            conge.statut='accepte'
            conge.manager_reponse=request.POST.get('manager_reponse')
            conge.date_reponse= now()
            conge.vu=True
            conge.save()
            messages.success(request, "Demande de congé acceptée avec succès.")
            redirect('detailconges', id=conge.id)
            
        else :
            conge.statut='refuse'
            conge.manager_reponse=request.POST.get('manager_reponse')
            conge.date_reponse= now()
            conge.vu=True
            conge.save()
            messages.success(request, "Demande de congé acceptée avec succès.")
            redirect('detailconges', id=conge.id)
    return render(request, 'admin/gestionconges/congesdetails.html' , {"conge":conge}) #affichage de la page d'édition de la tâche        