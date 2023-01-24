import map_data
import player_data
import world_data
import Small_Fuction
while player_data.player_data_global['player_condition']=='alive':

    print("&^" * 20)  # start
    map_data.confirm_map_imformation(player_data.player_data_global['player_position'])#打印位置信息
    #调试模式提示
    if player_data.player_data_global['player_is_admin']==True:
        print("*******开发者模式启用中！******")
        print("隐藏指令：自杀：suicide|调出控制台：cheat")


    inputcode=input("CODE:|move|save|room|:  ")
    print("&^" * 20)  # start
    def Player_move():#移动相关功能在这
        move_code=input("输入N，S，W，E来移动:")
        test_position=player_data.player_data_global['player_position']
        if move_code=='N':
            test_position=[player_data.player_data_global['player_position'][0],player_data.player_data_global['player_position'][1]-1]#往北excel读取的行数-1
            if map_data.confirm_map_imformation2(test_position) != 'nan':
                print("*你花费["+str(player_data.player_data_global['player_move_speed'])+"]分钟来到了|"+map_data.confirm_map_imformation2(test_position)+"|")
                world_data.Time[2]+=player_data.player_data_global['player_move_speed']
                return test_position#返回变化值
            else:
                print("\n你滴|北|边没有路了！看看地图吧！\n")
                return player_data.player_data_global['player_position']#走不了，返回原来值

        elif move_code == 'S':
            test_position = [player_data.player_data_global['player_position'][0], player_data.player_data_global['player_position'][1] + 1]  # 往南excel读取的行数+1
            if map_data.confirm_map_imformation2(test_position) != 'nan':
                print("*你花费[" + str(player_data.player_data_global['player_move_speed']) + "]分钟来到了|" + map_data.confirm_map_imformation2(
                    test_position) + "|")
                world_data.Time[2] += player_data.player_data_global['player_move_speed']
                return test_position  # 返回变化值
            else:
                print("\n你滴|南|边没有路了！看看地图吧！\n")
                return player_data.player_data_global['player_position']  # 走不了，返回原来值
        elif move_code == 'W':
            test_position = [player_data.player_data_global['player_position'][0]-1, player_data.player_data_global['player_position'][1]]  # 往西excel读取的列数-1
            if map_data.confirm_map_imformation2(test_position) != 'nan':
                print("*你花费[" + str(player_data.player_data_global['player_move_speed']) + "]分钟来到了|" + map_data.confirm_map_imformation2(
                    test_position) + "|")
                world_data.Time[2] += player_data.player_data_global['player_move_speed']
                return test_position  # 返回变化值
            else:
                print("\n你滴|西|边没有路了！看看地图吧！\n")
                return player_data.player_data_global['player_position']  # 走不了，返回原来值
        elif move_code == 'E':
            test_position = [player_data.player_data_global['player_position'][0]+1, player_data.player_data_global['player_position'][1]]  # 往东excel读取的列数+1
            if map_data.confirm_map_imformation2(test_position) != 'nan':
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

    if inputcode=="move":
        player_data.player_data_global['player_position']=Player_move()
    if inputcode=="room":
        map_data.meet_room()
    if inputcode=='save':#存档相关功能在这
        print("——存档读档——")
        print("--------------游戏数据系统------------------")
        code = input("输入0退出，输入1存档，输入2读档")
        if code == "0":
            print('-取消存档-')
            pass
        elif code == "1":
            Small_Fuction.cundang()
        elif code == "2":
            ####################################
             map_data.position,world_data.Time,player_data.player_data_global= Small_Fuction.dudang()[0],Small_Fuction.dudang()[1],Small_Fuction.dudang()[2]
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







    #指令输入后执行以下句段,(动态时间系统)

    world_data.Time_check(world_data.Time)
    print("现在的时间是："+str(world_data.Time[0])+"天 | "+str(world_data.Time[1])+"时 | "+str(world_data.Time[2])+"分 | ")







    print("&^" * 20)#end
    #made By Robin!

