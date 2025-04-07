from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from Conges.models import Conges

# Create your views here.

def mesconges(request):
    return render(request, 'emp/conges/conges.html')

def historique(request):
    conges= Conges.objects.filter(user=request.user)
    return render(request, 'emp/conges/congeshistorique.html', {"conges":conges})

def detail(request , id):
    conge = get_object_or_404(Conges, id=id , user=request.user)  # Filtrer par utilisateur
    return render(request, 'emp/conges/congesdetails.html' , {"conge":conge}) #affichage de la page d'édition de la tâche

#Les Vues de l'admin

def listconges (request):
    return render (request, 'admin/gestionconges/conges.html')

def detailconges(request):
    return  render (request, 'admin/gestionconges/congesdetails.html' )