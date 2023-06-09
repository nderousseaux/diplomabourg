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
                        type_unit=disp.type_unit,
                        cur_region=disp.region,
                        power=pui,
                        game=game,
                        src_region=disp.region
                    )

                #On place les centres
                create_centers(DBSession, game)

            game.state = DBSession().query(StateModel).filter_by(name="GAME").one()

            for p in game.players:
                p.is_ready = False

    #Durant la phase de jeu
    elif game.state.name == "GAME":
        #Si le jeu est forcé ou que tout le monde à dit "pret" alors on passe un tour et resout les ordres
        if game.is_all_pret() or forced:
            
            #On résout les conflit
            OrderResolutions(DBSession, game)

            end_state = DBSession().query(StateModel).filter_by(name="END").one()

            game.num_tour+=1

            if game.num_tour >= 15:
                game.state = end_state

            for p in game.players:
                p.is_ready = False
                if p.nb_center() >= 18:
                    game.state = end_state

    DBSession.flush()
