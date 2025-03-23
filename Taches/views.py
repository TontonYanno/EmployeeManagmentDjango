from django.shortcuts import render


# Create your views here.

#Les Vues Taches de l'employé

def mytasks(request):
    return render(request, 'emp/tache/taches.html')

def editmytasks(request):
    return render(request, 'emp/tache/editaches.html')

def archivetasks(request):
    return render(request, 'emp/tache/archivetaches.html')