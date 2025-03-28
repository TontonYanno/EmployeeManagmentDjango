from User import views
from django.urls import path

# urlpatterns = [
#     #Les routes pour l'employé
#     path('myprofile', views.myprofile, name='myprofile'),
#     path('changepassword/', views.changepassword, name='changepassword'),
    
#     #Les routes pour l'admin
#     path('adduser/', views.users, name='addusers'),
#     path('listusers/', views.listusers, name='listusers'),
#     path('edituser/', views.edituser, name='edituser'),
    
# ]
from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
     path('login/', LoginView.as_view(), name='login'),  # Connexion
     path('logout/', LogoutView.as_view(), name='logout'),
    path('redirect-user/', views.redirect_user, name='redirect-user'),  # Redirection après la connexion
    path('dashboard/employee/', views.employee_dashboard, name='employee_dashboard'),
    path('dashboard/manager/', views.manager_dashboard, name='manager_dashboard'),
    # Ajoutez d'autres URLs nécessaires pour votre application
]

