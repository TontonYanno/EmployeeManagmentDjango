from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from Taches.models import Tache
from User.models import Utilisateur
from django.contrib.auth.decorators import login_required


# Create your views here.

#Les Vues Taches de l'employé

def mytasks(request):
    return render(request, 'emp/tache/taches.html')

def editmytasks(request):
    return render(request, 'emp/tache/editaches.html')

def archivetasks(request):
    return render(request, 'emp/tache/archivetaches.html')

#Les Vues de l'admin 

def addtask(request):
    users= Utilisateur.objects.all()
    taches=Tache.objects.all()
    return render(request, 'admin/gestiontaches/addtaches.html',{"taches":taches,"users":users})

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
def listtasks(request):
    taches= Tache.objects.all()
    return render (request, 'admin/gestiontaches/listache.html',{"taches":taches})

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

def delete_task(request, id):
    tache = get_object_or_404(Tache, id=id)
    tache.delete()
    messages.success(request, "Tâche supprimée avec succès.")
    return redirect('listtasks')  # Rediriger vers la liste des tâches après la suppression
