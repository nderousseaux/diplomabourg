



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
        "name": "Great-Britain",  
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
    {"id":1, "name":"CONFIGURATION"}
]
typeOders=[
    
    {
        "name":"ATTACK"
    },
    {
        "name":"HOLD"
    },
    {
        "name":"SUPPORT"
    },
    {
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
        "name" : "Amdadou",
        "password":"cool",
        "map_id" : 1,
        "state_id": 1,
        "nbtour" :0
    }
    
]

players =[
    {
        "username":"Ladislav",
         "is_admin":True,
          "game_id": 1
              
    },
    {
        "username":"Emmanuel",
        "is_admin":False,
        "game_id": 1
        
              
    },
    {
        "username":"Emmanuel",
        "is_admin":False,
        "game_id": 1
               
    },
    {
        "username":"Mariame",
        "is_admin":False,
        "game_id": 1    
    },
    {
        "username":"Intissar",
        "is_admin":False,
        "game_id": 1    
    },
    {
        "username":"Melissa",
        "is_admin":False,
        "game_id": 1    
    },
    {
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
        "type_unit_id":2, #bateau
        "src_region_id":36, #kiel
        "cur_region_id":36,
        "player_power_power_id":1,
        "player_power_player_id":1
    },
    {
        "type_unit_id":1, #Army
        "src_region_id":13, #berlin
        "cur_region_id":13,
        "player_power_power_id":1,
        "player_power_player_id":1
    },
    {
        "type_unit_id":1, #Army
        "src_region_id":43, #munich
        "cur_region_id":43,
        "player_power_power_id":1,
        "player_power_player_id":1
    },
    #france
    {
        "type_unit_id":2, #bateau
        "src_region_id":16, #Brest
        "cur_region_id":16,
        "player_power_power_id":3,
        "player_power_player_id":3
    },
    {
        "type_unit_id":1, #Army
        "src_region_id":40, #Marseille
        "cur_region_id":40,
        "player_power_power_id":3,
        "player_power_player_id":3
    },
    {
        "type_unit_id":1, #Army
        "src_region_id":48, #Paris
        "cur_region_id":48,
        "player_power_power_id":3,
        "player_power_player_id":3
    },
    {
        "type_unit_id":1, #Army
        "src_region_id":28, #gascony
        "cur_region_id":28,
        "player_power_power_id":3,
        "player_power_player_id":3
    }
]
unitMaritimeConvoy=[
    # for convoy france
    {
        "type_unit_id":2, #bateau
        "src_region_id":75, #Mediterrane
        "cur_region_id":75,
        "player_power_power_id":3,
        "player_power_player_id":3
    },
    {
        "type_unit_id":2, #bateau
        "src_region_id":30, #Gulf of lyon
        "cur_region_id":30,
        "player_power_power_id":3,
        "player_power_player_id":3
    },
    #turkeey for convoy
    {
        "type_unit_id":1, #Army
        "src_region_id":60, #Smyrna
        "cur_region_id":60,
        "player_power_power_id":7,
        "player_power_player_id":7
    },

    {
        "type_unit_id":2, #bateeu
        "src_region_id":5, #Agean Sea
        "cur_region_id":5,
        "player_power_power_id":7,
        "player_power_player_id":7
    },
    #italie for  convoy
    {
        "type_unit_id":2, #bateau
        "src_region_id":34, #Ionian Sea
        "cur_region_id":34,
        "player_power_power_id":5,
        "player_power_player_id":5
    },
    {
        "type_unit_id":2, #Bateau
        "src_region_id":69, #Agean Sea
        "cur_region_id":69,
        "player_power_power_id":5,
        "player_power_player_id":5
    },
    #British
    {
        "type_unit_id":2, #Bateau
        "src_region_id":45, #Athlantic
        "cur_region_id":45,
        "player_power_power_id":4,
        "player_power_player_id":4
    },
    {
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
        "type_order_id": 1, #Attack
        "src_region_id":13, #berlin
        "dst_region_id" :43, #munich
        "unit_id":2,
        "nbtour" :0,
        "gameid":1
        
    },

    {
        "type_order_id": 1, #Attack
        "src_region_id":13, #berlin
        "dst_region_id" :58, #Silesia
        "unit_id":2,
        "nbtour" :0   ,
        "gameid":1
    },
    
    {
        "type_order_id": 1, #Attack
        "src_region_id":13, #berlin
        "dst_region_id" :48, #Paris
        "unit_id":2,
        "nbtour" :0   ,
        "gameid":1
    },

    #smyrna Attack brest
    {
        "type_order_id": 1, #Attack
        "src_region_id":60,
        "dst_region_id" :16,
        "unit_id":9,
        "nbtour" :0   ,
        "gameid":1
    },

]
orderConvoy=[
    #unit in Agean sea convoy unit Smyrnat  which go in brest
    {
        "type_order_id": 4, #convoy
        "src_region_id":5,
        "dst_region_id" :16,
        "unit_id":10,
        "other_unit_id":9,
        "nbtour" :0,
        "gameid":1 #unit present smyrna
    },
    #unit in ion Saea convoy unit Smyrnat which go in brest
    {
        "type_order_id": 4, #convoy
        "src_region_id":34,
        "dst_region_id" :16,
        "unit_id":11,
        "other_unit_id":9,
        "nbtour" :0   ,
        "gameid":1 #unit present smyrna
    },
    #unit in Tyrrhenien Sea convoy unit Smyrnat which go in brest
    {
        "type_order_id": 4,  # convoy
        "src_region_id": 69,
        "dst_region_id": 16,
        "unit_id": 12,
        "other_unit_id": 9,
        "nbtour" :0   ,
        "gameid":1 #unit present smyrna
    },

    #unit in meditarrene convoy unit Smyrnat which go in brest
    {
        "type_order_id": 4,  # convoy
        "src_region_id":75,
        "dst_region_id": 16,
        "unit_id": 7,
        "other_unit_id": 9, #unit present smyrna
        "nbtour" :0   ,
        "gameid":1
    },
    #unit in athlantic convoy unit Smyrnat which go in brest
    {
        "type_order_id": 4,  # convoy
        "src_region_id" :45,
        "dst_region_id": 16,
        "unit_id": 13,
        "other_unit_id": 9, #unit present smyrna
         "nbtour" :0   ,
         "gameid":1
        
    },


]
floatAttack=[
     #fleet Athlantic Attack brest(cost) 
    {
        "type_order_id": 1, #Attack
        "src_region_id":45,
        "dst_region_id" :16,
        "unit_id":13,
        "nbtour" :0   ,
        "gameid":1
    },
    #fleet Tyrrhenien Sea Attack ion Saea(maritime)
    {
        "type_order_id": 1, #Attack
        "src_region_id":69,
        "dst_region_id" :34,
        "unit_id":13,
        "nbtour" :0   ,
        "gameid":1
    },
    #fleet brestAttack gaskony cotiére
    {
        "type_order_id": 1, #Attack
        "src_region_id":16,
        "dst_region_id" :28,
        "unit_id":13,
        "nbtour" :0   ,
        "gameid":1
    },
    {
        "type_order_id": 1, #Attack
        "src_region_id":16,
        "dst_region_id" :3,
        "unit_id":1,
        "nbtour" :1,
        "gameid":1
    },
    
    
]

