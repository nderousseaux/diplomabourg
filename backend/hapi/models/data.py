



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

