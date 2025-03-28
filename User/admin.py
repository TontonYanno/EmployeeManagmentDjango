from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('prenoms', 'email', 'role', 'sexe', 'telephone')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informations personnelles', {'fields': ('nom', 'prenoms', 'sexe', 'matricule', 'telephone', 'adresse')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nom', 'prenoms', 'sexe', 'matricule', 'telephone', 'adresse', 'role', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
