from sqlalchemy import create_engine

colors=[
    {
        "id":1,
        "rgb":"black"  
    },
    {
        "id":2,
        "rgb" :"yellow"
    },
    {
        "id":3,
        "rgb" :"blue"
    },
    
    {
        "id":4,
        "rgb" :"pink"
    },
    
    {
        "id":5,
        "rgb" :"red"
        
    },
    {
        "id":6,
        "rgb" :"white"
        
    },
    {
        "id":7,
        "rgb" :"green"
        
    },
]
maps=[
    {
        "id":1,
        "name":"Europe"
    },
    {
        "id":2,
        "name":"Strasbourg"
    }
]



powers=[
    {
        "id":1,
        "name" : "Germany",
        "color_id":1,
        "map_id" : 1
    },
    {
        "id":2,
        "name": "Austria-Hungary", 
        "color_id":2,
        "map_id" : 1
    },
    
    {
        "id":3,
        "name": "France",
        "color_id":3,
        "map_id" : 1
    },
    
    {
        "id":4,
        "name": "Great-Britain",  
        "color_id":4,
        "map_id" : 1
    },
    
    {
        "id":5,
        "name": "Italy",
        "color_id":5,
        "map_id" : 1
    },
    
    {
        "id":6,
        "name": "Russia",
        "color_id":6,
        "map_id" : 1
    },
    
    {
        "id":7,
        "name": "Turkey",
        "color_id":7,
        "map_id" : 1
    },
]

typeRegion=[
    {
        "id":1,
        "name":"LAND"
    },
    {
        "id":2,
        "name":"SEA"
    },
    {
        "id":3,
        "name":"COAST"
    },
]

typeUnite=[
    {
        "id":1,
        "name":"ARMY"
    },
    {
        "id":2,
        "name":"FLEET"
    },
    
    {
        "id":3,
        "name": "CENTER"
    }
   
]

