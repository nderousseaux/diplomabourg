"""Retourne l'ordre gagnant dans une liste d'ordre
"""
def resolve_conflits(liste_orders):
    if len(liste_orders) > 1:
        counter = []

        for o in liste_orders:
            counter.append(o.number_soutients())
        
        val=max(counter)
        #Deux unités ont obtenu le même nombre de soutient valides 
        if(counter.count(val)==1): 
            i = getIndex(counter,val)
            order=liste_orders[i]
            liste_orders.pop(indice)

            #je valide le déplacement de l'unité gagnante
            order.unit.cur_region=order.dst_region
            #rendre toutes les attaques non effectives
            for o in liste_orders:
                    o.state = False  
            return order
        else:
            return False  
    elif len(liste_orders)==1:
        order = liste_orders[0]
        order.unit.cur_region=order.dst_region
        return order


def resolution_orders(DBSession,game):

    # Validation des ordres
    game.validation_orders()

    DBSession

    #On désactive toutes les attaques mutuelles
    for orders in game.attaques_mutuelles():
        for o in l:
            o.state = False 

    #On brise les support
    for o in [o for o in game.orders_valid() if o.type_order.name == "SUPPORT"]:
        o.coupe_soutien() 

    #On romp les convois
    for o in [o for o in game.orders_valid() if o.type_order.name == "CONVOY"]:
       o.broke_convoi()

    #On invalide les attaques dont les convois sont rompus
    for o in [o for o in game.orders_valid() if o.type_order.name == "SUPPORT" and o.state == False]:
        order = [o2 for o2 in game.orders_valid() if o2.type_order.name == "ATTACK" and o2.unit == o.other_unit]
        if len(order) > 0:
            order[0].is_valid = False

    #On déplace les unités
    game.move_units()
    
    #On résout les conflit
    game.resolve_all_conflits()
    
    #On supprime les unités
    game.remove_units_lost()
