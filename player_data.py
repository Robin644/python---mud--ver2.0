player_position=[4,9]#x,y
player_Map_name='map.xlsx'
player_move_speed=5#移动一格需要的分
player_condition="alive"#dead
player_is_admin=False#开发者模式
player_money=114
player_shuxing={'力量':0,'敏捷':0,'智力':0,"气运":100,'防御':0}
player_dubuo_count={}
player_bag=[]
player_equipment={}
player_is_talking=False
#下面是保存的数据
player_data_global={'player_position':[4,8],'player_Map_name':'map.xlsx','player_move_speed':2,
                    'player_condition':'alive','is_in_room':False,'player_is_admin':True,
                    "player_money":1145,
                    "player_bag":[],
                    'player_shuxing':{'力量':0,'敏捷':0,'智力':0,'气运':100,'防御':0},
                    'player_dubuo_count':{'赢':0,'输':0,"净赚":0},
                    'player_is_talking':False,
                    'player_equipment':{"player_equipment_body":None,"player_equipment_L_hand":None,
                  "player_equipment_R_hand":None,"player_equipment_L_feet":None,"player_equipment_R_feet":None,
                  "player_equipment_fingers":[],"player_equipment_else":[]

                                        }


                    }#存档读档都用这个