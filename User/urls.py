from User import views
from django.urls import path

urlpatterns = [
    path('', views.myprofile, name='myprofile'),
    path('changepassword/', views.changepassword, name='changepassword'),
    
    
]
