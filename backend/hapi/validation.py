
from this import d
from .db_utils import *
from hapi.models import *
import transaction

from sqlalchemy import or_, and_
#from sqlalchemy.sql import or_, and_






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

def updateOrder(order,DBSession,transaction):
    get_order = DBSession.query(OrderModel).filter(OrderModel.id == order.id).first()
    get_order.is_valid=True
    transaction.commit()
    

def valideAttaque(order,DBSession,transaction): #already tested
    idJoueur=order.unit.player.id
    if (isYourOwnUnity(idJoueur,order.unit.id)==True and isAttaqueMyself(idJoueur,order.dst_region_id)==False):
        if isArmy(order.unit.id,DBSession)==True:
            if(isLandRegion(order.dst_region_id,DBSession)==True or isCostaleRegion(order.dst_region_id,DBSession)==True):
                if (isTwoRegionsConnex(order.src_region_id,order.dst_region_id,DBSession)):
                     #modifié le champ isvalide de l'ordre
                     order.is_valid = True
                     return True  
                    
                elif (ExisteConvoy(order.unit.id,order.src_region_id,order.dst_region_id,DBSession)):
                    #modifié le champ isvalide de l'order
                     order.is_valid = True
                     print("Army attack valid")
                     return True 
        elif isFleet(order.id,DBSession)==True:
            if(isMaritimeRegion(order.dst_region_id ,DBSession)==True or isCostaleRegion(order.dst_region_id ,DBSession)==True):
                 if (isTwoRegionsConnex(order.src_region_id,order.dst_region_id,DBSession)):
                     #modifié le champ isvalide de l'order  
                     order.is_valid = True
                    
                     print("Fleet attack valid")
    return False

orderFloat=[10,11,12]
def tesvalideAttaque(idOrder,DBSession,transaction):
    order = DBSession.query(OrderModel).filter(OrderModel.id == idOrder).first()
    return (valideAttaque(order,DBSession,transaction))


#0- l'unité qui convoie t'appartient et est une flotte
#1-l'unité qui est convoyé est une arme
#2- tu ne peux pas te convoyer toi même
#3 - region courant de l'unité qui connvoie doit être maritime 
#4- region destination  de l'unité convoyé est côtiére 
#5  -région source de l'unité convoyé est  cotiére

def ValideConvoyArmy(order, DBSession,transaction): #already tested
    
    idJoueur=order.unit.player.id
    if (isYourOwnUnity(idJoueur,order.unit.id) and isFleet(order.unit.id,DBSession) and (order.unit_id != order.other_unit_id) and isArmy(order.other_unit.id,DBSession)and isMaritimeRegion(order.src_region_id ,DBSession) and isCostaleRegion(order.other_unit.cur_region_id, DBSession) and isCostaleRegion(order.dst_region_id, DBSession)) :
        order.is_valid = True
        print("convoy valide")
    return True
        
orderConvoie=[5,6,7,8,9]       
def testValideConvoy(idOrder,DBSession,transaction):
    order = DBSession.query(OrderModel).filter(OrderModel.id == idOrder).first()
    return (ValideConvoyArmy(order,DBSession,transaction))


def valideSoutien(order,DBSession,transaction):  # already tested 
    idJoueur = order.unit.player.id
    idUnit = order.unit.id
    idOtherUnit = order.other_unit.id
    idRegionSrc = order.src_region_id
    idRegionDst = order.dst_region_id
    #si c'est ton propre unité 
    if (isYourOwnUnity(idJoueur,order.unit.id)==True):
        #si l'unité  qui soutient est une armée 
        if (isArmy(order.unit.id, DBSession) == True):
             # teste si la région destination est cotiére ou maritime 
            if(isLandRegion(idRegionDst,DBSession)==True or isCostaleRegion(idRegionDst,DBSession)==True):
                if (isTwoRegionsConnex(idRegionSrc,idRegionDst,DBSession)):
                        order.is_valid = True
                        print("valideSoutien")
                        return True
                         
        elif (isFleet(order.id, DBSession) == True):
            if(isMaritimeRegion(idRegionDst,DBSession)==True or isCostaleRegion(idRegionDst,DBSession)==True):
                # if (isUnitePresentInRegion(idUnit, idRegionSrc) == True and isUnitePresentInRegion(idOtherUnit, idRegionDst)==True):
                    if (isTwoRegionsConnex(idRegionSrc,idRegionDst,DBSession)):
                        order.is_valid = True
                        print("valideSoutien")
                        return True
    return False
order=[14,15,16]
def testeValideSoutien(idOrder, DBSession,transaction):
    order = DBSession.query(OrderModel).filter(OrderModel.id == idOrder).first()
    return (valideSoutien(order,DBSession,transaction))


# Regroupe tous les ordres d'une partie en fonction du tour courant et appel une fonction en fonction du type d'ordre 
# Attaque, Soutien, Convoi, Tenir
# La fonction appelée veriife si l'ordre est valide ou pas et change le is_valid de cet ordre au besoin 
def Validation(game, DBSession,transaction) :
    orders= DBSession.query(OrderModel).filter(OrderModel.gameid.like(game.id),OrderModel.nbtour.like(game.nbtour))
    #orders= DBSession.query(OrderModel).filter((OrderModel.gameid == game.id), (OrderModel.nbtour == game.nbtour))

    # nbtour sera mise dans la table order
    for o in orders :
        if (o.type_order.name=="ATTACK"):  
            valideAttaque(o, DBSession, transaction) # Attaquer une zone
            
            
        elif (o.type_order.name  == "CONVOY"):
            ValideConvoyArmy(o, DBSession, transaction) # Convoyer une armée
            

        elif (o.type_order.name  == "SUPPORT"):
         valideSoutien(o, DBSession, transaction)

            
    print("Validation ok")
    transaction.commit()

def testValidationOrders(idGame, DBSession,transaction):
    game = DBSession.query(GameModel).filter(GameModel.id == idGame).first()
    Validation(game,DBSession,transaction)

def tesvalideSoutien(idOrder,DBSession,transaction):
    order = DBSession.query(OrderModel).filter(OrderModel.id == idOrder).first()
    return (valideSoutien(order,DBSession,transaction))

def valideRetraite(order, DBSession, transaction):
    idJoueur = order.unit.player.id
    idUnit = order.unit.id
    idRegionSrc = order.src_region_id
    idRegionDst = order.dst_region_id

    if (isYourOwnUnity(idJoueur,idUnit )==True):
        if (valideAttaque(order,DBSession,transaction) == False):
            if (isTwoRegionsConnex(idRegionSrc,idRegionDst,DBSession) == True):
                idRegionSrc = idRegionDst
                order.is_valid = True
                transaction.commit()
                return True

    return False

def tesvalideRetraite(idOrder,DBSession,transaction):
    order = DBSession.query(OrderModel).filter(OrderModel.id == idOrder).first()
    return (valideRetraite(order,DBSession,transaction))

def detecterConflit(order,DBSession):
    Conflit = []
    OrdreConflit = []

    # pour tous les ordres
    for o in order:

        # chercher les ordres de même tour et partie + 
        found = DBSession.query(OrderModel).filter(OrderModel.nbtour.like(o.nbtour),OrderModel.gameid.like(o.gameid),
                                                    OrderModel.dst_region_id.like(o.dst_region_id))
        
        if (found.count() != 0):
            if o not in OrdreConflit:
                data = []
                data.append(o)
                OrdreConflit.append(o)

                for f in found:
                    data.append(f)
                    OrdreConflit.append(f)
                Conflit.append(data)
    
    return Conflit
