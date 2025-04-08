from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from Taches.models import Tache
from User.models import Utilisateur
from django.utils.timezone import now
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

#Les Vues Taches de l'employé

def mytasks(request):
    taches= Tache.objects.filter(user=request.user, archive='non')  
    return render(request, 'emp/tache/taches.html', {"taches":taches})

def myarchive(request):
    taches = Tache.objects.filter(user=request.user, archive='oui')  
    return render(request, 'emp/tache/etat/archive.html', {"taches":taches}) #pour les taches archivées

def mycourant(request):
    taches = Tache.objects.filter(user=request.user).filter(Q(statut='en_attente')|Q(statut='en_cours')) 
    return render(request, 'emp/tache/etat/courant.html',{"taches":taches}) #pour les taches courante(en cours et en attente)

def myretard(request):
    today = now().date()
    taches = Tache.objects.filter(user=request.user,archive='non',date_limite__lt= today).filter(Q(statut='en_attente') | Q(statut='en_cours'))
    return render(request, 'emp/tache/etat/retard.html', {"taches":taches} ) #pour les taches les taches en retard

def editmytasks(request , id):
    tache= get_object_or_404(Tache, id=id , user=request.user)  # Filtrer par utilisateur
    return render(request, 'emp/tache/editaches.html', {"tache":tache}) #affichage de la page d'édition de la tâche

def update_mytask(request, id):
    tache = get_object_or_404(Tache, id=id , user=request.user)  # Filtrer par utilisateur
    if request.method == 'POST':
        tache.statut = request.POST.get('statut')
        tache.save()
        messages.success(request, "Tâche mise à jour avec succès.")
        redirect('editmytasks', id=tache.id)
    return render(request, 'emp/tache/editaches.html', {'tache': tache})  # Afficher le formulaire de mise à jour

def archivetasks(request , id):
    tache = get_object_or_404(Tache, id=id, user=request.user)
    return render(request, 'emp/tache/archivetaches.html', {"tache":tache}) #affichage de la page d'archivage

def archive_tasks(request , id):
    tache = get_object_or_404(Tache, id=id , user = request.user)
    if request.method == 'POST':
        tache.archive= 'oui'
        tache.mention_archive=request.POST.get('mention')
        tache.save()
        messages.success(request, "Tâches archivé avec succès")
        redirect('archivetasks',id=tache.id)
    return render(request, 'emp/tache/archivetaches.html', {"tache":tache})        

#Les Vues de l'admin 

@login_required
def listtasks(request):
    taches= Tache.objects.all().filter(archive='non')  
    return render (request, 'admin/gestiontaches/listache.html',{"taches":taches})

def archive(request):
    taches= Tache.objects.all().filter(  archive= "oui" )  
    return render(request, 'admin/gestiontaches/etat/archive.html' , {"taches":taches}) #pour afficher les taches archivées

def courant(request):
    taches= Tache.objects.all().filter( Q(statut= "en_cours")|Q(statut="en_attente") )  
    return render(request, 'admin/gestiontaches/etat/courant.html', {"taches":taches}) #pour afficher les taches courantes

def retard(request):
    today = now().date()
    taches = Tache.objects.all().filter(archive='non',date_limite__lt= today).filter(Q(statut='en_attente') | Q(statut='en_cours'))
    return render(request, 'admin/gestiontaches/etat/retard.html' , {"taches":taches}) 

@login_required
def add_task(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        date_limite = request.POST.get('date_limite')
        user_id = request.POST.get('user')  # Récupérer l'ID de l'utilisateur
        user = Utilisateur.objects.get(id=user_id)  # Obtenir l'utilisateur correspondant
        
        # Créer la tâche
        tache = Tache(titre=titre, description=description, date_limite=date_limite,  user=user)
        tache.save()
        messages.success(request, "Tâche ajoutée avec succès.")

    return redirect('addtasks')  # Rediriger vers la page d'ajout de tâche après la création

@login_required
def addtask(request):
    users= Utilisateur.objects.all()
    taches=Tache.objects.all()
    return render(request, 'admin/gestiontaches/addtaches.html',{"taches":taches,"users":users})

@login_required
def edittask (request, id):
    tache= get_object_or_404(Tache, id=id)
    users= get_object_or_404(Utilisateur, id=tache.user.id)
    test= Utilisateur.objects.all()
    return render (request, 'admin/gestiontaches/editaches.html', {"tache":tache, "users":users , "test":test}) #affichage de la page d'édition de la tâche

@login_required
def update_task(request, id):
    tache = get_object_or_404(Tache, id=id)
    if request.method == 'POST':
        if request.POST.get('date_limite')== "":
            messages.error(request, "La date limite ne peut pas être vide.")
            redirect('edittask', id=tache.id)
        elif request.POST.get('titre')== "":
            messages.error(request, "Le titre ne peut pas être vide.")
            redirect('edittask', id=tache.id)
        elif request.POST.get('description')== "":  
            messages.error(request, "La description ne peut pas être vide.")
            redirect('edittask', id=tache.id)
        elif request.POST.get('user')== "":
            messages.error(request, "L'utilisateur ne peut pas être vide.")
            redirect('edittask', id=tache.id)  
        else:
            tache.titre = request.POST.get('titre')
            tache.description = request.POST.get('description')
            tache.date_limite = request.POST.get('date_limite')
            tache.user = Utilisateur.objects.get(id=request.POST.get('user'))  # Récupérer l'utilisateur correspondant
            tache.save()
            messages.success(request, "Tâche mise à jour avec succès.")
            redirect('edittask', id=tache.id)  
    return render(request, 'admin/gestiontaches/editaches.html', {'tache': tache})  # Afficher le formulaire de mise à jour

@login_required
def delete_task(request, id):
    tache = get_object_or_404(Tache, id=id)
    tache.delete()
    messages.success(request, "Tâche supprimée avec succès.")
    return redirect('listtasks')  # Rediriger vers la liste des tâches après la suppression
