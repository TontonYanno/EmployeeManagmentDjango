from Conges import views
from django.urls import path
urlpatterns = [  
    #Les routes de l'employé  
    path('mesconges/',views.mesconges , name='mesconges'),
    path('historique/',views.historique , name='historique'),
    path('detail/',views.detail , name='detail'),
    #Les routes de l'admin
    path('listconges/',views.listconges , name='listconges'),
    path('detailconges/',views.detailconges, name='detailconges'),
]