# Algorithme de résolution des règles

## Structure de données pour un ordre

```
{
order : [
    id_unit : int                   // Unité qui fait l'action
    order-type : {                  // Types d'ordre
        HOLD = 0,
        ATTACK,
        SUPPORT,
        CONVOY
    }
    id_target_region : int          // Région ciblé
    id_convoy_unit : int            // Unité qui se fait déplacer par convoi
    ]
}
```

## Validité d'un ordre

- Pas plus d'une d'unité par régions.
- On ne peut pas convoyer sur une région côtière.
- Si un ordre devait dépendre d'un autre, et que celui ci est impossible. L'ordre est aussi impossible.
- Si deux unités reçoivent l'ordre d'attaquer la région l'une de l'autre aucun ne réussit le déplacement. Sauf si une ou les deux unités sont convoyées.
- Les unités terrestres doivent être sur les régions terrestres ou côtières.
- Les unités maritimes doivent être sur les régions maritimes ou côtières.

### Soutien

- Le soutien doit se faire une région adjacente et accessible sans convoi.
- Il est impossible de soutenir une unité qui soutient.
- Le soutien augmente la force de l'unité
- On peut soutenir tous les types ordres.

_Soutien coupé :_

- Si une unité qui soutient est attaqué, le soutien est coupé.
- Si une unité qui soutient est attaqué par une unité d'une autre région que celle attaquée, le soutien est coupé.
- Si un soutien est coupé l'unité ciblée n'en bénéficie plus.

### Attaque

- On ne peut attaquer une unité de sa propre nationalité
- Si deux attaques de force égales sont dirigées vers la même région, les attaques sont annulées et la garnison n'est pas contrainte au déplacement

### Retraite

- La retraite est un déplacement qui doit se faire sur une région libre, c'est à dire :
  - autre que celle d'où l'attaque provient
  - adjacente et accessible
  - inoccupée
  - sur laquelle des attaques ne sont pas bloquées
  - Si aucune des régions ne correspond à ces critères, l'unité est annihilée.
- L'annihilation entraîne le retrait de l'unité sur la carte
- Si deux unités doivent faire une retraite dans la même région, les deux unités sont annihilées.
- Si une unité est dispersée elle est retirée du jeu, mais la règle au dessus ne s'applique pas.

### Convoi

- Seule une flotte sur une région maritime peut convoyer des unités.
- Un convoi ne peut prendre qu'une seule unité.
- Le convoi est valide, seulement si le convoi n'est pas rompu, et que l'armée réussit une attaque sur la région ciblé.
- Le convoi se fait sur une unité présente sur une région côtière adjacente à l'unité qui convoi.
- Si le convoi est rompu par une attaque, l'unité terrestre n'est pas déplacée.
- Les convois peuvent formés des chaînes.
- Un convoi multiple n'échoue que si tout les convois possibles échouent.
- Si la destination de l'attaque peut être atteinte par voie maritime ou terrestre, on prend en compte les deux, la voie maritime en premier.

### Contrôle des centres

- Après les retraites et dispersions, une puissance peut prendre le contrôle d'un centre à la fin d'une saison d'automne.
- Un centre permet d'entretenir une unité supplémentaire.
- Le nombre d'unités contrôlées doit être ajusté au nombre de centre contrôlé par le joueur.
- Si le nombre d'unités est supérieur au nombre de centre, le joueur doit démobiliser une unité, choisit librement par le joueur.
- Si le nombre d'unités est inférieur au nombre de centre, le joueur doit mobiliser une unité, choisit librement par le joueur.
- Les unités mobilisés doivent être placées sur le centre où elles sont mobilisés.
- La mobilisation s'effectue sur un centre inoccupé possédé par le joueur.

### Désordre civil

- Le désordre civil est déclenché si un joueur est absent ou aucun ordre a été rendu, auquel cas, les unités tiennent leurs positions.
- Le désordre civil s'arrête si le joueur revient et donne des ordres ou que toutes les unités soient annihilées.
- Si une unité doit battre en retraite et que le joueur est en désordre civil, les unités sont dispersées.
- Si une unité doit être démobilisée et que le joueur est en désordre civil, l'unité retirée est la plus éloignée de son centre d'origine, en cas d'égalité, les flottes sont retirées en premier, puis on applique l'ordre alphabétique des régions.
