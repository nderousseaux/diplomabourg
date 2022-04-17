from hapi.models import StateModel
from hapi.utils.validation import resolution_orders

# Définit si il faut ou non changer d'état
def change_state(DBSession, game, forced = False):
    #Durant la phase de configuration
    if game.state.name == "CONFIGURATION":
        #Si le jeu est forcé ou que tout le monde à dit "pret" alors on passe en mode jeu
        if game.is_all_pret() or forced:
            game.place_units()
            game.state = DBSession().query(StateModel).filter_by(name="GAME").one()

            for p in game.players:
                p.is_ready = False

    #Durant la phase de jeu
    elif game.state.name == "GAME":
        #Si le jeu est forcé ou que tout le monde à dit "pret" alors on passe un tour et resout les ordres
        if game.is_all_pret() or forced:
            
            #On résout les conflit
            resolution_orders(DBSession, game)

            game.num_tour+=1

            #TODO: Définir quand est-ce qu'on finit ?
        
    
    DBSession.flush()
