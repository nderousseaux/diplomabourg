



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
        "name":"LAND"
    },
    {
        "name":"SEA"
    },
    {
        "name":"COAST"
    },
]

typeUnite=[
    {
        "name":"ARMY"
    },
    {
        "name":"FLEET"
    },
    
    {
        "name": "CENTER"
    }
   
]

regions=[

        {"name" : "Norwegian Sea", "map_id" : 1, "hasCenter": False},
        {"name" : "North Sea", "map_id" : 1, "hasCenter": False},
        {"name" : "Switzerland", "map_id" : 1, "hasCenter": False},
        {"name" : "Adriatic Sea", "map_id" : 1, "hasCenter": False},
        {"name" : "Aegean Sea", "map_id" : 1, "hasCenter": False},
        {"name" : "Albania", "map_id" : 1, "hasCenter": False},
        {"name" : "Ankara", "map_id" : 1, "hasCenter": True},
        {"name" : "Apulia", "map_id" : 1, "hasCenter": False},
        {"name" : "Armenia", "map_id" : 1, "hasCenter": False},
        {"name" : "Baltic Sea", "map_id" : 1, "hasCenter": False},
        {"name" : "Barents Sea", "map_id" : 1, "hasCenter": False},
        {"name" : "Belgium", "map_id" : 1, "hasCenter": False},
        {"name" : "Berlin", "map_id" : 1, "hasCenter": True},
        {"name" : "Black Sea", "map_id" : 1, "hasCenter": False},
        {"name" : "Bohemia", "map_id" : 1, "hasCenter": False},
        {"name" : "Brest", "map_id" : 1, "hasCenter": True},
        {"name" : "Budapest", "map_id" : 1, "hasCenter": True},
        {"name" : "Bulgaria", "map_id" : 1, "hasCenter": False},
        {"name" : "Burgundy", "map_id" : 1, "hasCenter": False},
        {"name" : "Clyde", "map_id" : 1, "hasCenter": False},
        {"name" : "Constantinople", "map_id" : 1, "hasCenter": True},
        {"name" : "Denmark", "map_id" : 1, "hasCenter":True},
        {"name" : "Eastern Mediterranean", "map_id" : 1, "hasCenter": False},
        {"name" : "Edinburgh", "map_id" : 1, "hasCenter": True},
        {"name" : "English Channel", "map_id" : 1, "hasCenter": False},
        {"name" : "Finland", "map_id" : 1, "hasCenter": False},
        {"name" : "Galicia", "map_id" : 1, "hasCenter": False},
        {"name" : "Gascony", "map_id" : 1, "hasCenter": False},
        {"name" : "Greece", "map_id" : 1, "hasCenter": False},
        {"name" : "Gulf of Lyon", "map_id" : 1, "hasCenter": False},
        {"name" : "Gulf of Bothnia", "map_id" : 1, "hasCenter": False},
        {"name" : "Helgoland Bight", "map_id" : 1, "hasCenter": False},
        {"name" : "Holland", "map_id" : 1, "hasCenter": False},
        {"name" : "Ionian Sea", "map_id" : 1, "hasCenter": False},
        {"name" : "Irish Sea", "map_id" : 1, "hasCenter": False},
        {"name" : "Kiel", "map_id" : 1, "hasCenter": True},
        {"name" : "Liverpool", "map_id" : 1, "hasCenter": True},
        {"name" : "Livonia", "map_id" : 1, "hasCenter": False},
        {"name" : "London", "map_id" : 1, "hasCenter": True},
        {"name" : "Marseilles", "map_id" : 1, "hasCenter": False},
        {"name" : "Mid-Atlantic Ocean", "map_id" : 1, "hasCenter": False},
        {"name" : "Moscow", "map_id" : 1, "hasCenter": True},
        {"name" : "Munich", "map_id" : 1, "hasCenter": True},
        {"name" : "Naples", "map_id" : 1, "hasCenter": True},
        {"name" : "North Atlantic Ocean", "map_id" : 1, "hasCenter": False},
        {"name" : "North Africa", "map_id" : 1, "hasCenter": False},
        {"name" : "Norway", "map_id" : 1, "hasCenter": False},
        {"name" : "Paris", "map_id" : 1, "hasCenter": True},
        {"name" : "Picardy", "map_id" : 1, "hasCenter": False},
        {"name" : "Piedmont", "map_id" : 1, "hasCenter": False},
        {"name" : "Portugal", "map_id" : 1, "hasCenter": False},
        {"name" : "Prussia", "map_id" : 1, "hasCenter": False},
        {"name" : "Rome", "map_id" : 1, "hasCenter": True},
        {"name" : "Ruhr", "map_id" : 1, "hasCenter": False},
        {"name" : "Rumania", "map_id" : 1, "hasCenter": False},
        {"name" : "Serbia", "map_id" : 1, "hasCenter": False},
        {"name" : "Sevastopol", "map_id" : 1, "hasCenter": False},
        {"name" : "Silesia", "map_id" : 1, "hasCenter": False},
        {"name" : "Skagerrak", "map_id" : 1, "hasCenter": False},
        {"name" : "Smyrna", "map_id" : 1, "hasCenter": True},
        {"name" : "Spain", "map_id" : 1, "hasCenter": False},
        {"name" : "St Petersburg", "map_id" : 1, "hasCenter": True},
        {"name" : "Sweden", "map_id" : 1, "hasCenter": False},
        {"name" : "Syria", "map_id" : 1, "hasCenter": False},
        {"name" : "Trieste", "map_id" : 1, "hasCenter": True},
        {"name" : "Tunis", "map_id" : 1, "hasCenter": False},
        {"name" : "Tuscany", "map_id" : 1, "hasCenter": False},
        {"name" : "Tyrolia", "map_id" : 1, "hasCenter": False},
        {"name" : "Tyrrhenian Sea", "map_id" : 1, "hasCenter": False},
        {"name" : "Ukraine", "map_id" : 1, "hasCenter": False},
        {"name" : "Venice", "map_id" : 1, "hasCenter": True},
        {"name" : "Vienna", "map_id" : 1, "hasCenter": True},
        {"name" : "Wales", "map_id" : 1, "hasCenter": False},
        {"name" : "Warsaw", "map_id" : 1, "hasCenter": False},
        {"name" : "Western Mediterranean", "map_id" : 1, "hasCenter": False},
        {"name" : "Yorkshire", "map_id" : 1, "hasCenter": False}
    ]
    

