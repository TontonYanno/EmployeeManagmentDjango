from django.db import models
from User.models import Utilisateur
# Create your models here.

class Conges(models.Model):
    TYPE_CHOICES = [
        ('conge', 'Congé'),
        ('maladie', 'Maladie'),
        ('autre', 'Autre'),
    ]
    
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('accepte', 'Accepté'),
        ('refuse', 'Refusé'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='conges')
    
    vu=models.BooleanField(default=False)  # Pour savoir si la demande a été vue par l'admin
    manager_reponse = models.TextField(null=True, blank=True)  # Réponse du manager
    date_reponse = models.DateTimeField(null=True, blank=True)  # Date de réponse du manager
    debut = models.DateField()
    fin = models.DateField()
    date_demande = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.type} - {self.get_statut_display()} (Demader Par : {self.user})"
    
    @property
    def duree(self):
        return (self.fin - self.debut).days + 1
