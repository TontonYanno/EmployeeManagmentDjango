from django.shortcuts import render


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
    return render(request, 'admin/gestiontaches/addtaches.html')

def listtasks(request):
    return render (request, 'admin/gestiontaches/listache.html')

def edittask (request):
    return render (request, 'admin/gestiontaches/editaches.html')