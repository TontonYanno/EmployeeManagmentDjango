from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    SEXE_CHOICES = (('M', 'Masculin'), ('F', 'Féminin'))
    ROLE_CHOICES = (('employe', 'Employé'), ('manager', 'Manager'))

    # username = models.CharField(max_length=20)
    nom_complet = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    matricule = models.CharField(max_length=20, unique=True)
    telephone = models.CharField(max_length=20, unique=True)
    adresse = models.TextField()
    date_naissance=models.DateField(null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="employe")
    photo = models.ImageField(upload_to='photos_profiles/', null=True, blank=True)

    # Supprimer le champ `username` qui est inclus par défaut dans `AbstractUser`

    # Définir `email` comme identifiant principal
    # USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [  "nom_complet","email", "sexe","matricule", "adresse", "telephone", "role"]

    def __str__(self):
        return f"{self.nom_complet} ({self.email})"
