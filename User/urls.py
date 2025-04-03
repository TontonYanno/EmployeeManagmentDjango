from User import views
from django.urls import path

urlpatterns = [
    #Les routes pour l'employé
    path('myprofile', views.myprofile, name='myprofile'),
    
    path('changepassword/', views.editprofile, name='editprofile'),
    path('change_password/', views.change_password, name='change_password'),
    
    #Les routes pour l'admin
    path('adduser/', views.users, name='addusers'),
    path('listusers/', views.listusers, name='listusers'),
    path('edituser/', views.edituser, name='edituser'),
    
]
