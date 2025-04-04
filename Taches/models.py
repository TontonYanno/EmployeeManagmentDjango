from django.db import models
from django.conf import settings
from User.models import Utilisateur

class Tache(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('terminee', 'Terminée'),
    ]
    ARCHIVE_CHOICES = [
        ('oui', 'Oui'),
        ('non', 'Non'),
    ]

    titre = models.CharField(max_length=255)
    description = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='taches')  
    archive = models.CharField(max_length=10, choices=ARCHIVE_CHOICES, default='non')  # Statut d'archivage
    mention_archive = models.TextField(null=True, blank=True)  # Explication de l'archivage
    date_limite = models.DateField(null=True, blank=True)  # Date limite pour terminer la tâche
    date_creation = models.DateTimeField(auto_now_add=True)  # Date de création automatique

    def __str__(self):
        return f"{self.titre} - {self.get_statut_display()} (Assigné à: {self.user})"
