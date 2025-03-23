from django.urls import path
from Taches import views 


urlpatterns = [
    # Les vues de l'employé
   path('', views.mytasks, name='mestaches'),
   path('editmytasks/', views.editmytasks, name='editmytasks'),
   path('archivetasks/', views.archivetasks, name='archivetasks'),
]
