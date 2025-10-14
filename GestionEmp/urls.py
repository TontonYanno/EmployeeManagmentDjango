"""
URL configuration for GestionEmp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from GestionEmp import views
from django.conf.urls.static import static
urlpatterns = [
    #Les connexions
    path('admin/', admin.site.urls),
    path ('',views.conexion , name='login'),
    path('logout/',views.deconnexion, name='logout'),
    # Dashboard de l'employé 
    path('mydashboard',views.userdashboard , name='userdashboard'),
    # Dashboard de l'admin 
    path ('dashboard/', views.dashboard , name='dashboard'),
    
    path('tasks/', include('Taches.urls')),
    path('user/', include('User.urls')),
    path('conges/', include('Conges.urls')),
 ]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

