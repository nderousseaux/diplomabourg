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
    print(unite.id)
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
def isRegionOccupedByOtherUnit(idRegion,DBSession): #already tested
     region = DBSession.query(RegionModel).filter(RegionModel.id == idRegion).first()
     uniteRegions=region.units_cur_region
     if(len(list(uniteRegions)))!=0:
        return True
     return False 
 
   
def updateOrder(order,DBSession,transaction):
    get_order = DBSession.query(OrderModel).filter(OrderModel.id == order.id).first()
    get_order.is_valid=True
    transaction.commit()
    

def valideAttaque(order,DBSession,transaction): #already tested
    idJoueur=order.unit.player.id
    print("hello")
    if (isYourOwnUnity(idJoueur,order.unit.id)==True and isAttaqueMyself(idJoueur,order.dst_region_id)==False):
        print(order.unit.type_unit_id) 
        if isArmy(order.unit.id,DBSession)==True:
            print("Army")
            if(isLandRegion(order.dst_region_id,DBSession)==True or isCostaleRegion(order.dst_region_id,DBSession)==True):
                if (isTwoRegionsConnex(order.src_region_id,order.dst_region_id,DBSession)):
                     #modifié le champ isvalide de l'ordre
                     order.is_valid = True
                     order.unit.cur_region_id=order.dst_region_id
                     return True  
                    
                elif (ExisteConvoy(order.unit.id,order.src_region_id,order.dst_region_id,DBSession)):
                    #modifié le champ isvalide de l'order
                     order.is_valid = True
                     print("Army attack valid")
                     return True 
        elif isFleet(order.unit.id,DBSession)==True:
            if(isMaritimeRegion(order.dst_region_id ,DBSession)==True or isCostaleRegion(order.dst_region_id ,DBSession)==True):
                 if (isTwoRegionsConnex(order.src_region_id,order.dst_region_id,DBSession)):
                     #modifié le champ isvalide de l'order  
                     order.is_valid = True
                     print("Fleet attack valid")
    return False

def moveUnits(DBSession,nbtour,gameid,transaction):
    #toute les ordres d'attaques valide
    orders= DBSession.query(OrderModel).filter(OrderModel.gameid.like(gameid),OrderModel.nbtour.like(nbtour),OrderModel.type_order_id.like(1),OrderModel.is_valid==True,OrderModel.state!=False)
    print("déplacement des unités")
    for o in orders:
        o.unit.cur_region_id=o.dst_region_id
    transaction.commit()
    print("fin déplacement")
    
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
    if (isYourOwnUnity(idJoueur,order.unit.id)):
        if(isFleet(order.unit.id,DBSession) ):
            if(order.unit_id != order.other_unit_id):
                    if(isArmy(order.other_unit.id,DBSession)):
                        if(isMaritimeRegion(order.src_region_id ,DBSession)):
                            if(isCostaleRegion(order.other_unit.cur_region_id, DBSession)):
                                if(isCostaleRegion(order.dst_region_id, DBSession)) :
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
                         
        elif (isFleet(order.unit.id, DBSession) == True):
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

#veryimportant 
def Validation(DBSession,nbtour,gameid,transaction) :
    orders= DBSession.query(OrderModel).filter(OrderModel.gameid.like(gameid),OrderModel.nbtour.like(nbtour))
    #orders= DBSession.query(OrderModel).filter((OrderModel.gameid == game.id), (OrderModel.nbtour == game.nbtour))

    print("validation ordre")
    for o in orders :
        print("idOrder:",o.id)
        if (o.type_order.name=="ATTACK"):  
            valideAttaque(o, DBSession, transaction) # Attaquer une zone
            
            
        elif (o.type_order.name  == "CONVOY"):
            ValideConvoyArmy(o, DBSession, transaction) # Convoyer une armée
            

        elif (o.type_order.name  == "SUPPORT"):
         valideSoutien(o, DBSession, transaction)

            
    
    transaction.commit()
    print("fin validation")

def testValidationOrders(idGame, DBSession,transaction):
    game = DBSession.query(GameModel).filter(GameModel.id == idGame).first()
    Validation(DBSession,game.nbtour,game.id,transaction)

def tesvalideSoutien(idOrder,DBSession,transaction):
    order = DBSession.query(OrderModel).filter(OrderModel.id == idOrder).first()
    return (valideSoutien(order,DBSession,transaction))

