from django.shortcuts import render


def index(request):
    return render(request, 'emp/conges/congesdetails.html')