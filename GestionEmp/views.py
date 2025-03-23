from django.shortcuts import render


def accueil(request):
    return render(request, 'login.html')

def userdashboard(request):
    return render(request, 'emp/dashboard.html')