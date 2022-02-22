# Notes sur le design de l'api

## 


- Réception d'ordre 
    - Ordre valide/invalide

- Get
    - Avec geojson

- Get carte + nb joueurs
    - Réponse de la config théorique de départ

- get All cartes
    - sans geojson

- Getconfiguration acutelle
    - info partie (si elle a commencée ou pas)
    - Enmplacement de tout les pionts
    - Numéro du tour

- Get liste des jouers et états

- Je valide mon tour

- Ordre de création de partie
    - json entier de la partie

- Modification des réglages de la partie
    - Ne peut être que par celui qui à crée la partie

- Demande le cookie, avec le nom d'utilisateur
    - Envoie le cookie, et l'id user

- WhoIAmI

- Demande de connection à la partie (avec id et mot de passe)
    - Oui / non et pourquoi

- Demande le départ de la partie

- Demande le départ de la partie forcée (admin uniquement)


## Websocket


envoie une url, qui est celle interessante pour le front. le front dois ensuite demander l'url pour avoir la nouvelle info
