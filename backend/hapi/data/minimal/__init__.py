"""
Données minimales nécessaires au bon fonctionnement de l'application
"""
from hapi.models import *

from .color_data import colors
from .disposition_unite_data import disposition_unite
from .map_data import maps
from .power_data import powers
from .region_data import regions
from .region_type_region import regions_type_region
from .state_data import states
from .type_order_data import type_orders
from .type_region_data import type_regions
from .type_unite_data import type_unites
from .voisinage_data import voisinages

""""
insérrer les données minimales dans la base
"""
def insert_minimal_data(session):
    for m in maps:
        session.add(MapModel(**m))
    for c in colors:
        session.add(ColorModel(**c))
    for p in powers:
        session.add(PowerModel(**p))
    for tr in type_regions:
        session.add(TypeRegionModel(**tr))
    for tu in type_unites:
        session.add(TypeUnitModel(**tu))
    for r in regions:
        session.add(RegionModel(**r))
    for du in disposition_unite:
        session.add(DispositionUnitModel(**du))
    for v in voisinages:
        region = session.query(RegionModel).get(v["src_region_id"]+1)
        for dest in v["dst_region_id"]: 
            dest+=1 #FIXME : Pourquoi ?
            region_autre = session.query(RegionModel).get(dest)
            region.beNeigbours(region_autre)
    for rtr in regions_type_region:    
        region = session.query(RegionModel).get(rtr["region_id"]+1)
        for type_id in rtr["type_region_id"]:
            type_id+=1
            type_region=session.query(TypeRegionModel).get(type_id)
            region.types.append(type_region)
    for s in states:
        session.add(StateModel(**s))
    for to in type_orders:
        session.add(TypeOrderModel(**to))

    session.commit()