regions=[

        {"id":1,"name" : "Norwegian Sea", "map_id" : 1, "hasCenter": False},
        {"id":2,"name" : "North Sea", "map_id" : 1, "hasCenter": False},
        {"id":3,"name" : "Switzerland", "map_id" : 1, "hasCenter": False},
        {"id":4,"name" : "Adriatic Sea", "map_id" : 1, "hasCenter": False},
        {"id":5,"name" : "Aegean Sea", "map_id" : 1, "hasCenter": False},
        {"id":6,"name" : "Albania", "map_id" : 1, "hasCenter": False},
        {"id":7,"name" : "Ankara", "map_id" : 1, "hasCenter": True},
        {"id":8,"name" : "Apulia", "map_id" : 1, "hasCenter": False},
        {"id":9,"name" : "Armenia", "map_id" : 1, "hasCenter": False},
        {"id":10,"name" : "Baltic Sea", "map_id" : 1, "hasCenter": False},
        {"id":11,"name" : "Barents Sea", "map_id" : 1, "hasCenter": False},
        {"id":12,"name" : "Belgium", "map_id" : 1, "hasCenter": False},
        {"id":13,"name" : "Berlin", "map_id" : 1, "hasCenter": True},
        {"id":14,"name" : "Black Sea", "map_id" : 1, "hasCenter": False},
        {"id":15,"name" : "Bohemia", "map_id" : 1, "hasCenter": False},
        {"id":16,"name" : "Brest", "map_id" : 1, "hasCenter": True},
        {"id":17,"name" : "Budapest", "map_id" : 1, "hasCenter": True},
        {"id":18,"name" : "Bulgaria", "map_id" : 1, "hasCenter": False},
        {"id":19,"name" : "Burgundy", "map_id" : 1, "hasCenter": False},
        {"id":20,"name" : "Clyde", "map_id" : 1, "hasCenter": False},
        {"id":21,"name" : "Constantinople", "map_id" : 1, "hasCenter": True},
        {"id":22,"name" : "Denmark", "map_id" : 1, "hasCenter":True},
        {"id":23,"name" : "Eastern Mediterranean", "map_id" : 1, "hasCenter": False},
        {"id":24,"name" : "Edinburgh", "map_id" : 1, "hasCenter": True},
        {"id":25,"name" : "English Channel", "map_id" : 1, "hasCenter": False},
        {"id":26,"name" : "Finland", "map_id" : 1, "hasCenter": False},
        {"id":27,"name" : "Galicia", "map_id" : 1, "hasCenter": False},
        {"id":28,"name" : "Gascony", "map_id" : 1, "hasCenter": False},
        {"id":29,"name" : "Greece", "map_id" : 1, "hasCenter": False},
        {"id":30,"name" : "Gulf of Lyon", "map_id" : 1, "hasCenter": False},
        {"id":31,"name" : "Gulf of Bothnia", "map_id" : 1, "hasCenter": False},
        {"id":32,"name" : "Helgoland Bight", "map_id" : 1, "hasCenter": False},
        {"id":33,"name" : "Holland", "map_id" : 1, "hasCenter": False},
        {"id":34,"name" : "Ionian Sea", "map_id" : 1, "hasCenter": False},
        {"id":35,"name" : "Irish Sea", "map_id" : 1, "hasCenter": False},
        {"id":36,"name" : "Kiel", "map_id" : 1, "hasCenter": True},
        {"id":37,"name" : "Liverpool", "map_id" : 1, "hasCenter": True},
        {"id":38,"name" : "Livonia", "map_id" : 1, "hasCenter": False},
        {"id":39,"name" : "London", "map_id" : 1, "hasCenter": True},
        {"id":40,"name" : "Marseilles", "map_id" : 1, "hasCenter": False},
        {"id":41,"name" : "Mid-Atlantic Ocean", "map_id" : 1, "hasCenter": False},
        {"id":42,"name" : "Moscow", "map_id" : 1, "hasCenter": True},
        {"id":43,"name" : "Munich", "map_id" : 1, "hasCenter": True},
        {"id":44,"name" : "Naples", "map_id" : 1, "hasCenter": True},
        {"id":45,"name" : "North Atlantic Ocean", "map_id" : 1, "hasCenter": False},
        {"id":46,"name" : "North Africa", "map_id" : 1, "hasCenter": False},
        {"id":47,"name" : "Norway", "map_id" : 1, "hasCenter": False},
        {"id":48,"name" : "Paris", "map_id" : 1, "hasCenter": True},
        {"id":49,"name" : "Picardy", "map_id" : 1, "hasCenter": False},
        {"id":50,"name" : "Piedmont", "map_id" : 1, "hasCenter": False},
        {"id":51,"name" : "Portugal", "map_id" : 1, "hasCenter": False},
        {"id":52,"name" : "Prussia", "map_id" : 1, "hasCenter": False},
        {"id":53,"name" : "Rome", "map_id" : 1, "hasCenter": True},
        {"id":54,"name" : "Ruhr", "map_id" : 1, "hasCenter": False},
        {"id":55,"name" : "Rumania", "map_id" : 1, "hasCenter": False},
        {"id":56,"name" : "Serbia", "map_id" : 1, "hasCenter": False},
        {"id":57,"name" : "Sevastopol", "map_id" : 1, "hasCenter": False},
        {"id":58,"name" : "Silesia", "map_id" : 1, "hasCenter": False},
        {"id":59,"name" : "Skagerrak", "map_id" : 1, "hasCenter": False},
        {"id":60,"name" : "Smyrna", "map_id" : 1, "hasCenter": True},
        {"id":61,"name" : "Spain", "map_id" : 1, "hasCenter": False},
        {"id":62,"name" : "St Petersburg", "map_id" : 1, "hasCenter": True},
        {"id":63,"name" : "Sweden", "map_id" : 1, "hasCenter": False},
        {"id":64,"name" : "Syria", "map_id" : 1, "hasCenter": False},
        {"id":65,"name" : "Trieste", "map_id" : 1, "hasCenter": True},
        {"id":66,"name" : "Tunis", "map_id" : 1, "hasCenter": False},
        {"id":67,"name" : "Tuscany", "map_id" : 1, "hasCenter": False},
        {"id":68,"name" : "Tyrolia", "map_id" : 1, "hasCenter": False},
        {"id":69,"name" : "Tyrrhenian Sea", "map_id" : 1, "hasCenter": False},
        {"id":70,"name" : "Ukraine", "map_id" : 1, "hasCenter": False},
        {"id":71,"name" : "Venice", "map_id" : 1, "hasCenter": True},
        {"id":72,"name" : "Vienna", "map_id" : 1, "hasCenter": True},
        {"id":73,"name" : "Wales", "map_id" : 1, "hasCenter": False},
        {"id":74,"name" : "Warsaw", "map_id" : 1, "hasCenter": False},
        {"id":75,"name" : "Western Mediterranean", "map_id" : 1, "hasCenter": False},
        {"id":76,"name" : "Yorkshire", "map_id" : 1, "hasCenter": False}
    ]
    
