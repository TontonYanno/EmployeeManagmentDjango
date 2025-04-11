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

Modèle  Tache
  titre
  description
  statut(en_attente|en_cours| terminée)
  user (clé étrangère sur Utilisateur)
  archive(oui|non)
  mention_archive
  date_limite
  date_creation(now date)

Modèle Conges 
  type
  description
  statut(en_attente|accepte|refuse)
  user (clé étranger sur Utilisateur )
  vu (True|False)
  manager_reponse
  date_reponse
  debut
  fin
  date_demande


