
from .db_utils import *
from hapi.models import *
import transaction

from sqlalchemy import or_, and_






def typeRegion(regionId,DBSession,type_region): #already tested
    region=DBSession.query(RegionModel).filter(RegionModel.id==regionId).first()
    for t in region.types:
        if (t.name==type_region):
                return True
    return False

def typeUnit(unitId,DBSession,type_unit):#already tested
    #recupérer l'unité 
    unite=DBSession.query(UnitModel).filter(UnitModel.id==unitId).first()
    if (unite.type_unit.name==type_unit):
        return True
    return False    

 #si la région est terestre
def isLandRegion(regionId,DBSession,type_region="LAND"):#already tested
    return typeRegion(regionId,DBSession,type_region)
    

#si la région est côtière
def isCostaleRegion(regionId,DBSession,type_region="COAST"):#already tested
    return typeRegion(regionId,DBSession,type_region)
    
    
# si la région est maritime 
def isMaritimeRegion(regionId,DBSession,type_region="SEA"):#already tested
    return typeRegion(regionId,DBSession,type_region)


    
#si l'unité est une armée 
def isArmy(unitId,DBSession,type_unit="ARMY"):#already tested
     return typeUnit(unitId,DBSession,type_unit)
    
   
     
#si l'unité est une flote
def isFleet(unitId,DBSession,type_unit="FLEET"):#already tested
    return typeUnit(unitId,DBSession,type_unit)


# si region est connexe 
def isTwoRegionsConnex(idSrc,idTarget,DBSession):#already tested
        region=DBSession.query(RegionModel).filter(RegionModel.id==idSrc).first()
        for r  in region.neighbours:
            if(r.id==idTarget):
                print("connex_region")
                return True
        return False

def existechemin(src,listRegion,dest,DBSession):
    i=0
    val=True
    while(i<len(listRegion) ):
        if(isTwoRegionsConnex(src,listRegion[i],DBSession)):
            src=listRegion[i]
            del listRegion[i]
            i=0
        else :
            i=i+1
    if isTwoRegionsConnex(src,dest,DBSession):
        print("Exist convoy")
        return True
    return False


        
#si le convoie existe 
def ExisteConvoy(idUniteConvoye,idRegionSource,idRegionDest,DBSession): # alreedy tested
    ordreConvoy=DBSession.query(OrderModel).filter(OrderModel.other_unit_id==idUniteConvoye)
    listIdRegion=[]
    for o in ordreConvoy:
        listIdRegion.append(o.src_region_id)
    return existechemin(idRegionSource,listIdRegion,idRegionDest,DBSession)

    return None
#si je m'attaque 
def isAttaqueMyself(idJoueur,idRegionDest): #already tested
    region = DBSession.query(RegionModel).filter(RegionModel.id == idRegionDest).first()
    for u in region.units_cur_region:
        if(u.player.id==idJoueur):
            print("isAttaqueMyself")
            return True
    return False


def isYourOwnUnity(idJoueur,idUnite): #already tested
    unite = DBSession.query(UnitModel).filter(UnitModel.id == idUnite).first()
    unite
    if(unite.player.id==idJoueur):
        print("isYourOwnUnity:")
        return True

    return False

# si l'unité est présente sur une région
def isUnitePresentInRegion(idUnite,idRegion):
    #récupère l'unité
    unite = DBSession.query(UnitModel).filter(UnitModel.id == idUnite).first()
    if(unite.region.id == idRegion):
        print("isUnitePresentInRegion:")
        print("c'est ok)")
        return True

    return False 

def valideAttaque(order,DBSession,transaction): #already tested
    idJoueur=order.unit.player.id
    if (isYourOwnUnity(idJoueur,order.unit.id)==True and isAttaqueMyself(idJoueur,order.dst_region_id)==False):
        if isArmy(order.unit.id,DBSession)==True:
            if(isLandRegion(order.dst_region_id,DBSession)==True or isCostaleRegion(order.dst_region_id,DBSession)==True):
                if (isTwoRegionsConnex(order.src_region_id,order.dst_region_id,DBSession)):
                     #modifié le champ isvalide de l'ordre
                     order.is_valid=True
                     DBSession.commit()
                     return True  
                    
                elif (ExisteConvoy(order.unit.id,order.src_region_id,order.dst_region_id,DBSession)):
                    #modifié le champ isvalide de l'order
                     order.is_valid = True
                     transaction.commit()
                     return True 
        elif isFleet(order.id,DBSession)==True:
            if(isMaritimeRegion(order.idDest,DBSession)==True or isCostaleRegion(order.idDest,DBSession)==True):
                 if (isTwoRegionsConnex(order.idSrc,order.idtarget,DBSession)):
                     #modifié le champ isvalide de l'order 
                     return True 
    return False
def tesvalideAttaque(idOrder,DBSession,transaction):
    order = DBSession.query(OrderModel).filter(OrderModel.id == idOrder).first()
    return (valideAttaque(order,DBSession,transaction))


def checkConvoyArmy(playerID, orderid, DBSession):
    
    ourConvoy = DBSession.query(OrderModel).filter(OrderModel.id == orderid).first()
    ourCurrUnit = DBSession.query(UnitModel).filter(UnitModel.id == ourConvoy.unit_id).first()
    state = False

    if (isYourOwnUnity(playerID, ourCurrUnit.player_power_player_id) and ourConvoy.unit_id != ourConvoy.other_unit_id) 
    and (ourConvoy.src_region_id != ourConvoy.dst_region_id) and isMaritimeRegion(ourCurrUnit.cur_region_id, DBSession) 
    and isFleet(ourConvoy.unit_id, DBSession) and isTwoRegionsConnex(ourConvoy.src_region_id, ourCurrUnit.cur_region_id, DBSession) 
    and isTwoRegionsConnex(ourConvoy.dst_region_id, ourCurrUnit.cur_region_id, DBSession) 
    and isCostaleRegion(ourConvoy.src_region_id, DBSession) and isCostaleRegion(ourConvoy.dst_region_id, DBSession) :
        convoy.is_valid = True
        state = convoy.is_valid
        DBSession.commit()

    return state


# Regroupe tous les ordres d'une partie en fonction du tour courant et appel une fonction en fonction du type d'ordre 
# Attaque, Soutien, Convoi, Tenir
# La fonction appelée veriife si l'ordre est valide ou pas et change le is_valid de cet ordre au besoin 
def Validation(gameID, DBSession) :
    # nbtour sera mise dans la table order
    ourOrders = DBSession.query(OrderModel).filter(and_(OrderModel.unit.player.game_id == gameID, OrderModel.unit.player.game.nbtour == OrderModel.nbtour ))

    for order in ourOrders :
        if order.type_order.name == "ATTACK" : 
            valideAttaque(order, DBSession, transaction) # Attaquer une zone
            
        else if order.type_order.name == "CONVOY":
            checkConvoyArmy(order.unit.player.id, order.id, DBSession) # Convoyer une armée

        else if order.type_order.name == "HOLD":
            # Tenir sa position

        else if order.type_order.name == "SUPPORT":
            # Soutenir

        else : 
            # ordre non reconnu : HOLD par defaut

    # Soit on modifie le nombre de tour ici dans la table game ou on le fait ailleurs
    #game = DBSession.query(GameModel).filter(GameModel.id == gameID).first()
    #game.nbtour += 1
    #DBSession.commit()

    return True


    