dispositionUnite= [
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
        
        "region_id":57,  # ODESSA à revoir
        
        "power_id" : 6
    },
    
    {
        "type_unit_id": 1,
        
        "region_id":42, #MOSCOU
        
        "power_id" : 6
    },
    {
        "type_unit_id": 1,
        
        "region_id":74, #VARSOVIE
        
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
    {"src_region_id": 44, "dst_region_id": [15]},
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
    {"src_region_id": 74, "dst_region_id": [44]}

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
    {"id":1, "name":"CONFIGURATION"},
    {"id":2, "name":"GAME"},
    {"id":3, "name":"END"},
]
typeOders=[
    
    {
        "id":1,
        "name":"ATTACK"
    },
    {
        "id":2,
        "name":"HOLD"
    },
    {
        "id":3,
        "name":"SUPPORT"
    },
    {
        "id":4,
        "name":"CONVOY"
    }
]

state=[
    
    {
        "name": "START"
    }
    
]
games=[
    {   
        "id": 1,
        "name" : "Amdadou",
        "password":"cool",
        "map_id" : 1,
        "state_id": 1,
        "num_tour" :0
    }
    
]

players =[
    {
        "id":1,
        "username":"Ladislav",
         "is_admin":True,
          "game_id": 1
              
    },
    {
        "id":2,
        "username":"Emmanuel",
        "is_admin":False,
        "game_id": 1
        
              
    },
    {
        "id":3,
        "username":"Emmanuel2",
        "is_admin":False,
        "game_id": 1
               
    },
    {
        "id":4,
        "username":"Mariame",
        "is_admin":False,
        "game_id": 1    
    },
    {
        "id":5,
        "username":"Intissar",
        "is_admin":False,
        "game_id": 1    
    },
    {
        "id":6,
        "username":"Melissa",
        "is_admin":False,
        "game_id": 1    
    },
    {
        "id":7,
        "username":"Loic",
        "is_admin":False,
        "game_id": 1    
    },
]
playersPowers=[
    {
        "power_id":1,
        "player_id":1
    },
    {
        "power_id":2,
        "player_id":2
    },
    {
        "power_id":3,
        "player_id":3
    },
    {
        "power_id":4,
        "player_id":4
    },
    {
        "power_id":5,
        "player_id":5
    },
    {
        "power_id":6,
        "player_id":6
    },
    {
        "power_id":7,
        "player_id":7
    },
]
unites=[
    #germany
    {
        "id":1,
        "type_unit_id":2, #bateau
        "src_region_id":36, #kiel
        "cur_region_id":36,
        "player_power_power_id":1,
        "player_power_player_id":1
    },
    {
        "id":2,
        "type_unit_id":1, #Army
        "src_region_id":13, #berlin
        "cur_region_id":13,
        "player_power_power_id":1,
        "player_power_player_id":1
    },
    {
        "id":3,
        "type_unit_id":1, #Army
        "src_region_id":43, #munich
        "cur_region_id":43,
        "player_power_power_id":1,
        "player_power_player_id":1
    },
    #france
    {
        "id":4,
        "type_unit_id":2, #bateau
        "src_region_id":16, #Brest
        "cur_region_id":16,
        "player_power_power_id":3,
        "player_power_player_id":3
    },
    {
        "id":5,
        "type_unit_id":1, #Army
        "src_region_id":40, #Marseille
        "cur_region_id":40,
        "player_power_power_id":3,
        "player_power_player_id":3
    },
    {
        "id":6,
        "type_unit_id":1, #Army
        "src_region_id":48, #Paris
        "cur_region_id":48,
        "player_power_power_id":3,
        "player_power_player_id":3
    }
]
unitMaritimeConvoy=[
    # for convoy france
    {
        "id":7,
        "type_unit_id":2, #bateau
        "src_region_id":75, #Mediterrane
        "cur_region_id":75,
        "player_power_power_id":3,
        "player_power_player_id":3
    },
    {
        "id":8,
        "type_unit_id":2, #bateau
        "src_region_id":30, #Gulf of lyon
        "cur_region_id":30,
        "player_power_power_id":3,
        "player_power_player_id":3
    },
    #turkeey for convoy
    {
        "id":9,
        "type_unit_id":1, #Army
        "src_region_id":60, #Smyrna
        "cur_region_id":60,
        "player_power_power_id":7,
        "player_power_player_id":7
    },

    {
        "id":10,
        "type_unit_id":2, #bateeu
        "src_region_id":5, #Agean Sea
        "cur_region_id":5,
        "player_power_power_id":7,
        "player_power_player_id":7
    },
    #italie for  convoy
    {
        "id":11,
        "type_unit_id":2, #bateau
        "src_region_id":34, #Ionian Sea
        "cur_region_id":34,
        "player_power_power_id":5,
        "player_power_player_id":5
    },
    {
        "id":12,
        "type_unit_id":2, #Bateau
        "src_region_id":69, #Agean Sea
        "cur_region_id":69,
        "player_power_power_id":5,
        "player_power_player_id":5
    },
    #British
    {
        "id":13,
        "type_unit_id":2, #Bateau
        "src_region_id":45, #Athlantic
        "cur_region_id":45,
        "player_power_power_id":4,
        "player_power_player_id":4
    },
    {
        "id":14,
        "type_unit_id":2, #Bateau
        "src_region_id":25, #English channel
        "cur_region_id":25,
        "player_power_power_id":4,
        "player_power_player_id":4
    }
]