ordreSoutient=[
    
    #fleet Tyrrhenien soutient défensive ion Saea(maritime)
    {
        "type_order_id": 3, #support
        "src_region_id":69,
        "dst_region_id" :34,
        "unit_id":13,
        "other_unit_id":11,
        "nbtour" :0 ,
        "gameid":1
        
        
    },
    #smyrna soutient défensive  brest
    {
        "type_order_id": 3, #support
        "src_region_id":60,
        "dst_region_id" :16,
        "unit_id":9,
        "other_unit_id": 4,
        "nbtour" :0,
        "gameid":1
        
        
        
    },
     #berlin soutient  défensif  #munish
    {
        "type_order_id": 3, #support
        "src_region_id":13, #berlin
        "dst_region_id" :43, #munish
        "unit_id":2,
        "other_unit_id": 3, 
        "nbtour" :0 ,
        "gameid":1
           
    }
]

AttackMutuel=[
    #paris attaque breste 
    {
        "type_order_id": 1, #Attack
        "src_region_id":48, #Paris
        "unit_id":6,
        "dst_region_id" :16, 
        "nbtour" :0   ,
        "gameid":1
    },
    #et brest Attaque Paris 
    {
        "type_order_id": 1, #Attack
        "src_region_id":16, #brest
        "unit_id":4,
        "dst_region_id" :48, #Paris 
        "nbtour" :0   ,
        "gameid":1
    },
    
    #fleet in ageen sea attack fleet in  ionSea  
    {
        "type_order_id": 1, #Attack
        "src_region_id":5, # AAgean sea 
        "dst_region_id" :34, #Ion Sea 
        "unit_id":13,
        "nbtour" :0   ,
        "gameid":1
    },
    # et fleet in ion sea attack fleet in Agean Sea 
    {
        "type_order_id": 1, #Attack
        "src_region_id":34,  #Ion Sea 
        "dst_region_id" :5,   #Agean sea 
        "unit_id":12,
        "nbtour" :0,
        "gameid":1
    },
    
    # army in gascony  attack army  in Marseille
    {
        "type_order_id": 1, #Attack
        "src_region_id":28,  #Gascony
        "dst_region_id" :40,   #Marseillle
        "unit_id":7,
        "nbtour" :0,
        "gameid":1
    },
    # army in  Marseille attack army  in gascony
    {
        "type_order_id": 1, #Attack
        "src_region_id":40,   #Marseillle
        "dst_region_id" :28,  #Gascony
        "unit_id":5,
        "nbtour" :0,
        "gameid":1
    },
    
]
CreatConflit=[
    
    #berlin  et munich attaquent silésie 
    #berlin attaque silésie 
    {
        "type_order_id": 1, #Attack
        "src_region_id":13, #Berlin
        "unit_id":2,
        "dst_region_id" :58, #sliésie 
        "nbtour" :0   ,
        "gameid":1
    },
    #munich attaque silésie
    {
        "type_order_id": 1, #Attack
        "src_region_id":43, #munich
        "unit_id":3,
        "dst_region_id" :58, #sliésie 
        "nbtour" :0   ,
        "gameid":1
    },
    #paris et breste attaque picardie 
    #paris attaque picardie 
    {
        "type_order_id": 1, #Attack
        "src_region_id":48, # paris
        "unit_id":6,
        "dst_region_id" :49, #picardie
        "nbtour" :0   ,
        "gameid":1
    },
    #brest attaque picardie 
    {
        "type_order_id": 1, #Attack
        "src_region_id":16, #brest
        "unit_id":4,
        "dst_region_id" :49, #picardie
        "nbtour" :0   ,
        "gameid":1
    }
    
]
soutientCoupe=[
    #gascony qui est attaqué par marseille soutient brest
    {
        "type_order_id": 3, #support
        "src_region_id":28, 
        "dst_region_id" :16, #brest
        "unit_id":7,
        "other_unit_id":4,
        "nbtour" :0 ,
        "gameid":1
        
        
    },
    #  flleet Agean sea attaqué par fleet de ion Sea  support smyrna Army 
    {
        "type_order_id": 3, #support
        "src_region_id":5, #agenan ses 
        "dst_region_id" :60,
        "unit_id":11,
        "other_unit_id": 10,
        "nbtour" :0,
        "gameid":1
      
        
    },
]
def fillTableMap(data):
    return

