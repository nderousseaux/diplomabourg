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

### Pas plus d'une d'unité par régions

```python
if units > 1 :
    return False
```

### On ne peut pas convoyer sur une région côtière

```python
if region_type == COSTAL :
    return False
```