orderAttack=[
    #unite de munich attaque berlin
    {
        "id":1,
        "type_order_id": 1, #Attack
        "src_region_id":13, #berlin
        "dst_region_id" :43, #munich
        "unit_id":2,
        "num_tour" :0
        
    },

    {
        "id":2,
        "type_order_id": 1, #Attack
        "src_region_id":13, #berlin
        "dst_region_id" :58, #Silesia
        "unit_id":2,
        "num_tour" :0   
    },
    {
        "id":3,
        "type_order_id": 1, #Attack
        "src_region_id":13, #berlin
        "dst_region_id" :48, #Paris
        "unit_id":2,
        "num_tour" :0   
    },

    #smyrna Attack brest
    {
        "id":4,
        "type_order_id": 1, #Attack
        "src_region_id":60,
        "dst_region_id" :16,
        "unit_id":9,
        "num_tour" :0   
    },

]
orderConvoy=[
    #unit in Agean sea convoy unit Smyrnat  which go in brest
    {
        "id":5,
        "type_order_id": 4, #convoy
        "src_region_id":5,
        "dst_region_id" :16,
        "unit_id":10,
        "other_unit_id":9,
        "num_tour" :0 #unit present smyrna
    },
    #unit in ion Saea convoy unit Smyrnat which go in brest
    {
        "id":6,
        "type_order_id": 4, #convoy
        "src_region_id":34,
        "dst_region_id" :16,
        "unit_id":11,
        "other_unit_id":9,
        "num_tour" :0    #unit present smyrna
    },
    #unit in Tyrrhenien Sea convoy unit Smyrnat which go in brest
    {
        "id":7,
        "type_order_id": 4,  # convoy
        "src_region_id": 69,
        "dst_region_id": 16,
        "unit_id": 12,
        "other_unit_id": 9,
        "num_tour" :0    #unit present smyrna
    },

    #unit in meditarrene convoy unit Smyrnat which go in brest
    {
        "id":8,
        "type_order_id": 4,  # convoy
        "src_region_id":75,
        "dst_region_id": 16,
        "unit_id": 7,
        "other_unit_id": 9, #unit present smyrna
        "num_tour" :0   
    },
    #unit in athlantic convoy unit Smyrnat which go in brest
    {
        "id":9,
        "type_order_id": 4,  # convoy
        "src_region_id" :45,
        "dst_region_id": 16,
        "unit_id": 13,
        "other_unit_id": 9, #unit present smyrna
         "num_tour" :0
        
    },


]
floatAttack=[
     #fleet Athlantic Attack brest(cost) 
    {
        "id":10,
        "type_order_id": 1, #Attack
        "src_region_id":45,
        "dst_region_id" :16,
        "unit_id":13,
        "num_tour" :0   
    },
    #fleet Tyrrhenien Sea Attack ion Saea(maritime)
    {
        "id":11,
        "type_order_id": 1, #Attack
        "src_region_id":69,
        "dst_region_id" :34,
        "unit_id":13,
        "num_tour" :0   
    },
    #fleet brest  Attack gaskony cotiére
    {
        "id":12,
        "type_order_id": 1, #Attack
        "src_region_id":16,
        "dst_region_id" :28,
        "unit_id":13,
        "num_tour" :0   
    },
    {
        "id":13,
        "type_order_id": 1, #Attack
        "src_region_id":16,
        "dst_region_id" :3,
        "unit_id":1,
        "num_tour" :1
    }, 
]


