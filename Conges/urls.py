from Conges import views
from django.urls import path
urlpatterns = [  
    #Les routes de l'employé  
    path('mesconges/',views.mesconges , name='mesconges'),
    path('mes_conges/',views.mes_conges , name='mes_conges'),#traitement demander congés
    path('historique/',views.historique , name='historique'),
    path('detail/<int:id>/',views.detail , name='detail'),
    #Les routes de l'admin
    path('listconges/',views.listconges , name='listconges'),
    path('detailconges/<int:id>/',views.detailconges, name='detailconges'),
    path('detail_conges/<int:id>/',views.detail_conges, name='detail_conges'),#traiter la reponse de l'admin
]