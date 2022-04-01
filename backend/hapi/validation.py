

from .db_utils import *
from hapi.models import *





def testevalidation():
    data= DBSession.query(MapModel).filter(MapModel.name=='Strasbourg')
    for m in data:
        print(m.name)
        
        

def typeRegion(regionId,DBSession,type_region): #already tested
    region=DBSession.query(RegionModel).filter(RegionModel.id==regionId)
    for r in region:
        for t in r.types:
            if (t.name==type_region):
                return True
    return False

def typeUnit(unitId,DBSession,type_unit):#already tested
    #recupérer l'unité 
    unite=DBSession.query(UnitModel).filter(UnitModel.id==unitId);
    for u in unite:
        if (u.type_unit.name==type_unit):
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
    region=DBSession.query(RegionModel).filter(RegionModel.id==idSrc) #
    for r in region:
        for n in r.neighbours:
            if(n.id==idTarget):
                return True
    return False 
        
#si le convoie existe 
def ExisteConvoy(idSrc,idTarget,DBSession):
    return None
#si je m'attaque 
def isAttaqueMyself(idJoueur,idRegionDest):
    return None 

def isYourOwnUnity(idJoueur,idUnite):
    return None

def isUnitePresentInRegion(idUnite,idRegion):
    return None 

def valideAttaque(order,Dbasession):
    #recupére l'id joueur 
    idJoueur=True
    if isYourOwnUnity(idJoueur,ordre.idUnite)==False:    
        if isArmy(order.UnitId,DBSession)==True:
            if(isLandRegion(order.idDest,DBSession)==True or isCostaleRegion(order.idDest,DBSession)==True):
                if (isTwoRegionsConnex(order.idSrc,order.idtarget,DBSession)):
                     #modifié le champ isvalide de l'order 
                     return True  
                    
                elif (ExisteConvoy(order.idSrc,order.idtarget,DBSession)):
                    #modifié le champ isvalide de l'order 
                     return True 
        elif isFleet(order.id,DBSession)==True:
            if(isMaritimeRegion(order.idDest,DBSession)==True or isCostaleRegion(order.idDest,DBSession)==True):
                 if (isTwoRegionsConnex(order.idSrc,order.idtarget,DBSession)):
                     #modifié le champ isvalide de l'order 
                     return True 
    return False 