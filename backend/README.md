Hapi
==========

Lancer le projet
---------------

- Créer l'environnement virtuel python (si c'est pas déjà fait)

    Sous linux : python3 -m venv env
    Sous macOs : virtualenv env

- Activer l'environnement virtuel

    source env/bin/activate

- Installer les dépendances, si nécessaire

    sh dependencies.sh

- Modifier votre fichier de configuration

    cp exemple.env dev.env
    Modifier les variables dev.env pour vous connecter à votre base de données

- Préparer le fichier de log

    touch dev.log

- "Précompiler" le code : 

    python setup.py develop
    
- Lancer le serveur :

    server_start development.ini


## Base de données

- Pour initialiser la base de donnée

    env/bin/initialize_db development.ini

- Pour remplir la base de données de données de tests
    env/bin/fill_db development.ini

Note : J'ai fais un docker-compose pour initialiser une base de données rapidement, mais attention, mettez un autre port que 3306 afin d'éviter d'éventuels conflits avec une instance déjà installée sur votre machine.