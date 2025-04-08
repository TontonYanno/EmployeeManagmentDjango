from django.contrib import admin
from .models import Conges
# Register your models here.

@admin.register(Conges)
class CongesAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'statut', 'user', 'vu', 'manager_reponse', 'date_reponse', 'debut', 'fin', 'date_demande')
    search_fields = ('type', 'user__username')
    list_filter = ('statut', 'type')
    ordering = ('-date_demande',)  # Tri par date de demande décroissante