def insertMaps(maps,session,table):
    for m in maps :
        new_maps=table(name=m["name"])
        session.add(new_maps)
        session.commit()
        
def insertColor(colors,session,table):
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
def insertTypeOrder(typeOrder,session,table)   :
    for tO in typeOrder :
        new_typeOrder=table(name=tO["name"])
        session.add(new_typeOrder)
        session.commit() 
        
def insertState(states,session,table)   :
    for s in states :
        new_states=table(name=s["name"])
        session.add(new_states)
        session.commit()
def insertGame(games,session,table):
    for g in games :
        new_games=table(name=g["name"],password=g["password"],map_id=g["map_id"],state_id=g["state_id"],nbtour=g["nbtour"])
        session.add(new_games)
        session.commit() 
def insertPlayer(players,session,table):
    for p in players :
        new_players=table(username=p["username"],is_admin=p["is_admin"],game_id=p["game_id"])
        session.add(new_players)
        session.commit()
def insertPlayerPower(playersPowers,engine,table):
        for p in playersPowers:
                new_line=table.insert().values(power_id=p["power_id"],player_id=p["player_id"]);
                engine.execute(new_line) 
def insertUnite(unite,session,table):
     for u in unite:
        new_unite=table(type_unit_id=u["type_unit_id"],src_region_id=u["src_region_id"],cur_region_id=u["cur_region_id"],player_power_power_id=u["player_power_power_id"],player_power_player_id=u["player_power_player_id"])
        session.add(new_unite)
        session.commit()
def insertOrderAttack(orderAttack,session,table):
    for o in orderAttack :
        new_orderAttack=table(type_order_id=o["type_order_id"],src_region_id=o["src_region_id"], dst_region_id=o["dst_region_id"],unit_id=o["unit_id"],nbtour=o["nbtour"],gameid=o["gameid"])
        session.add(new_orderAttack)
        session.commit()
def insertOrderConvoy(orderConvoy,session,table):
    for o in orderConvoy :
        new_orderConvoy=table(type_order_id=o["type_order_id"],src_region_id=o["src_region_id"], dst_region_id=o["dst_region_id"],unit_id=o["unit_id"],other_unit_id=o["other_unit_id"],nbtour=o["nbtour"],gameid=o["gameid"])
        session.add(new_orderConvoy)
        session.commit()
def insertOrderSupport(orderSupport,session,table):
    for o in orderSupport :
        new_orderSupport=table(type_order_id=o["type_order_id"],src_region_id=o["src_region_id"], dst_region_id=o["dst_region_id"],unit_id=o["unit_id"],other_unit_id=o["other_unit_id"],nbtour=o["nbtour"],gameid=o["gameid"])
        session.add(new_orderSupport)
        session.commit()