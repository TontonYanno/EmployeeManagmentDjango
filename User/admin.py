from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur

class CustomUserAdmin(UserAdmin):
    list_display = ( "username", "email", "nom_complet", "sexe", "matricule", "date_naissance", "telephone", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Informations personnelles", {"fields": ( "nom_complet","email", "sexe", "matricule","date_naissance","telephone", "adresse", "role")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    search_fields = ("email", "nom_complet", "matricule")
    ordering = ("email",)

admin.site.register(Utilisateur, CustomUserAdmin)
