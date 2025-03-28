from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]

    ROLE_CHOICES = [
        ('employé', 'Employé'),
        ('manager', 'Manager'),
    ]

    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=255)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    matricule = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, unique=True)
    adresse = models.TextField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employé')

    USERNAME_FIELD = 'email'  # L'authentification se fera par email
    REQUIRED_FIELDS = ['nom', 'prenoms', 'sexe', 'matricule', 'telephone', 'adresse', 'role']

    def __str__(self):
        return f"{self.prenoms} ({self.role})"

    @property
    def is_employee(self):
        return self.role == 'employé'  # Compare avec 'employé'
