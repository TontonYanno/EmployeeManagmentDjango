from User import views
from django.urls import path

urlpatterns = [
    #Les routes pour l'employé
    path('myprofile', views.myprofile, name='myprofile'),
    path('changepassword/', views.editprofile, name='editprofile'),
    path('change_password/', views.change_password, name='change_password'), #le traitement du changement de mot de passe
    path('changephoto/', views.editphoto, name='editphoto'),
    path('change_photo/', views.change_photo, name='change_photo'), #le traitement du changement de photo de profil
    
    #Les routes pour l'admin
    path('adduser/', views.users, name='addusers'),
    path('add_user/', views.register, name='add_user'), #le traitement de l'ajout d'un utilisateur
    path('listusers/', views.listusers, name='listusers'),
    path('edituser/<int:id>/', views.edituser, name='edituser'), #affichage
    path('update_user/<int:id>/', views.update_user, name='update_user'), #le traitement de la modification d'un utilisateur
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'), #le traitement de la suppression d'un utilisateur
    
  
]
