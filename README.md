Modèle  Utilisateur 
  -nom
  -nom_complet
  -sexe(m/f)
  -matricule
  -email
  -password
  -telephone
  -adresse
  -role( employé / manager)
Voilà un peu les info qu'on doit avoir pour un compte Utilisateur 

/!\ Si tu remarque bien mes vues, c'est le manager seul qui peut creer des comptes.

QUELQUES REGLES DE GESTION

* Le manager creer les comptes des employés 
* Le manager assigne des taches a 1 ou n employés
* Le manager accepte ou refuse les congés de ses  employés

* L'employé peut modefier son password une fois que son compte est créer
* L'employé peut modifier le status des tâches qui lui sont assignés dans son espace
* L'employé peut faire des demandes de congés
* L'employé peut archivé des tâches


/!\ Pour le moment tu va sciencer la fonctionnaliité d'authnetification là d'abord 
JE pense pouvoir gerer le reste


faut lancer l'application pour voir utilise 
pour employee:admin@gmail.com et code bbkml123
pour manager:bookeleblan@gmail.com et code bbkml
et si tu veux voir le formulaire user et essaie de taper url= http://127.0.0.1:8000/admin/ connectez en tant que manager sinon employer na pas acces