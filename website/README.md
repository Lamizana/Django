
-------------------------------------------------------------------------------
architecture:
- Website:
    - site
    - man:
        - ls:
            -name:
            -synopsis:
            -descrition:
            -auteur:
            -bug:
            -copyright:
            -voir aussi:

        - cd

- manage.py
- web_env


-----------------------------------------------
- Creation du projet:
```bash
$ django-admin startproject website .
```
> ne pas oublier le point a la fin!

- Creation de la base de données:
```bash
$ python3 manage.py migrate
```

- Lancement du serveur:
```bash
$ python3 manage.py runserver
```

-------------------------------------------------------------------------------
### Commencer une application.

```bash
$ python3 manage.py startapp man_fr

```