def fillTableMap(data):
    return

def insertMaps(maps,session,table):
    for m in maps :
        new_maps=table(id=m["id"], name=m["name"])
        session.add(new_maps)
        session.commit()
        
def insertColor(colors,session,table):
    for c in colors :
        new_color=table(id=c["id"], rgb=c["rgb"])
        session.add(new_color)
        session.commit()
        
def insertPower(powers,session,table):
    
    for p in powers :
        new_powers=table(id=p["id"], name=p["name"],color_id=p["color_id"],map_id=p["map_id"])
        session.add(new_powers)
        session.commit()

def insertTypeRegion(typeRegion,session,table)   :
    for tr in typeRegion :
        new_typeRegion=table(id=tr["id"], name=tr["name"])
        session.add(new_typeRegion)
        session.commit() 
        
def insertTypeUnite(typeUnite,session,table)   :
    for tu in typeUnite :
        new_typeUnite=table(id=tu["id"], name=tu["name"])
        session.add(new_typeUnite)
        session.commit() 

def insertRegion(regions,session,table):
    for r in regions:
        new_region=table(id=r["id"],name=r["name"],map_id=r["map_id"],hasCenter=r["hasCenter"])
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
def insertTypeOrder(typeOrder,session,table)   :
    for tO in typeOrder :
        new_typeOrder=table(id=tO["id"], name=tO["name"])
        session.add(new_typeOrder)
        session.commit() 
        
def insertState(states,session,table)   :
    for s in states :
        new_states=table(id=s["id"], name=s["name"])
        session.add(new_states)
        session.commit()
def insertGame(games,session,table):
    for g in games :
        new_games=table(id=g["id"], name=g["name"],password=g["password"],map_id=g["map_id"],state_id=g["state_id"],num_tour=g["num_tour"])
        session.add(new_games)
        session.commit() 
def insertPlayer(players,session,table):
    for p in players :
        new_players=table(id=p["id"],username=p["username"],is_admin=p["is_admin"],game_id=p["game_id"])
        session.add(new_players)
        session.commit()
def insertPlayerPower(playersPowers,engine,table):
        for p in playersPowers:
                new_line=table.insert().values(power_id=p["power_id"],player_id=p["player_id"]);
                engine.execute(new_line) 
def insertUnite(unite,session,table):
     for u in unite:
        new_unite=table(id=u["id"], type_unit_id=u["type_unit_id"],src_region_id=u["src_region_id"],cur_region_id=u["cur_region_id"],player_power_power_id=u["player_power_power_id"],player_power_player_id=u["player_power_player_id"])
        session.add(new_unite)
        session.commit()
def insertOrderAttack(orderAttack,session,table):
    for o in orderAttack :
        new_orderAttack=table(id=o["id"],type_order_id=o["type_order_id"],src_region_id=o["src_region_id"], dst_region_id=o["dst_region_id"],unit_id=o["unit_id"],num_tour=o["num_tour"])
        session.add(new_orderAttack)
        session.commit()
def insertOrderConvoy(orderConvoy,session,table):
    for o in orderConvoy :
        new_orderConvoy=table(id=o["id"],type_order_id=o["type_order_id"],src_region_id=o["src_region_id"], dst_region_id=o["dst_region_id"],unit_id=o["unit_id"],other_unit_id=o["other_unit_id"],num_tour=o["num_tour"])
        session.add(new_orderConvoy)
        session.commit()