dispositionUnite=[
    
    #germany : 
    {
        "type_unit_id": 2, #bateau 
        
        "region_id":36, #kiel
        
        "power_id" : 1  #germany
    },
    {
        "type_unit_id": 1,
        
        "region_id":13, #berlin
        
        "power_id" : 1
    },
    {
        "type_unit_id": 1,
        
        "region_id":  43 ,#munich
        
        "power_id" : 1
    },
    #AUTRICHE-HONGRIE 
    {
        "type_unit_id": 2, #bateau
        
        "region_id":65, #TRIESTE
        
        "power_id" : 2
    },
    {
        "type_unit_id": 1, #armée
        
        "region_id":17, #BUDAPEST
        
        "power_id" : 2 
    },
    {
        "type_unit_id": 1,
        
        "region_id":72,   #VIENNE
        
        "power_id" : 2
    },
    #France
    {
        "type_unit_id": 2,
        
        "region_id":16, #BREST
        
        "power_id" : 3
    },
    {
        "type_unit_id": 1,
        
        "region_id":40, #MARSEILLE
        
        "power_id" : 3
    },
    {
        "type_unit_id": 1,
        
        "region_id":48, #PARIS
        
        "power_id" : 3
    },
    #GRANDE BRETAGNE 
    {
        "type_unit_id": 2,
        
        "region_id":24, #EDIMBOURG
        
        "power_id" : 4
    },
    {
        "type_unit_id": 2,
        
        "region_id":39,#LONDRES
        
        "power_id" : 4
    },
    {
        "type_unit_id": 2,
        
        "region_id":37, #LIVERPOOL
        
        "power_id" : 4
    },
    #ITALIE
    {
        "type_unit_id": 2,
        
        "region_id":44, #NAPLES
        
        "power_id" : 5
    },
    {
        "type_unit_id": 1,
        
        "region_id":53, #ROME
        
        "power_id" : 5
    },
    {
        "type_unit_id": 1,
        
        "region_id":71, #VENISE
        
        "power_id" : 5
    },
    #RUSSIE
    {
        "type_unit_id": 2,
        
        "region_id":62,  # ST PETERSBOURG
        
        "power_id" : 6
    },
    {
        "type_unit_id": 2, 
        
        "region_id":1,  # ODESSA à revoir
        
        "power_id" : 6
    },
    
    {
        "type_unit_id": 1,
        
        "region_id":42, #MOSCOU
        
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
        
        "region_id":21, #CONSTANTINOPLE
        
        "power_id" : 7
    },
    {
        "type_unit_id": 1,
        
        "region_id":60, #SMYRNE
        
        "power_id" : 7
    },
    
]

