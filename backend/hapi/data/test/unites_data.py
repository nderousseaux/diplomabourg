"""
Unités des joueurs
"""

unites=[
    #germany
    {
        "id":1,
        "type_unit_id":2, #bateau
        "src_region_id":36, #kiel
        "cur_region_id":36,
        "player_power_power_id":1,
        "player_power_player_id":1,
        "game_id": 1
    },
    {
        "id":2,
        "type_unit_id":1, #Army
        "src_region_id":13, #berlin
        "cur_region_id":13,
        "player_power_power_id":1,
        "player_power_player_id":1,
        "game_id": 1
    },
    {
        "id":3,
        "type_unit_id":1, #Army
        "src_region_id":43, #munich
        "cur_region_id":43,
        "player_power_power_id":1,
        "player_power_player_id":1,
        "game_id": 1
    },
    #france
    {
        "id":4,
        "type_unit_id":2, #bateau
        "src_region_id":16, #Brest
        "cur_region_id":16,
        "player_power_power_id":3,
        "player_power_player_id":3,
        "game_id": 1
    },
    {
        "id":5,
        "type_unit_id":1, #Army
        "src_region_id":40, #Marseille
        "cur_region_id":40,
        "player_power_power_id":3,
        "player_power_player_id":3,
        "game_id": 1
    },
    {
        "id":6,
        "type_unit_id":1, #Army
        "src_region_id":48, #Paris
        "cur_region_id":48,
        "player_power_power_id":3,
        "player_power_player_id":3,
        "game_id": 1
    },
    {
        "id":7,
        "type_unit_id":1, #Army
        "src_region_id":28, #gascony
        "cur_region_id":28,
        "player_power_power_id":3,
        "player_power_player_id":3,
        "game_id": 1
    }
]
unites_maritime_convoy=[
    # for convoy france
    {
        "id":8,
        "type_unit_id":2, #bateau
        "src_region_id":75, #Mediterrane
        "cur_region_id":75,
        "player_power_power_id":3,
        "player_power_player_id":3,
        "game_id": 1
    },
    {
        "id":9,
        "type_unit_id":2, #bateau
        "src_region_id":30, #Gulf of lyon
        "cur_region_id":30,
        "player_power_power_id":3,
        "player_power_player_id":3,
        "game_id": 1
    },
    #turkeey for convoy
    {
        "id":10,
        "type_unit_id":1, #Army
        "src_region_id":60, #Smyrna
        "cur_region_id":60,
        "player_power_power_id":7,
        "player_power_player_id":7,
        "game_id": 1
    },

    {
        "id":11,
        "type_unit_id":2, #bateeu
        "src_region_id":5, #Agean Sea
        "cur_region_id":5,
        "player_power_power_id":7,
        "player_power_player_id":7,
        "game_id": 1
    },
    #italie for  convoy
    {
        "id":12,
        "type_unit_id":2, #bateau
        "src_region_id":34, #Ionian Sea
        "cur_region_id":34,
        "player_power_power_id":5,
        "player_power_player_id":5,
        "game_id": 1
    },
    {
        "id":13,
        "type_unit_id":2, #Bateau
        "src_region_id":69, #Agean Sea
        "cur_region_id":69,
        "player_power_power_id":5,
        "player_power_player_id":5,
        "game_id": 1
    },
    #British
    {
        "id":14,
        "type_unit_id":2, #Bateau
        "src_region_id":45, #Athlantic
        "cur_region_id":45,
        "player_power_power_id":4,
        "player_power_player_id":4,
        "game_id": 1
    },
    {
        "id":15,
        "type_unit_id":2, #Bateau
        "src_region_id":25, #English channel
        "cur_region_id":25,
        "player_power_power_id":4,
        "player_power_player_id":4,
        "game_id": 1
    }
]
unites_soutient=[
    {
        "id":16,
        "type_unit_id":1, #Army
        "src_region_id":12, #Belgique(Belgium)
        "cur_region_id":12,
        "player_power_power_id":1,
        "player_power_player_id":1,
        "game_id": 1
    },
    {
        "id":17,
        "type_unit_id":1, #Army
        "src_region_id":19, #Bourgogne(Burgundy)
        "cur_region_id":19,
        "player_power_power_id":4,
        "player_power_player_id":4,
        "game_id": 1
    },
    {
        "id":18,
        "type_unit_id":1, #Army
        "src_region_id":52, #Prusse(Prussia)
        "cur_region_id":52,
        "player_power_power_id":3,
        "player_power_player_id":3,
        "game_id": 1
    },
    {
        "id":19,
        "type_unit_id":1, #Army
        "src_region_id":15, #Boheme(Bohemia)
        "cur_region_id":15,
        "player_power_power_id":2,
        "player_power_player_id":2,
        "game_id": 1
    },
    {
        "id":20,
        "type_unit_id":1, #Army
        "src_region_id":74, #Varsovie(warsaw)
        "cur_region_id":74,
        "player_power_power_id":5,
        "player_power_player_id":5,
        "game_id": 1
    }
]
unites_convoy_broken=[      
    {  # unit in North sea 
        "id":21,
        "type_unit_id":2, #bateau
        "src_region_id":2, #Norhe of the sea 
        "cur_region_id":2,
        "player_power_power_id":5, #italie
        "player_power_player_id":5,
        "game_id": 1
    },
    
    #Angleterre
    {
        "id":22,
        "type_unit_id":2, #bateau
        "src_region_id":39, #london
        "cur_region_id":39,
        "player_power_power_id":4,
        "player_power_player_id":4,
        "game_id": 1
    },
    #Russ 
    {
        "id":23,
        "type_unit_id":1, #Army
        "src_region_id":22,#danMark
        "cur_region_id":22, 
        "player_power_power_id":6,
        "player_power_player_id":6,
        "game_id": 1
    },
    
    { # unit in baye de holland
        "id":24,
        "type_unit_id":2, #bateau
        "src_region_id":32, #baye de holland
        "type_unit_id":2, #bateau
        "cur_region_id":32, 
        "player_power_power_id":6, #Ruuss
        "player_power_player_id":6,
        "game_id": 1
    }
]
