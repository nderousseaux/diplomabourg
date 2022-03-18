



from sqlalchemy import create_engine


colors=[
    {
        "rgb":"black"
        
    },
    {
        "rgb" :"yellow"
        
    },
    {
        "rgb" :"blue"
    },
    
    {
        "rgb" :"pink"
    },
    
    {
        "rgb" :"red"
        
    },
    {
        "rgb" :"white"
        
    },
    {
        "rgb" :"green"
        
    },
]
maps=[
    {
        "name":"Europe"
    },
    {
        "name":"Strasbourg"
    }
]



powers=[
    {
        "name" : "Germany",
        "color_id":1,
        "map_id" : 1
    },
    {
        "name": "Austria-Hungary", 
        "color_id":2,
        "map_id" : 1
    },
    
    {
        "name": "France",
        "color_id":3,
        "map_id" : 1
    },
    
    {
        "name": "Great Britain",  
        "color_id":4,
        "map_id" : 1
    },
    
    {
        "name": "Italy",
        "color_id":5,
        "map_id" : 1
    },
    
    {
        "name": "Russia",
        "color_id":6,
        "map_id" : 1
    },
    
    {
        "name": "Turkey",
        "color_id":7,
        "map_id" : 1
    },
]

typeRegion=[
    {
        "name":"Land"
    },
    {
        "name":"Sea"
    },
    {
        "name":"Coast"
    },
]

typeUnite=[
    {
        "name":"Army"
    },
    {
        "name":"Fleet"
    },
    
    {
        "name": "Center"
    }
   
]

