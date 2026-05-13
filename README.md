# RPG2D_Imad_El_Khattabi

Un jeu style RPG en 2D de type action-exploration, dans lequel nous incarnons un plongeur légendaire en quête de la légendaire cité perdue au fin fond des abysses AQUAELIS, afin de mettre la min sur le trésor du Kraken oublié.


## Installation:

### Pré-requis:
    Python 3.10 +
    MySQL 8.0

### Dépendances:
    Pygame : pip install pygame
    MySQL : pip install mysql-connector-python
    Hashage du mot de passe : pip install bcrypt
    Liaison entre le .env et le fichier db.py : pip install python-dotenv

## Utilisation:

1. Executer le fichier MySQL qui se trouve dans documentation/DB/RPG2D.sql dans un client graphique pour base de données ex. HeidiSQL


2. Aller dans le fichier backend/config/.env.exemple et choisissez une de ces deux options: 
   1. copier les données, collez les dans un fichier .env créé au préalable puis insérer vos identifiants pour vous connecter à la base de données

   2. ou alors insérer vos identifiants directement dans le fichier et renommer le fichier en .env
   

3. Lancer le fichier "main.py"

### Contrôles:
    Déplacer à gauche : ←
    Déplacer à droite : →
    Déplacer en haut : ↑
    Déplacer en bas : ↓
    L'inventaire : I
    Prendre un objet : E
    Utiliser un objet Item : E
    Attaquer : X
    Mettre en Pause : Esc