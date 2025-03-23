from django.urls import path
from Taches import views 


urlpatterns = [
    # Les vues de l'employé
   path('mytasks', views.mytasks, name='mestaches'),
   path('editmytasks/', views.editmytasks, name='editmytasks'),
   path('archivetasks/', views.archivetasks, name='archivetasks'),
   #Les vues de l'admin
   path('addtask/', views.addtask, name='addtasks'),
   path('listtasks/', views.listtasks, name='listtasks'),
   path('edittask/', views.edittask, name='edittask'),
]
