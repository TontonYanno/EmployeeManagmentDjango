from django.contrib import admin
from .models import Tache

# Register your models here.

@admin.register(Tache)
class TacheAdmin(admin.ModelAdmin):
    list_display = ('titre','description', 'statut', 'date_limite', 'user', 'archive', 'date_creation')
    search_fields = ('titre', 'user')
    list_filter = ('statut', 'archive')

# Ou alternative plus simple
# admin.site.register(Tache)
