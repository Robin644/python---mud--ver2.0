#Sheet1场景Sheet2房间
import pandas as pd
import player_data

position=[4,8]#对应excel4列8行
#地图打印相关函数
def confirm_scene_imformation_npc():#打印场景npc信息的函数
    import player_data
    position = player_data.player_data_global['player_position']
    npc_name_list = list(str(pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='场景npc', header=None).values[
        position[1], position[0]]).split(','))
    npc_print_list=[]
    # debug:print(npc_name_list)
    for items in npc_name_list:
        if str(items) != "nan":  # 看看有没有npc
            npc_print_list.append(items)
    if npc_print_list!=[]:
        print("|*这里有Npc|"+str(npc_print_list).replace("'","")+"|")
    else:
        print("|这里没有NPC~|")



def confirm_scene_imformation_items():#打印场景道具信息的函数
    import player_data
    position = player_data.player_data_global['player_position']
    npc_name_list = list(str(pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='场景物品', header=None).values[
        position[1], position[0]]).split(','))
    npc_print_list=[]
    # debug:print(npc_name_list)
    for items in npc_name_list:
        if str(items) != "nan":  # 看看有没有npc
            npc_print_list.append(items)
    if npc_print_list!=[]:
        print("|*这里有物品|"+str(npc_print_list).replace("'","")+"|")
    else:
        print("|这里没有物品~|")
def confirm_scene_imformation_equipments():#打印场景装备信息的函数
    import player_data
    position = player_data.player_data_global['player_position']
    npc_name_list = list(str(pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='场景装备', header=None).values[
        position[1], position[0]]).split(','))
    npc_print_list=[]
    # debug:print(npc_name_list)
    for items in npc_name_list:
        if str(items) != "nan":  # 看看有没有npc
            npc_print_list.append(items)
    if npc_print_list!=[]:
        print("|*这里有@装备@|"+str(npc_print_list).replace("'","")+"|")
    else:
        print("|这里没有装备~|")





def confirm_room_imformation_npc():#打印场景npc信息的函数
    import player_data
    position = player_data.player_data_global['player_position']
    npc_name_list = list(str(pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='房间npc', header=None).values[
        position[1], position[0]]).split(','))
    npc_print_list=[]
    # debug:print(npc_name_list)
    for items in npc_name_list:
        if str(items) != "nan":  # 看看有没有npc
            npc_print_list.append(items)
    if npc_print_list!=[]:
        print("|*房间里有Npc|"+str(npc_print_list).replace("'","")+"|")
    else:
        print("|房间里没有NPC~|")
def confirm_room_imformation_items():#打印房间物品信息的函数
    import player_data
    position = player_data.player_data_global['player_position']
    npc_name_list = list(str(pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='房间物品', header=None).values[
        position[1], position[0]]).split(','))
    npc_print_list=[]
    # debug:print(npc_name_list)
    for items in npc_name_list:
        if str(items) != "nan":  # 看看有没有npc
            npc_print_list.append(items)
    if npc_print_list!=[]:
        print("|*房间里有物品：|"+str(npc_print_list).replace("'","")+"|")
    else:
        print("|房间里没有物品~|")
def confirm_room_imformation_equipments():#打印房间信息的函数
    import player_data
    position = player_data.player_data_global['player_position']
    npc_name_list = list(str(pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='房间装备', header=None).values[
        position[1], position[0]]).split(','))
    npc_print_list=[]
    # debug:print(npc_name_list)
    for items in npc_name_list:
        if str(items) != "nan":  # 看看有没有npc
            npc_print_list.append(items)
    if npc_print_list!=[]:
        print("|*房间里有装备：|"+str(npc_print_list).replace("'","")+"|")
    else:
        print("|房间里没有装备~|")









#房间相关在下面
"""
房间相当于绑定的只是功能函数，核心是功能函数而非其本身。
进入房间只需要传递地图名字和坐标就可以了。
"""
def room_function_1():
    print("你上了个厕所，花了10元。")
    import player_data
    player_data.player_data_global['player_money']-=10
def room_function_tao():
    print("你扫了个厕所，赚了114514元。")
    import player_data
    player_data.player_data_global['player_money']+=114514
def room_function_dubuo():
    import Small_Fuction
    dubuo_class=input("q退出，a二十一点")
    if dubuo_class=='a':
        Small_Fuction.dubup_21()
    elif dubuo_class=='q':
        print("还是不赌博了~")

def room_function_buy1():#赌场超市
    print("debug:function use is succeed!")
    print("@@@@@@debug_RoomFunction_Succeed@@@@@@21321321@")





