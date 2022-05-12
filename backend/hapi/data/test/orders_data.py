"""
Ordres des unités
"""
orders_attack=[
    #unite de munich attaque berlin
    {
        "id":1,
        "type_order_id": 1, #Attack
        "src_region_id":13, #berlin
        "dst_region_id" :43, #munich
        "unit_id":2,
        "num_tour" :0
    },

    # {
    #     "type_order_id": 1, #Attack
    #     "src_region_id":13, #berlin
    #     "dst_region_id" :58, #Silesia
    #     "unit_id":2,
    #     "num_tour" :0   ,

    # },
    
    {
        "id":2,
        "type_order_id": 1, #Attack
        "src_region_id":13, #berlin
        "dst_region_id" :48, #Paris
        "unit_id":2,
        "num_tour" :0   
    },

    #smyrna Attack brest
    {
        "id":3,
        "type_order_id": 1, #Attack
        "src_region_id":60,
        "dst_region_id" :16,
        "unit_id":9,
        "num_tour" :0   
    },
]
orders_convoi=[
    #unit in Agean sea convoy unit Smyrnat  which go in brest
    {
        "id":4,
        "type_order_id": 4, #convoy
        "src_region_id":5,
        "dst_region_id" :16,
        "unit_id":10,
        "other_unit_id":10,
        "num_tour" :0
    },
    #unit in ion Saea convoy unit Smyrnat which go in brest
    {
        "id":5,
        "type_order_id": 4, #convoy
        "src_region_id":34,
        "dst_region_id" :16,
        "unit_id":11,
        "other_unit_id":10,
        "num_tour" :0
    },
    #unit in Tyrrhenien Sea convoy unit Smyrnat which go in brest
    {
        "id":6,
        "type_order_id": 4,  # convoy
        "src_region_id": 69,
        "dst_region_id": 16,
        "unit_id": 12,
        "other_unit_id": 10,
        "num_tour" :0 
    },

    #unit in meditarrene convoy unit Smyrnat which go in brest
    {
        "id":7,
        "type_order_id": 4,  # convoy
        "src_region_id":75,
        "dst_region_id": 16,
        "unit_id": 7,
        "other_unit_id": 10, #unit present smyrna
        "num_tour" :0  
    },
    #unit in athlantic convoy unit Smyrnat which go in brest
    {
        "id":8,
        "type_order_id": 4,  # convoy
        "src_region_id" :45,
        "dst_region_id": 16,
        "unit_id": 13,
        "other_unit_id": 10, #unit present smyrna
         "num_tour" :0  
        
    },
]
orders_attack_float=[
     #fleet Athlantic Attack brest(cost) 
    {
        "id":9,
        "type_order_id": 1, #Attack
        "src_region_id":45,
        "dst_region_id" :16,
        "unit_id":13,
        "num_tour" :0   
    },
    #fleet Tyrrhenien Sea Attack ion Saea(maritime)
    {
        "id":10,
        "type_order_id": 1, #Attack
        "src_region_id":69,
        "dst_region_id" :34,
        "unit_id":13,
        "num_tour" :0   
    },
    #fleet brestAttack gaskony cotiére
    {
        "id":11,
        "type_order_id": 1, #Attack
        "src_region_id":16,
        "dst_region_id" :28,
        "unit_id":13,
        "num_tour" :0   
    },
    {
        "id":12,
        "type_order_id": 1, #Attack
        "src_region_id":16,
        "dst_region_id" :3,
        "unit_id":1,
        "num_tour" :1
    }, 
]
orders_soutient=[
    
    #fleet Tyrrhenien soutient défensive ion Saea(maritime)
    {
        "type_order_id": 3, #support
        "src_region_id":69,
        "dst_region_id" :34,
        "unit_id":13,
        "other_unit_id":11,
        "num_tour" :0
        
        
    },
    #smyrna soutient défensive  brest
    {
        "type_order_id": 3, #support
        "src_region_id":60,
        "dst_region_id" :16,
        "unit_id":9,
        "other_unit_id": 4,
        "num_tour" :0
    },
    #berlin soutient  défensif  #munish
    {
        "type_order_id": 3, #support
        "src_region_id":13, #berlin
        "dst_region_id" :43, #munish
        "unit_id":2,
        "other_unit_id": 3, 
        "num_tour" :0 
           
    }
]
orders_attack_mutuel=[
    #paris attaque breste 
    {
        "type_order_id": 1, #Attack
        "src_region_id":48, #Paris
        "unit_id":6,
        "dst_region_id" :16, 
        "num_tour" :0
    },
    #et brest Attaque Paris 
    {
        "type_order_id": 1, #Attack
        "src_region_id":16, #brest
        "unit_id":4,
        "dst_region_id" :48, #Paris 
        "num_tour" :0
    },
    
    #fleet in ageen sea attack fleet in  ionSea  
    {
        "type_order_id": 1, #Attack
        "src_region_id":5, # AAgean sea 
        "dst_region_id" :34, #Ion Sea 
        "unit_id":13,
        "num_tour" :0
    },
    # et fleet in ion sea attack fleet in Agean Sea 
    {
        "type_order_id": 1, #Attack
        "src_region_id":34,  #Ion Sea 
        "dst_region_id" :5,   #Agean sea 
        "unit_id":12,
        "num_tour" :0
    },
    
    # army in gascony  attack army  in Marseille
    {
        "type_order_id": 1, #Attack
        "src_region_id":28,  #Gascony
        "dst_region_id" :40,   #Marseillle
        "unit_id":7,
        "num_tour" :0
    },
    # army in  Marseille attack army  in gascony
    {
        "type_order_id": 1, #Attack
        "src_region_id":40,   #Marseillle
        "dst_region_id" :28,  #Gascony
        "unit_id":5,
        "num_tour" :0
    },  
]
orders_create_conflit=[ 
    #berlin et munich attaquent silésie 
    #berlin attaque silésie 
    {
        "type_order_id": 1, #Attack
        "src_region_id":13, #Berlin
        "unit_id":2,
        "dst_region_id" :58, #sliésie 
        "num_tour" :0
    },
    #munich attaque silésie
    {
        "type_order_id": 1, #Attack
        "src_region_id":43, #munich
        "unit_id":3,
        "dst_region_id" :58, #sliésie 
        "num_tour" :0
    },
    #paris et breste attaque picardie 
    #paris attaque picardie 
    {
        "type_order_id": 1, #Attack
        "src_region_id":48, # paris
        "unit_id":6,
        "dst_region_id" :49, #picardie
        "num_tour" :0
    },
    #brest attaque picardie 
    {
        "type_order_id": 1, #Attack
        "src_region_id":16, #brest
        "unit_id":4,
        "dst_region_id" :49, #picardie
        "num_tour" :0
    }   
]
orders_soutient_coupe=[
    #gascony qui est attaqué par marseille soutient brest
    {
        "type_order_id": 3, #support
        "src_region_id":28, 
        "dst_region_id" :16, #brest
        "unit_id":7,
        "other_unit_id":4,
        "num_tour" :0 
        
        
    },
    #  flleet Agean sea attaqué par fleet de ion Sea  support smyrna Army 
    {
        "type_order_id": 3, #support
        "src_region_id":5, #agenan ses 
        "dst_region_id" :60,
        "unit_id":11,
        "other_unit_id": 10,
        "num_tour" :0
      
        
    },
]
orders_soutient_attack_conflit=[

    #Belgique  soutient  Bress qui attaque picardie
    {
        "type_order_id": 3, #support
        "src_region_id":12, #Belgique
        "dst_region_id" :49, #picardie
        "unit_id":16,
        "other_unit_id": 4, 
        "num_tour" :0
           
    },
    #Bourgogne  soutient  Paris qui attaque la region picardie
    {
        "type_order_id": 3, #support
        "src_region_id":19, #Bourgogne
        "dst_region_id" :49, #picardie
        "unit_id":17,
        "other_unit_id": 6, 
        "num_tour" :0
           
    },
     #Prusse  soutient   Berlin  qui attaque silésie
    {
        "type_order_id": 3, #support
        "src_region_id":52, #Prusse
        "dst_region_id" :58, #silésie
        "unit_id":18,
        "other_unit_id": 2, 
        "num_tour" :0
           
    },
    #Boheme  soutient  Berlin  qui attaque silésie
    {
        "type_order_id": 3, #support
        "src_region_id":15, #Boheme
        "dst_region_id" :58, #silésie
        "unit_id":19,
        "other_unit_id":2, 
        "num_tour" :0
           
    },
     #Varsovie  soutient  munich  qui attaque silésie
    {
        "type_order_id": 3, #support
        "src_region_id":74, #varsovie
        "dst_region_id" :58, #silésie
        "unit_id":20,
        "other_unit_id": 3, 
        "num_tour" :0
           
    }
]
orders_add=[
    #unit in North sea convoy unit belgique  which go in  Norway 
    {
        "type_order_id": 4, #convoy
        "src_region_id":2, #Northe sea 
        "dst_region_id" :47,# Norway 
        "unit_id":21,
        "other_unit_id":16,
        "num_tour" :2
    },
    #unit in bay holland  attaque North sea
    {
        "type_order_id":1, #Attack
        "src_region_id":32, #bay holland
        "unit_id":24,
        "dst_region_id" :2, #North sea
        "num_tour" :2
    },
    #Londone soutient NRD
    {
        "type_order_id": 3, #support
        "src_region_id":39, #London
        "dst_region_id" :2, #NRD
        "unit_id":22,
        "other_unit_id": 21, 
        "num_tour" :2       
    }
]

orders_all = (
    orders_attack +
    orders_convoi +
    orders_attack_float +
    orders_soutient +
    orders_attack_mutuel +
    orders_create_conflit +
    orders_soutient_coupe +
    orders_soutient_attack_conflit +
    orders_add
)