def AttaqueMutuelle(orders, DBSession): #already testeed 
    MutualAttack = []
    redondencyListe=[]
    for o in orders :
        
        
        # La liste des ordres en conflit avec l'ordre source
        found = DBSession.query(OrderModel).filter(OrderModel.id.not_like(o.id),OrderModel.type_order_id .like(1), OrderModel.src_region_id.like(o.dst_region_id), OrderModel.dst_region_id.like(o.src_region_id), OrderModel.nbtour.like(o.nbtour),OrderModel.gameid.like(o.gameid))
        
        if(found.count()!=0):
            if o not in redondencyListe:
                data=[]
                data.append(o)
                redondencyListe.append(o)

                for f in found:
                    data.append(f)
                    redondencyListe.append(f)
                MutualAttack.append(data)  

    return MutualAttack 

#result must be  unit wich are in conflict :
    # [6, 4]
    # [13, 12]
    # [7, 5]

def testAttaqueMutuelle(idGame, DBSession,transaction):
    game = DBSession.query(GameModel).filter(GameModel.id == idGame).first()
    orders= DBSession.query(OrderModel).filter(OrderModel.gameid.like(game.id),OrderModel.nbtour.like(game.nbtour))
    list=AttaqueMutuelle(orders, DBSession)
    return list
    

    
        
    

#state est True par défaut alors on le met à False
#orders est la liste des attaque mutuelle
# La clé etant l'instance source alors on modifiera que celui ci
def AnnuleAttMutuelle(orders, DBSession, transaction):
    for o in orders:
        o.state = False # correspond à ===> order.o qui ne peut etre utilisé
        
#important     
def AnnuleAllAttMutuelle(DBSession, nbtour,gameid ,transaction):
    orders = DBSession.query(OrderModel).filter(OrderModel.type_order_id .like(1), OrderModel.nbtour.like(nbtour),OrderModel.gameid.like(gameid),OrderModel.is_valid==True)
    listMutualAttack=AttaqueMutuelle(orders, DBSession)
    for l in listMutualAttack:
         AnnuleAttMutuelle(l, DBSession, transaction)    
    transaction.commit()
   

# Retourne la liste de tous les ordres qui attaquent une meme zone dans un tour
# order est un ordre de type attaque en fonction du nombre de tour de la partie
def SameAreaAttacked(order, DBSession, transaction):
    found = DBSession.query(OrderModel).filter(OrderModel.id != order.id, OrderModel.type_order_id ==1, OrderModel.dst_region_id == order.dst_region_id, order.nbtour == OrderModel.nbtour)
    return found   
# Retourne une liste d'ordres qui visent une zone de l'ordre passé en paramètre
# order est un ordre de n'importe quel type en fonction du nombre de tour de la partie
def isIamAttacked(order, DBSession): #already tested
    
    found = DBSession.query(OrderModel).filter(OrderModel.id != order.id, OrderModel.type_order_id==1, OrderModel.dst_region_id == order.src_region_id, order.nbtour == OrderModel.nbtour)
    return found

listInputOrder=[27,28]
def testisIamAttacked(idOrder, DBSession):
    order= DBSession.query(OrderModel).filter(OrderModel.id==idOrder).first()
    query=isIamAttacked(order,DBSession)
    l=[o.unit_id for o in query]
    print(l)


# order est un ordre de type soutient en fonction du nombre de tour de la partie
# Pour la recuperer : DBSession.query(OrderModel).filter(OrderModel.type_order.name == "SUPPORT", OrderModel.nbtour == game.nbtour)
def soutientCoupe(order, DBSession, transaction): #already tested
    conflit = isIamAttacked(order, DBSession)
    if(conflit.count()!=0):
        order.state = False
        
#important 
def BreakSupport(DBSession,nbtour,gameid,transaction):
    orders = DBSession.query(OrderModel).filter(OrderModel.type_order_id .like(3), OrderModel.nbtour.like(nbtour),OrderModel.gameid.like(gameid))
    print("break support")
    for o in orders:
        soutientCoupe(o, DBSession, transaction)    
    transaction.commit()
    print("fin break supoort")


listInputIdOrder=[27,28]
def testSoutientCoupe(idOrder, DBSession, transaction):  
    order= DBSession.query(OrderModel).filter(OrderModel.id==idOrder).first()
    soutientCoupe(order, DBSession, transaction)
    
    


def getRegionConnex(idRegionDest):
    region=DBSession.query(RegionModel).filter(RegionModel.id==idRegionDest).first()
    return region.neighbours
    
#prends tous les ordres d'attaques dont states==False

