from django.urls import path
from Taches import views 


urlpatterns = [
    # Les vues de l'employé
   path('mytasks', views.mytasks, name='mestaches'),
   path('editmytasks/', views.editmytasks, name='editmytasks'),
   path('archivetasks/', views.archivetasks, name='archivetasks'),
   
   #Les vues de l'admin
   path('addtask/', views.addtask, name='addtasks'),
   path('add_task/', views.add_task, name='add_task'), #le traitement de l'ajout d'une tache
   
   path('edittask/<int:id>/', views.edittask, name='edittask'), #affichage
   path('update_task/<int:id>/', views.update_task, name='update_task'), #le traitement de la modification d'une tache
   path('delete_task/<int:id>/', views.delete_task, name='delete_task'), #le traitement de la suppression d'une tache
   
   path('listtasks/', views.listtasks, name='listtasks'),
]