regions=[
    {
        "name": "Norwegian Sea"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name":"North Sea"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Switzerland"
        ,
        "map_id" :1
        ,
        "hasCenter":False
        
    },
    {
        "name":"Adriatic Sea"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Aegean Sea"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Albania"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Ankara"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Apulia"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Armenia"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    #10
    {
        "name": "Belgium"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Berlin"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Bohemia"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Brest"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
     {
        "name": "Budapest"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name":"Bulgaria"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name":"Burgundy"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Clyde"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name":"Constantinople"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    
    {
        "name": "Denmark"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    #10
    {
        "name": "Eastern Mediterranean"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Edinburgh"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "English Channel"
        
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Finland"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Galicia"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Gascony"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Greece"
        
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Gulf of Lyon"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Gulf of Bothnia"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Helgoland Bight"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Holland"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Ionian Sea"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Gulf of Lyon"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Irish Sea"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name":"Kiel"
        ,
        "map_id" :1
        ,
        "hasCenter" :False
        
    },
    {
        "name": "Liverpool"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Livonia"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "London"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Marseilles"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Mid-Atlantic Ocean"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Moscow"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Munich"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Naples"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "North Atlantic Ocean"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "North Africa"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Norway"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Paris"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Picardy"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Piedmont"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Portugal"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Prussia"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    }
    ,
    {
        "name": "Rome"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Ruhr"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Rumania"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Serbia"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Sevastopol"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Silesia"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Skagerrak"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Smyrna"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Spain"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "St Petersburg"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Sweden"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Syria"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Trieste"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    
    {
        "name": "Tunis"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Tuscany"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Tyrolia"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Tyrrhenian Sea"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Ukraine"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Venice"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Vienna"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Wales"
        
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Warsaw"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    },
    {
        "name": "Western Mediterranean"
        ,
        "map_id" :1
        
        ,
        "hasCenter" :False

    },
    {
        "name": "Yorkshire"
        ,
        "map_id" :1
        ,
        "hasCenter" :False

    }
      
]
regionsToulouse=[ 
        {
        "name": "Toulouse"
        ,
        "map_id":1
        ,
        "hasCenter":False
        }
]

dispositionUnite=[
    
    #germany : 
    {
        "type_unit_id": 2, #bateau 
        
        "region_id":34, #kiel
        
        "power_id" : 1  #germany
    },
    {
        "type_unit_id": 1,
        
        "region_id":11, #berlin
        
        "power_id" : 1
    },
    {
        "type_unit_id": 1,
        
        "region_id":  41 ,#munich
        
        "power_id" : 1
    },
    #AUTRICHE-HONGRIE 
    {
        "type_unit_id": 2, #bateau
        
        "region_id":63, #TRIESTE
        
        "power_id" : 2
    },
    {
        "type_unit_id": 1, #armée
        
        "region_id":14, #BUDAPEST
        
        "power_id" : 2 
    },
    {
        "type_unit_id": 1,
        
        "region_id":70,   #VIENNE
        
        "power_id" : 2
    },
    #France
    {
        "type_unit_id": 2,
        
        "region_id":13, #BREST
        
        "power_id" : 3
    },
    {
        "type_unit_id": 1,
        
        "region_id":38, #MARSEILLE
        
        "power_id" : 3
    },
    {
        "type_unit_id": 1,
        
        "region_id":46, #PARIS
        
        "power_id" : 3
    },
    #GRANDE BRETAGNE 
    {
        "type_unit_id": 2,
        
        "region_id":21, #EDIMBOURG
        
        "power_id" : 4
    },
    {
        "type_unit_id": 2,
        
        "region_id":37,#LONDRES
        
        "power_id" : 4
    },
    {
        "type_unit_id": 2,
        
        "region_id":35, #LIVERPOOL
        
        "power_id" : 4
    },
    #ITALIE
    {
        "type_unit_id": 2,
        
        "region_id":42, #NAPLES
        
        "power_id" : 5
    },
    {
        "type_unit_id": 1,
        
        "region_id":51, #ROME
        
        "power_id" : 5
    },
    {
        "type_unit_id": 1,
        
        "region_id":69, #VENISE
        
        "power_id" : 5
    },
    #RUSSIE
    {
        "type_unit_id": 2,
        
        "region_id":60,  # ST PETERSBOURG
        
        "power_id" : 6
    },
    {
        "type_unit_id": 2, 
        
        "region_id":1,  # ODESSA à revoir
        
        "power_id" : 6
    },
    
    {
        "type_unit_id": 1,
        
        "region_id":40, #MOSCOU
        
        "power_id" : 6
    },
    {
        "type_unit_id": 1,
        
        "region_id":2, #VARSOVIE # à revoir
        
        "power_id" : 6
    },
    #TURQUIE
    {
        "type_unit_id": 2,
        
        "region_id":7, #ANKARA
        
        "power_id" : 7
    },
    {
        "type_unit_id": 1,
        
        "region_id":18, #CONSTANTINOPLE
        
        "power_id" : 7
    },
    {
        "type_unit_id": 1,
        
        "region_id":58, #SMYRNE
        
        "power_id" : 7
    },
    
]

voisinage=[
    
     {  
        "src_region_id": 30,
        "dst_region_id" : [12,22,13],
         
     }, 
 ]



def fillTableMap(data):
    return

def insertMaps(maps,session,table):
    for m in maps :
        new_maps=table(name=m["name"])
        session.add(new_maps)
        session.commit()
        
def insertColor(colors,session,table,):
    for c in colors :
        new_color=table(rgb=c["rgb"])
        session.add(new_color)
        session.commit()
        
def insertPower(powers,session,table):
    
    for p in powers :
        new_powers=table(name=p["name"],color_id=p["color_id"],map_id=p["map_id"])
        session.add(new_powers)
        session.commit()

def insertTypeRegion(typeRegion,session,table)   :
    for tr in typeRegion :
        new_typeRegion=table(name=tr["name"])
        session.add(new_typeRegion)
        session.commit() 
        
def insertTypeUnite(typeUnite,session,table)   :
    for tu in typeUnite :
        new_typeUnite=table(name=tu["name"])
        session.add(new_typeUnite)
        session.commit() 

def insertRegion(regions,session,table):
    for r in regions:
        new_region=table(name=r["name"],map_id=r["map_id"],hasCenter=r["hasCenter"])
        session.add(new_region)
        session.commit() 
        
def insertion_voisin(voisinage,engine,table):
        for v in voisinage:
            liste_dest=v["dst_region_id"]
            for dest in liste_dest:
                new_voisinage=table.insert().values(src_region_id=v["src_region_id"],dst_region_id=dest);
                engine.execute(new_voisinage) 
                
                new_voisinage=table.insert().values(src_region_id= dest,dst_region_id=v["src_region_id"]);
                engine.execute(new_voisinage) 
def insert_disposition_unite(dispositionUnite,session,table):
     for d in dispositionUnite:
        new_disp=table(type_unit_id=d["type_unit_id"],region_id=d["region_id"],power_id=d["power_id"])
        session.add(new_disp)
        session.commit()
