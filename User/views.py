from django.shortcuts import render

# Create your views here.

#Les Vues User ou Profils de l'employé

def myprofile(request):
    return render(request, 'emp/profile/profile.html')

def changepassword(request):
    return render(request, 'emp/profile/editprofile.html')