def meet_npc(npc_name):#npc互动
    import player_data
    import Small_Fuction

    npc_in_list_position=Small_Fuction.get_coordinates(pd.read_excel('all_npc.xlsx',sheet_name='名称',header=None),npc_name)#[0]行[1]列
    #print(npc_in_list_position)
    if npc_in_list_position[0]=="找不到":
        print("|这里没有这个人啊？|")
        return ValueError
    else:
        #print(pd.read_excel('all_npc.xlsx', sheet_name='描述'))
        npc_describe = pd.read_excel('all_npc.xlsx', sheet_name='描述',header=None).values[
        npc_in_list_position[0], npc_in_list_position[1]]
        npc_function_id = list(str(pd.read_excel('all_npc.xlsx', sheet_name='功能ID',header=None).values[
        npc_in_list_position[0], npc_in_list_position[1]]).split(","))
        try:
            npc_data_dict = eval(str(pd.read_excel('all_npc.xlsx', sheet_name='属性',header=None).values[npc_in_list_position[0], npc_in_list_position[1]]))
        except:
            npc_data_dict={"无":"无"}
        #print(npc_data_dict)
        #print(pd.read_excel('all_npc.xlsx', sheet_name='描述',header=None))
        #print(npc_function_id)
    #debug:print(room_function_id)
    if str(npc_name)!="nan":#看看是不是空
        player_data.player_data_global['player_is_talking'] = True
    else:
        print("——这里哪有人？")
    while player_data.player_data_global['player_is_talking'] == True:
        print("|————————————NPC："+str(npc_name)+"——————————————————|")
        print('|描述:'+str(npc_describe)+"|")
        print('|属性:' + str(npc_data_dict)+"|")
        #confirm_room_imformation_npc()
        room_code=input('输入q离开，输入功能ID进行Npc互动:')
        print(npc_function_id)
        if room_code=='q':
            player_data.player_data_global['player_is_talking'] = False
        elif room_code in npc_function_id:
            try:
                send_data=[npc_name]#封装
                import npc_function
                eval("npc_function.npc_function_"+str(room_code)+"("+str(send_data)+")")#调用npc功能函数
            except:
                print('没有这个功能！')
        else:
            print("没有这个功能！")
            continue
            ###

#debug:meet_npc("npc模板1")



def meet_room():#进房间
    import player_data
    position=player_data.player_data_global['player_position']
    room_name = pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='房间', header=None).values[
        position[1], position[0]]

    room_describe = pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='房间描述', header=None).values[
        position[1], position[0]]
    room_function_id = list(str(pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='房间功能ID', header=None).values[
        position[1], position[0]]).split(","))
    #debug:print(room_function_id)

    if str(room_name)!="nan":#看看是不是空房间
        player_data.player_data_global['is_in_room'] = True
    else:
        print("——这里哪有房间？")
    while player_data.player_data_global['is_in_room']==True:
        print("————————————房间："+str(room_name)+"——————————————————")
        print('描述:'+str(room_describe))
        confirm_room_imformation_npc()
        confirm_room_imformation_equipments()
        confirm_room_imformation_items()
        room_code=input('输入q离开，输入功能ID进行房间功能使用,输入npc进行互动:')
        if room_code=='q':
            player_data.player_data_global['is_in_room'] = False
        elif room_code in room_function_id:
            try:
                exec("room_function_"+str(room_code)+"()")#调用房间功能函数
            except:
                print('没有这个功能！')
        elif room_code=='npc':

            npc_name = input("|你要跟谁互动？(输入名字)|:")
            meet_npc(npc_name)
        else:
            print("没有这个功能！")
            continue
            ###




##场景进入条件ID功能函数
def scene_condition_0():#0是无条件捏
   return True
def scene_condition_1():
    if player_data.player_data_global['player_is_admin']==True:
        return True
    else:
        print("*你没有资格进入此场景！*这个场景只有开发者可以进入!")
        return False
def scene_condition_2():#赌场
    if player_data.player_data_global['player_money']>=1000:
        return True
    else:
        print("*你没有资格进入此场景！*这个场景只有1000以上现金才可以进入!")
        return False
#exec ("print('sss')")
"""
print(scene_condition_0())
exec("a=scene_condition_0()")
print(a)"""


















def confirm_map_imformation(position):#打印位置函数
    import player_data
    position=player_data.player_data_global['player_position']
    print("目前位置坐标:列X:"+str(position[0])+'|行Y:'+str(position[1]))
    scene=pd.read_excel(player_data.player_data_global['player_Map_name'],sheet_name='场景',header=None).values[position[1],position[0]]#y坐标代表行，x代表列，读取行/列
    print("**********\n你现在位于场景:|" + str(scene)+"|")#nan=None
    if str(scene)== 'nan':
        print('（你好像掉进虚空了？？debug启动）')
        print(pd.read_excel(player_data.player_data_global['player_Map_name'],sheet_name='场景',header=None))
    try:
        describe = pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='描述',header=None).values[position[1],position[0]]
        print("**********\n|场景描述:" +str(describe)+"|")
    except:
        print("|**********\nOvO该场景没有描述~|")
    try:
        room = pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='房间',header=None).values[position[1],position[0]]
        if str(room)!='nan':
            print("**********\n|包含房间:" +str(room)+"|")
        else:
            print("**********\n|该场景没有房间~|")
    except:
        print("**********\n|该场景没有房间~|")
def confirm_map_imformation2(position2):
    import player_data
    scene1 = str(pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='场景', header=None).values[position2[1], position2[0]])
    return scene1
#print(confirm_map_imformation2([2,8]))




#print("debug:"+pd.read_excel('Map.xlsx',header=None, sheet_name='场景').values[19,8])
#confirm_map_imformation([19,8])
