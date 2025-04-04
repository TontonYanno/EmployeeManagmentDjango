from django.urls import path
from Taches import views 


urlpatterns = [
    # Les vues de l'employé
   path('mytasks', views.mytasks, name='mestaches'),
   path('archive', views.archive, name='archive'), #pour tester le fonctionnement de la page
   path('courant', views.courant, name='courant'), #pour tester le fonctionnement de la page
   path('retard', views.retard, name='retard'), #pour tester le fonctionnement de la page

   
   path('editmytasks/<int:id>/', views.editmytasks, name='editmytasks'), #affichage de la page d'édition de la tâche
   path('update_mytask/<int:id>/', views.update_mytask, name='update_mytask'), #le traitement de la modification d'une tache
   
   path('archivetasks/<int:id>/', views.archivetasks, name='archivetasks'), #affichage de la pages d'archivage de la tache
   path('archive_tasks/<int:id>/', views.archive_tasks, name="archive_tasks"),#le traitement de l'archivage 
   
   #Les vues de l'admin
   path('listtasks/', views.listtasks, name='listtasks'),
   
   path('addtask/', views.addtask, name='addtasks'),
   path('add_task/', views.add_task, name='add_task'), #le traitement de l'ajout d'une tache
   
   path('edittask/<int:id>/', views.edittask, name='edittask'), #affichage
   path('update_task/<int:id>/', views.update_task, name='update_task'), #le traitement de la modification d'une tache
   
   path('delete_task/<int:id>/', views.delete_task, name='delete_task'), #le traitement de la suppression d'une tache
   
]
