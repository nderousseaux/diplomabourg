from hapi.models import StateModel, UnitModel
from hapi.validation import *

# Définit si il faut ou non changer d'état
def change_state(DBSession, game, forced = False):
    #Durant la phase de configuration
    if game.state.name == "CONFIGURATION":
        #Si le jeu est forcé ou que tout le monde à dit "pret" alors on passe en mode jeu
        if game.is_all_pret() or forced:
            
            for pui in game.map.powers:
                for disp in pui.disposition_unit:
                    unit = UnitModel(
                        type_unit_id=disp.type_unit_id,
                        cur_region_id=disp.region_id,
                        power=pui,
                        game=game,
                        src_region_id=disp.region_id #FIXME: Reste à null ?
                    )

            game.state = DBSession().query(StateModel).filter_by(name="GAME").one()

            for p in game.players:
                p.is_ready = False

    #Durant la phase de jeu
    elif game.state.name == "GAME":
        #Si le jeu est forcé ou que tout le monde à dit "pret" alors on passe un tour et resout les ordres
        if game.is_all_pret() or forced:
            
            #On résout les conflit
            OrderResolutions(DBSession, game.num_tour, game.id, 0)

            game.num_tour+=1

            for p in game.players:
                p.is_ready = False

            #TODO: Définir quand est-ce qu'on finit ?
        
    
    DBSession.flush()