voisinage=[
    {"src_region_id": 0, "dst_region_id": [10,46,44,1]},
    {"src_region_id": 1, "dst_region_id": [46,23,75,38,31,21,58,11,24,32]},
    {"src_region_id": 2, "dst_region_id": [39,18,49,67,42]},
    {"src_region_id": 3, "dst_region_id": [7,70,64,5,33]},
    {"src_region_id": 4, "dst_region_id": [28,59,20,17,22,33]},
    {"src_region_id": 5, "dst_region_id": [64,55,33,28]},
    {"src_region_id": 6, "dst_region_id": [20,59,8,13]},
    {"src_region_id": 7, "dst_region_id": [52,43,70,33]},
    {"src_region_id": 8, "dst_region_id": [56,59,63,13]},
    {"src_region_id": 9, "dst_region_id": [62,21,12,35,51,37,30]},
    {"src_region_id": 10, "dst_region_id": [61,46]},
    {"src_region_id": 11, "dst_region_id": [18,32,48,24,53]},
    {"src_region_id": 12, "dst_region_id": [35,42,51,57]},
    {"src_region_id": 13, "dst_region_id": [56,54,20,17]},
    {"src_region_id": 14, "dst_region_id": [42,71,67,57,26]},
    {"src_region_id": 15, "dst_region_id": [47,48,27,24,40]},
    {"src_region_id": 16, "dst_region_id": [64,71,55,26,54]},
    {"src_region_id": 17, "dst_region_id": [55,54,28,20]},
    {"src_region_id": 18, "dst_region_id": [47,48,27,39,42,53]},
    {"src_region_id": 19, "dst_region_id": [23,36,44]},
    {"src_region_id": 20, "dst_region_id": [59]},
    {"src_region_id": 21, "dst_region_id": [31,58,62,35]},
    {"src_region_id": 22, "dst_region_id": [63,59,33]},
    {"src_region_id": 23, "dst_region_id": [36,75]},
    {"src_region_id": 24, "dst_region_id": [34,72,38,48,40]},
    {"src_region_id": 25, "dst_region_id": [46,62,61,30]},
    {"src_region_id": 26, "dst_region_id": [73,57,69,71,54]},
    {"src_region_id": 27, "dst_region_id": [47,39,40,60]},
    {"src_region_id": 28, "dst_region_id": [55,33]},
    {"src_region_id": 29, "dst_region_id": [60,49,39,66,74,68]},
    {"src_region_id": 30, "dst_region_id": [62,61,37]},
    {"src_region_id": 31, "dst_region_id": [32,35]},
    {"src_region_id": 32, "dst_region_id": [35,53]},
    {"src_region_id": 33, "dst_region_id": [65,43,68]},
    {"src_region_id": 34, "dst_region_id": [44,40,36,72]},
    {"src_region_id": 35, "dst_region_id": [53,42]},
    {"src_region_id": 36, "dst_region_id": [72,75,44]},
    {"src_region_id": 37, "dst_region_id": [41,61,73,51]},
    {"src_region_id": 38, "dst_region_id": [72,75]},
    {"src_region_id": 39, "dst_region_id": [49]},
    {"src_region_id": 40, "dst_region_id": [44,50,60,74,45]},
    {"src_region_id": 41, "dst_region_id": [61,56,69,73]},
    {"src_region_id": 42, "dst_region_id": [53,57,67]},
    {"src_region_id": 43, "dst_region_id": [52,68]},
    # {"src_region_id": 44, "dst_region_id": []},
    {"src_region_id": 45, "dst_region_id": [74,65]},
    {"src_region_id": 46, "dst_region_id": [62,58,61]},
    {"src_region_id": 47, "dst_region_id": [48]},
    # {"src_region_id": 48, "dst_region_id": []},
    {"src_region_id": 49, "dst_region_id": [67,66,70]},
    {"src_region_id": 50, "dst_region_id": [60]},
    {"src_region_id": 51, "dst_region_id": [57,73]},
    {"src_region_id": 52, "dst_region_id": [66,70,68]},
    # {"src_region_id": 53, "dst_region_id": []},
    {"src_region_id": 54, "dst_region_id": [56,69,55]},
    {"src_region_id": 55, "dst_region_id": [64]},
    {"src_region_id": 56, "dst_region_id": [69]},
    {"src_region_id": 57, "dst_region_id": [73]},
    {"src_region_id": 58, "dst_region_id": [62]},
    {"src_region_id": 59, "dst_region_id": [63]},
    {"src_region_id": 60, "dst_region_id": [74]},
    # {"src_region_id": 61, "dst_region_id": []},
    # {"src_region_id": 62, "dst_region_id": []},
    # {"src_region_id": 63, "dst_region_id": []},
    {"src_region_id": 64, "dst_region_id": [67,70,71]},
    {"src_region_id": 65, "dst_region_id": [74,68]},
    {"src_region_id": 66, "dst_region_id": [70,68]},
    {"src_region_id": 67, "dst_region_id": [70,71]},
    {"src_region_id": 68, "dst_region_id": [74]},
    {"src_region_id": 69, "dst_region_id": [73]},
    # {"src_region_id": 70, "dst_region_id": []},
    # {"src_region_id": 71, "dst_region_id": []},
    {"src_region_id": 72, "dst_region_id": [75]},
    # {"src_region_id": 73, "dst_region_id": []},
    # {"src_region_id": 74, "dst_region_id": []},
    # {"src_region_id": 75, "dst_region_id": []} 
 ]

