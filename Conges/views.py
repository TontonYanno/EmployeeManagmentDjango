from django.shortcuts import render

# Create your views here.

def mesconges(request):
    return render(request, 'emp/conges/conges.html')

def historique(request):
    return render(request, 'emp/conges/congeshistorique.html')

def detail(request):
    return render(request, 'emp/conges/congesdetails.html')

#Les Vues de l'admin

def listconges (request):
    return render (request, 'admin/gestionconges/conges.html')

def detailconges(request):
    return  render (request, 'admin/gestionconges/congesdetails.html' )