def isRetraitPossible(order, DBSession, transaction):
    # teste si la région source de l'unité qui attaque n'est pas occupé 
    if (isRegionOccupedByOtherUnit(order.src_region_id,DBSession)==False):
        order.unit.cur_region_id=order.src_region_id
        print("retrait in cur_region id")
    else:    
          neighbours=getRegionConnex(order.dst_region_id )
          for n in neighbours:
              if (n.id!=order.src_region_id):
                  print(n.name)
                  if (isRegionOccupedByOtherUnit(n.id,DBSession)==False):
                      order.unit.cur_region_id=n.id
                      print("retrait in other connex region")
                      return True
    order.unit.life=False 
    return False


liste=[26,25,24,23]    
def testIsRetraitPossible(idOrder, DBSession, transaction):
    order= DBSession.query(OrderModel).filter(OrderModel.id==idOrder).first()
    isRetraitPossible(order, DBSession, transaction)

#impprtant     
def removeUnitsLost(DBSession,nbtour,gameid ,transaction):
    print("debut retrait")
    orders= DBSession.query(OrderModel).filter(OrderModel.nbtour.like(nbtour),OrderModel.gameid.like(gameid),OrderModel.state==False)
    for o in orders:
        isRetraitPossible(o, DBSession, transaction)
    transaction.commit()
    print("fin retrait")
#prend tous les ordres de la partie 
def dectetAllConflicts(orders,DBSession): #already teste 
    Conflit = []
    OrdreConflit = []
    # pour tous les ordres
    for o in orders:
        # chercher les ordres de même tour et partie + 
        # found = DBSession.query(OrderModel).filter(OrderModel.id.not_like(o.id),OrderModel.unit.cur_region_id.like(o.unit.cur_region_id))
            if o not in OrdreConflit:
                data = []
                data.append(o)
                OrdreConflit.append(o)
                for i in orders:
                    if(o.id!=i.id and o.unit.cur_region_id==i.unit.cur_region_id):
                        data.append(i)
                        OrdreConflit.append(i)
                Conflit.append(data)
    return Conflit



def testDectetAllConflicts(DBSession): #already tested
    #recupére tous les ordres d'attaque
    orders = DBSession.query(OrderModel).filter(OrderModel.nbtour==2,OrderModel.gameid==1)
    listeConflit=dectetAllConflicts(orders,DBSession)
    for l in listeConflit:
        lc=[o.id for o in l ]
        print(lc)
        
    # retourne le nombre soutient valide qu'à obtenu l'unité qui attaque
def nbValidSupportForOrder(order, DBSession): # Pour Diaby #already tested 
    #fiare une requête c'est plus simple 
    #orders = getAllSupportOrders(orderAttaque.gameid, DBSession)
    orders = DBSession.query(OrderModel).filter(OrderModel.type_order_id.like(3),OrderModel.other_unit_id.like(order.unit_id), OrderModel.nbtour.like(order.nbtour),OrderModel.gameid.like(order.gameid),OrderModel.other_unit_id.like(order.unit_id),OrderModel.state!=False)
    return orders.count()

listInputIdOrder=[22,23,23,25,26]
def testnbValidSupportForOrder(idOrder, DBSession):
     order= DBSession.query(OrderModel).filter(OrderModel.id==idOrder).first()
     print("Attaque region:",order.src_region.name)
     return nbValidSupportForOrder(order, DBSession)
     

# Verifier qu'une zone est attaque : Utilisez pour le soutien spécifiquement ici
def isAttacked(order , DBSession):
    AllAttacksOrders = getAllAttackOrders(order.gameid, DBSession)
    for o in AllAttacksOrders:
        if (o.dst_region_id == order.src_region_id) and (o.other_unit_id == order.unit_id) :
            True

    return False

def countX(lst, x): 
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count
#valeur doit être forcément présent  
def  getIndex(L,x):
    idx = 0
    for ele in L: 
        if (ele != x): 
            idx = idx + 1
        else :
                return idx