reg_type_reg=[
    {"region_id" : 0, "type_region_id" : [1]},
    {"region_id" : 1, "type_region_id" : [1]},
    # {"region_id" : 2, "type_region_id" : [-1]},
    {"region_id" : 3, "type_region_id" : [1]},
    {"region_id" : 4, "type_region_id" : [1]},
    {"region_id" : 5, "type_region_id" : [0,2]},
    {"region_id" : 6, "type_region_id" : [0,2]},
    {"region_id" : 7, "type_region_id" : [0,2]},
    {"region_id" : 8, "type_region_id" : [0,2]},
    {"region_id" : 9, "type_region_id" : [1]},
    {"region_id" : 10, "type_region_id" : [1]},
    {"region_id" : 11, "type_region_id" : [0,2]},
    {"region_id" : 12, "type_region_id" : [0,2]},
    {"region_id" : 13, "type_region_id" : [1]},
    {"region_id" : 14, "type_region_id" : [0]},
    {"region_id" : 15, "type_region_id" : [0,2]},
    {"region_id" : 16, "type_region_id" : [0]},
    {"region_id" : 17, "type_region_id" : [0,2]},
    {"region_id" : 18, "type_region_id" : [0]},
    {"region_id" : 19, "type_region_id" : [0,2]},
    {"region_id" : 20, "type_region_id" : [0,2]},
    {"region_id" : 21, "type_region_id" : [0,2]},
    {"region_id" : 22, "type_region_id" : [1]},
    {"region_id" : 23, "type_region_id" : [0,2]},
    {"region_id" : 24, "type_region_id" : [1]},
    {"region_id" : 25, "type_region_id" : [0,2]},
    {"region_id" : 26, "type_region_id" : [0]},
    {"region_id" : 27, "type_region_id" : [0,2]},
    {"region_id" : 28, "type_region_id" : [0,2]},
    {"region_id" : 29, "type_region_id" : [1]},
    {"region_id" : 30, "type_region_id" : [1]},
    {"region_id" : 31, "type_region_id" : [1]},
    {"region_id" : 32, "type_region_id" : [0,2]},
    {"region_id" : 33, "type_region_id" : [1]},
    {"region_id" : 34, "type_region_id" : [1]},
    {"region_id" : 35, "type_region_id" : [0,2]},
    {"region_id" : 36, "type_region_id" : [0,2]},
    {"region_id" : 37, "type_region_id" : [0,2]},
    {"region_id" : 38, "type_region_id" : [0,2]},
    {"region_id" : 39, "type_region_id" : [0,2]},
    {"region_id" : 40, "type_region_id" : [1]},
    {"region_id" : 41, "type_region_id" : [0]},
    {"region_id" : 42, "type_region_id" : [0]},
    {"region_id" : 43, "type_region_id" : [0,2]},
    {"region_id" : 44, "type_region_id" : [1]},
    {"region_id" : 45, "type_region_id" : [0,2]},
    {"region_id" : 46, "type_region_id" : [0,2]},
    {"region_id" : 47, "type_region_id" : [0]},
    {"region_id" : 48, "type_region_id" : [0,2]},
    {"region_id" : 49, "type_region_id" : [0,2]},
    {"region_id" : 50, "type_region_id" : [0,2]},
    {"region_id" : 51, "type_region_id" : [0,2]},
    {"region_id" : 52, "type_region_id" : [0,2]},
    {"region_id" : 53, "type_region_id" : [0]},
    {"region_id" : 54, "type_region_id" : [0,2]},
    {"region_id" : 55, "type_region_id" : [0]},
    {"region_id" : 56, "type_region_id" : [0,2]},
    {"region_id" : 57, "type_region_id" : [0]},
    {"region_id" : 58, "type_region_id" : [1]},
    {"region_id" : 59, "type_region_id" : [0,2]},
    {"region_id" : 60, "type_region_id" : [0,2]},
    {"region_id" : 61, "type_region_id" : [0,2]},
    {"region_id" : 62, "type_region_id" : [0,2]},
    {"region_id" : 63, "type_region_id" : [0,2]},
    {"region_id" : 64, "type_region_id" : [0,2]},
    {"region_id" : 65, "type_region_id" : [0,2]},
    {"region_id" : 66, "type_region_id" : [0,2]},
    {"region_id" : 67, "type_region_id" : [0]},
    {"region_id" : 68, "type_region_id" : [1]},
    {"region_id" : 69, "type_region_id" : [0]},
    {"region_id" : 70, "type_region_id" : [0,2]},
    {"region_id" : 71, "type_region_id" : [0]},
    {"region_id" : 72, "type_region_id" : [0,2]},
    {"region_id" : 73, "type_region_id" : [0]},
    {"region_id" : 74, "type_region_id" : [1]},
    {"region_id" : 75, "type_region_id" : [0,2]}
    ]

states=[
    {"id":1, "name":"CONFIGURATION"}
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
                new_voisinage=table.insert().values(src_region_id=v["src_region_id"]+1,dst_region_id=dest+1);
                engine.execute(new_voisinage) 
                
                new_voisinage=table.insert().values(src_region_id= dest+1,dst_region_id=v["src_region_id"]+1);
                engine.execute(new_voisinage) 
                
                
def insert_disposition_unite(dispositionUnite,session,table):
     for d in dispositionUnite:
        new_disp=table(type_unit_id=d["type_unit_id"],region_id=d["region_id"],power_id=d["power_id"])
        session.add(new_disp)
        session.commit()
        
    
def insertRegTypeReg(reg_type_reg,engine,table):
        for r in reg_type_reg:
            type_list=r["type_region_id"]
            for dest in type_list:
                new_line=table.insert().values(region_id=r["region_id"]+1,type_region_id=dest+1);
                engine.execute(new_line) 

def insertState(state,session,table):
    for st in state:
        new_state=table(id=st["id"], name=st["name"])
        session.add(new_state)
        session.commit() 