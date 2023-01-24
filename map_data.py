#Sheet1场景Sheet2房间
import pandas as pd
import player_data

position=[4,8]#对应excel4列8行
#房间相关在下面
"""
房间相当于绑定的只是功能函数，核心是功能函数而非其本身。
进入房间只需要传递地图名字和坐标就可以了。
"""
def room_function_1():
    print("@@@@@@debug_RoomFunction_Succeed@@@@@@21321321@")
def room_function_use():
    print("debug:function use is succeed!")
    print("@@@@@@debug_RoomFunction_Succeed@@@@@@21321321@")
def meet_room():
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
        room_code=input('输入q离开，输入功能ID进行使用:')
        if room_code=='q':
            player_data.player_data_global['is_in_room'] = False
        elif room_code in room_function_id:
            try:
                exec("room_function_"+str(room_code)+"()")#调用房间功能函数
            except:
                print('没有这个功能！')
        else:
            print("没有这个功能！")
            continue
            ###














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
