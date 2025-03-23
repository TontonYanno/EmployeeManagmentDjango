from Conges import views
from django.urls import path
urlpatterns = [    
    path('',views.mesconges , name='mesconges'),
    path('historique/',views.historique , name='historique'),
    path('detail/',views.detail , name='detail'),
 
]