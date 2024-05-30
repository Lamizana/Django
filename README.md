# Django

--------------------------------------------------------------
### Mettre en place un projet.

- Créer un environnement virtuel:
```bash
$ python3 -m venv ja_env
```

- Activer l'environnement virtuel:
```bash
$ source ja_env/bin/activate
```

--------------------------------------------------------------
### Commandes.

- Démarre une console interactive shell:
```bash
$ python3 manage.py shell
```

- Importe la base de données utilisateurs (User):
```python
>>> from django.contrib.auth.models import User
```
- Parcours et affiche les utilisateurs et leur identifiant:
```python
>>> for user in User.objects.all():
...     print(user.username, user.id)
...
```

--------------------------------------------------------------
### Mettre en place des comptes utilisateurs.

Mettre en place un systeme d'inscription et d'autorisation:
    - Permet de créer un compte et de se déconnecter du site.

[1]. Application utilisateurs.

- Création de l'application:
```bash
$ python3 manage.py startapp utilisateurs
```

- Ajout utilisateur a ***INSTALLED_APP*** dans *settings.py*
- Ajout des urls pour utilisateurs dans ***journal_apprentissage/urls.py***.

[2]. Page de connexion.

- Création d'un fichier urls.py dans le dossier utilisateur.
- Les vues par default sont dans un dossier registration.

- Etapes:
    - Creer un gabarit de connexion.
    - Creer un lien vers la page de connexion.
        - il se situera dans **base.html** pour etre dans toutes les pages.
> Le gabarit d'authentification de django contient une variable user dont la
> valeur ***is_authenticated*** est déclaré.
    - Creer un lien vers la page de déconnexion.   
        - gabarit de reference ***logged_out.html***.
    - Page d'inscription: form **UserCreationForm**.
        - TEMPLATE PREDEFINIS DANS DJANGO (voir register dans views.py)

### Associer les données aux utilisateurs.

la redirection ***@login_required*** indispensable.

### Restreindre l'accés au sujets.

- Demande a django de retrouver dans la base de données uniquement
les objets Topic dont l'attribut owner correspond a l'utilisateur
connecté: Vive les templates et gabarits !
```python
topics = Topic.objects.filter(owner=request.user).order_by('date_added')
```