def ResolveConflict(listOrder, DBSession, transaction): # Pour Diaby
    if(len(listOrder)>1):
        counterArray = []
        for o in listOrder:
            # Stocke le nombre de soutien de chaque ordre de listOrdre
            val=nbValidSupportForOrder(o, DBSession)
            counterArray.append(val)
        maxVal=max(counterArray) 
        #counterArray.count(maxVal)
        if(countX(counterArray, maxVal)==1) : # deux unités ont obtenu le même nombre de soutient valides 
            indice =getIndex(counterArray,maxVal)
            orderGangant=listOrder[indice]
            listOrder.pop(indice)
            #je valide le déplacement de l'unité gangant 
            orderGangant.unit.cur_region_id=orderGangant.dst_region_id
            print(orderGangant.src_region.name)
            return orderGangant
        #rendre tous  les attaques no effettif 
        for  o in listOrder:
                o.state = False  
        else :
            print("perssonne n'a gangé")
            return False  
    elif(len(listOrder)==1) :
        orderGangant=listOrder[0]
        orderGangant.unit.cur_region_id=orderGangant.dst_region_id
        return  orderGangant


   
   
    
def testResolveConflict(listOrderId, DBSession, transaction):
    listOrder=[]
    for o in listOrderId:
         order= DBSession.query(OrderModel).filter(OrderModel.id==o).first()
         listOrder.append(order)
    ResolveConflict(listOrder, DBSession, transaction)     

#important 
def ResolveAllConflicts(DBSession,nbtour,gameid,transaction):
    print("debut resolution conflit ")
    OrderPatie=DBSession.query(OrderModel).filter(OrderModel.nbtour.like(nbtour),OrderModel.gameid.like(gameid))
    listOfAllConflicts=dectetAllConflicts(OrderPatie,DBSession)
    for l in listOfAllConflicts:
        ResolveConflict(l, DBSession, transaction)
    transaction.commit()
    print("fin resolution conflit ")
    
# Prend un ordre de convoi et teste si les conditions sont réunies pour qu'il soit rompu alors c'est rompu 
def ConvoyBroken(OrderConvoy, DBSession, transaction): # Pour Diaby #already tested 
    conflit = isIamAttacked(OrderConvoy, DBSession)
    if(conflit.count()!=0): # ça veut dire y'a un conflit 
        listOrders=[c for c in conflit]
        listOrders.append(OrderConvoy)
        orderGangnant=ResolveConflict(listOrders, DBSession, transaction)
        if(orderGangnant==False):
                OrderConvoy.state=False
                
                
def testConvoyBroke(idOrder, DBSession, transaction) :
        order= DBSession.query(OrderModel).filter(OrderModel.id==idOrder).first()
        ConvoyBroken(order, DBSession, transaction)    


#important 
def BreakSomeConvoy(DBSession,nbtour,gameid,transaction):
    #recupére tous les ordres de convois valides
    print(" debut break convoy")
    orderConvoy= DBSession.query(OrderModel).filter(OrderModel.type_order_id.like(4),OrderModel.nbtour.like(nbtour),OrderModel.gameid.like(gameid),OrderModel.is_valid==True)
    for o in orderConvoy:
       ConvoyBroken(o,DBSession, transaction)
    transaction.commit()
    print(" fin break convoy")

def removeAttaqueByConvoy(DBSession,nbtour,gameid,transaction):
    #je recupére tous les ordres de convois brisés
    print("relocalisation")
    orderConvoy= DBSession.query(OrderModel).filter(OrderModel.type_order_id.like(4),OrderModel.nbtour.like(nbtour),OrderModel.gameid.like(gameid),OrderModel.is_valid==True,OrderModel.state==False)
    for o in orderConvoy:
        orderAttack=DBSession.query(OrderModel).filter(OrderModel.type_order_id.like(1),OrderModel.nbtour.like(nbtour),OrderModel.gameid.like(gameid),OrderModel.is_valid==True,OrderModel.unit_id==o.other_unit_id).first()
        orderAttack.is_valide=False
    transaction.commit()
    print("relocalisation")
    
def OrderResolutions(DBSession,nbtour,gameid,transaction):
    #je valide d'abord les ordres
    Validation(DBSession,nbtour,gameid,transaction)
    
    #j'annule les attaques mutuelles 
    AnnuleAllAttMutuelle(DBSession, nbtour,gameid ,transaction)
    
    #je brise les soutients 
    BreakSupport(DBSession,nbtour,gameid,transaction)
    
    #je romps les covois 
    BreakSomeConvoy(DBSession,nbtour,gameid,transaction)
    
    #j'invalide les attaques dont les convois sont rompus 
    removeAttaqueByConvoy(DBSession,nbtour,gameid,transaction)
    
    #je déplace les unités 
    moveUnits(DBSession,nbtour,gameid,transaction)
    
    
    #je résous les conflits
    ResolveAllConflicts(DBSession,nbtour,gameid,transaction)
    
    #je retire les unités 
    removeUnitsLost(DBSession,nbtour,gameid ,transaction)