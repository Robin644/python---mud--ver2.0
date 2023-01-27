import map_data
import player_data
import world_data
import Small_Function
while player_data.player_data_global['player_condition']=='alive':
    print('\n\n')
    print("&^" * 20)  # start
    world_data.Time_check(world_data.Time)
    print("|现在的时间是：|" + str(world_data.Time[0]) + "天 | " + str(world_data.Time[1]) + "时 | " + str(
        world_data.Time[2]) + "分 | ")


    map_data.confirm_map_imformation(player_data.player_data_global['player_position'])#打印位置信息
    map_data.confirm_scene_imformation_npc()#打印npc信息
    map_data.confirm_scene_imformation_items()
    map_data.confirm_scene_imformation_equipment()


    #调试模式提示
    if player_data.player_data_global['player_is_admin']==True:
        print("*******开发者模式启用中！******")
        print("隐藏指令：自杀：suicide|调出控制台：cheat")


    inputcode=input("CODE:|map|move|save|room|npc|C(查看自己)|:  ")
    print("&^" * 20)  # start
    def Player_move():#移动相关功能在这
        import pandas as pd
        move_code=input("输入N，S，W，E来移动:")
        test_position=player_data.player_data_global['player_position']



        if move_code=='N':
            test_position=[player_data.player_data_global['player_position'][0],player_data.player_data_global['player_position'][1]-1]#往北excel读取的行数-1
            try:

                scene_condition_id = list(str(
                    pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='场景条件ID',
                                  header=None).values[
                        test_position[1], test_position[0]]).split(","))  # 判断是否满足所有进入场景的条件
                #print(str(scene_condition_id) + "|debug2132132132131")
            except:
                #print(str(scene_condition_id) + "|debug2132132132131")
                scene_condition_id = [0]
            result_list = []
            a = None

            for ids in scene_condition_id:#找所有的条件ID
                # try:scene_condition_1()
                try:
                    a = eval("map_data.scene_condition_" + str(ids) + "()")
                except:
                    a=eval("map_data.scene_condition_0()")#出bug或无条件则放行

                result_list.append(a)  # a在exec已经赋值。
                # except:
                #   pass
                """
            print(result_list)
            print(scene_condition_id)
            print(ids)
            print(a)
            """
            if False in result_list:
                result_ = False
            else:
                result_ = True
            if map_data.confirm_map_imformation2(test_position) != 'nan' and result_==True:
                print("*你花费["+str(player_data.player_data_global['player_move_speed'])+"]分钟来到了|"+map_data.confirm_map_imformation2(test_position)+"|")
                world_data.Time[2]+=player_data.player_data_global['player_move_speed']
                return test_position#返回变化值
            else:
                print("\n你滴|北|边没有路了！看看地图吧！\n")
                return player_data.player_data_global['player_position']#走不了，返回原来值

        elif move_code == 'S':
            test_position = [player_data.player_data_global['player_position'][0], player_data.player_data_global['player_position'][1] + 1]  # 往南excel读取的行数+1
            try:

                scene_condition_id = list(str(
                    pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='场景条件ID',
                                  header=None).values[
                        test_position[1], test_position[0]]).split(","))  # 判断是否满足所有进入场景的条件
                #print(str(scene_condition_id) + "|debug2132132132131")
            except:
                #print(str(scene_condition_id) + "|debug2132132132131")
                scene_condition_id = [0]
            result_list = []
            a = None

            for ids in scene_condition_id:
                # try:scene_condition_1()
                try:
                    a = eval("map_data.scene_condition_" + str(ids) + "()")
                except:
                    a = eval("map_data.scene_condition_0()")  #出bug或无条件则放行  # a在exec已经赋值。
                # except:
                #   pass
                result_list.append(a)
                """
            print(result_list)
            print(scene_condition_id)
            print(ids)
            print(a)
            """
            #print(result_list)
            if False in result_list:
                result_ = False
            else:
                result_ = True
            if map_data.confirm_map_imformation2(test_position) != 'nan'and result_==True:
                print("*你花费[" + str(player_data.player_data_global['player_move_speed']) + "]分钟来到了|" + map_data.confirm_map_imformation2(
                    test_position) + "|")
                world_data.Time[2] += player_data.player_data_global['player_move_speed']
                return test_position  # 返回变化值
            else:
                print("\n你滴|南|边没有路了！看看地图吧！\n")
                return player_data.player_data_global['player_position']  # 走不了，返回原来值
        elif move_code == 'W':
            test_position = [player_data.player_data_global['player_position'][0]-1, player_data.player_data_global['player_position'][1]]  # 往西excel读取的列数-1
            try:

                scene_condition_id = list(str(
                    pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='场景条件ID',
                                  header=None).values[
                        test_position[1], test_position[0]]).split(","))  # 判断是否满足所有进入场景的条件
                #print(str(scene_condition_id) + "|debug2132132132131")
            except:
                #print(str(scene_condition_id) + "|debug2132132132131")
                scene_condition_id = [0]
            result_list = []
            a = None

            for ids in scene_condition_id:
                # try:scene_condition_1()
                try:
                    a = eval("map_data.scene_condition_" + str(ids) + "()")
                except:
                    a = eval("map_data.scene_condition_0()")  #出bug或无条件则放行  # a在exec已经赋值。
                # except:
                #   pass
                result_list.append(a)
                """
            print(result_list)
            print(scene_condition_id)
            print(ids)
            print(a)
            """
            if False in result_list:
                result_ = False
            else:
                result_ = True
            if map_data.confirm_map_imformation2(test_position) != 'nan'and result_==True:
                print("*你花费[" + str(player_data.player_data_global['player_move_speed']) + "]分钟来到了|" + map_data.confirm_map_imformation2(
                    test_position) + "|")
                world_data.Time[2] += player_data.player_data_global['player_move_speed']
                return test_position  # 返回变化值
            else:
                print("\n你滴|西|边没有路了！看看地图吧！\n")
                return player_data.player_data_global['player_position']  # 走不了，返回原来值
        elif move_code == 'E':
            test_position = [player_data.player_data_global['player_position'][0]+1, player_data.player_data_global['player_position'][1]]  # 往东excel读取的列数+1
            try:

                scene_condition_id = list(str(
                    pd.read_excel(player_data.player_data_global['player_Map_name'], sheet_name='场景条件ID',
                                  header=None).values[
                        test_position[1], test_position[0]]).split(","))  # 判断是否满足所有进入场景的条件
                #print(str(scene_condition_id) + "|debug2132132132131")
            except:
                #print(str(scene_condition_id) + "|debug2132132132131")
                scene_condition_id = [0]
            result_list = []
            a = None

            for ids in scene_condition_id:
                # try:scene_condition_1()
                try:
                    a = eval("map_data.scene_condition_" + str(ids) + "()")
                except:
                    a = eval("map_data.scene_condition_0()")  #出bug或无条件则放行# a在exec已经赋值。
                # except:
                #   pass
                result_list.append(a)
                """
            print(result_list)
            print(scene_condition_id)
            print(ids)
            print(a)
            """
            if False in result_list:
                result_ = False
            else:
                result_ = True
            if map_data.confirm_map_imformation2(test_position) != 'nan'and result_==True:
                print("*你花费[" + str(player_data.player_data_global['player_move_speed'])+"]分钟来到了|" + map_data.confirm_map_imformation2(
                    test_position) + "|")
                world_data.Time[2] += player_data.player_data_global['player_move_speed']
                return test_position  # 返回变化值
            else:
                print("\n你滴|东|边没有路了！看看地图吧！\n")
                return player_data.player_data_global['player_position']  # 走不了，返回原来值
        else:
            print("******\ndebug1\n******")
            pass#




    if inputcode=='map':
        import pandas as pd
        import numpy
        pd.set_option('display.colheader_justify', 'center')
        pd.set_option('display.max_columns', 2000)
        pd.set_option('display.width', 2000)
        pd.set_option('display.max_colwidth', 2000)
        pd.set_option('display.unicode.ambiguous_as_wide', True)
        pd.set_option('display.unicode.east_asian_width', True)
        #tem_p=[player_data.player_data_global["player_position"][1],player_data.player_data_global["player_position"][0]]
        #original_name=str(pd.read_excel(player_data.player_data_global['player_Map_name'],header=None,sheet_name='场景').values[player_data.player_data_global["player_position"][1],player_data.player_data_global["player_position"][0]])
       # print("xadwdw1223"+original_name)#
        #print(pd.read_excel(player_data.player_data_global['player_Map_name'], header=None, sheet_name='场景').values[player_data.player_data_global["player_position"][1],player_data.player_data_global["player_position"][0]]='(你在这)')
        #print(pd.read_excel(player_data.player_data_global['player_Map_name'], header=None, sheet_name='场景').loc[player_data.player_data_global["player_position"][1],player_data.player_data_global["player_position"][0]])

        #print(pd.read_excel(player_data.player_data_global['player_Map_name'], header=None, sheet_name='场景').values[player_data.player_data_global["player_position"][1],player_data.player_data_global["player_position"][0]])
        print(str(pd.read_excel(player_data.player_data_global['player_Map_name'],header=None,sheet_name='场景')).replace('NaN','   '))
        ##
        #pd.read_excel(player_data.player_data_global['player_Map_name'], header=None, sheet_name='场景').loc[
           # player_data.player_data_global["player_position"][1], player_data.player_data_global["player_position"][
              #  0]] = original_name
    if inputcode=="C":
        Small_Function.Check_self()
    if inputcode=="move":
        player_data.player_data_global['player_position']=Player_move()
    if inputcode=="room":
        map_data.meet_room()
    if inputcode=='npc':
        npc_name=input("|你要跟谁互动？(输入名字)|:")
        map_data.meet_npc(npc_name)
    if inputcode=='save':#存档相关功能在这
        print("——存档读档——")
        print("--------------游戏数据系统------------------")
        code = input("输入0退出，输入1存档，输入2读档")
        if code == "0":
            print('-取消存档-')
            pass
        elif code == "1":
            Small_Function.cundang()
        elif code == "2":
            ####################################
             map_data.position,world_data.Time,player_data.player_data_global= Small_Function.dudang()[0], Small_Function.dudang()[1], Small_Function.dudang()[2]
            ######AA##############################
        print("\n" + "-" * 30)##





     #以下是调试指令，玩家看不见需要在数据里把“开发者模式”改成True才能显示
    if inputcode=='suicide' and player_data.player_data_global['player_is_admin']==True:
        player_data.player_data_global['player_condition']='dead'
    if inputcode == 'cheat' and player_data.player_data_global['player_is_admin'] == True:
        print("请输入作弊功能1:执行代码段,2:,3:：")
        cheat_code=input(": ")
        if cheat_code=='1':
            admin_code=str(input("|请输入要执行的代码|\n"))
            try:
                print("-------------运行结果——————————————")
                exec(admin_code)
                print("-------------——————————————————————")
                print("Succeed.")
            except:
                print("执行失败。")







    #指令输入后执行以下句段









    print("&^" * 20)#end
    #made By Robin!

