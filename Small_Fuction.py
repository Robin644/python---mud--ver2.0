#存档功能的实现
#导入json函数
def dubup_21():
    import random
    import player_data
    player_point=0
    enemie_point=0
    game_turn=1
    counter=0
    cards={'p1':4,'p2':4,'p3':4,'p4':4,'p5':4,
          'p6':4,'p7':4,'p8':4,'p9':4,'p10':16}#每个点数一共四张,jqk看成10



    """
    a_1,a_2,..........a_13
    b
    c
    d
    """

    while True:
        try:
            player_xiazhu=int(input('请你下注。（按q，这是最后一次离开的机会！）:'))
        except:
            break
        if player_xiazhu<=player_data.player_data_global['player_money'] and player_xiazhu>0:
            print("【你已下注:"+str(player_xiazhu)+"元！】")

            print("**游戏开始！**")

            # 开局前抽牌
            #玩家
            while 1:
                counter=random.randint(1,10)
                if cards['p' + str(counter)] >0:
                    player_point+=counter
                    print("[第一回合：玩家抽到"+str(player_point)+"点]")
                    cards['p' + str(counter)]-=1
                    break
                else:
                    continue
            #庄家
            while 1:
                counter = random.randint(1, 10)
                if cards['p' + str(counter)] > 0:
                    cards['p' + str(counter)] -= 1
                    enemie_point+=counter
                    print("[庄家抽到" + str(counter) + "点]")
                    input()
                    game_turn+=1
                    break
                else:
                    continue

            while 0 <= player_point < 21 and 0 <= enemie_point < 21:#游戏进行时循环
                print("---------------------21点----------------")
                input()
                while player_point<17 and enemie_point<17:#未到17时游戏主循环

                    input("双方均未到17点，请继续下一回合要牌")
                    # 玩家抽牌循环
                    is_taken=False
                    while is_taken==False:
                        counter = random.randint(1, 10)
                        if cards['p' + str(counter)] > 0:
                            player_point += counter
                            print("[：玩家抽到" + str(counter) + "点]")
                            cards['p' + str(counter)] -= 1
                            is_taken=True
                            #若牌非空则游戏继续，不需要break
                        else:
                            continue#若牌空则继续抽牌
                    # 庄家
                    is_taken=False
                    while is_taken==False:
                        counter2 = random.randint(1, 10)
                        if cards['p' + str(counter2)] > 0:
                            cards['p' + str(counter2)] -= 1
                            enemie_point += counter2
                            game_turn+=1
                            is_taken=True
                            print("Game Turn:"+str(game_turn))
                            print("[庄家抽到" + str(counter2) + "点]")
                            print('\n【玩家总共：'+str(player_point)+'点】')
                            print('【庄家总共：' + str(enemie_point) + '点】')
                            input()
                            #若牌非空则游戏继续，不需要break
                        else:
                            continue
                    if enemie_point>=21 or player_point>=21:#进入结算
                        break
                if enemie_point>=17 and player_point>=17:#都到17
                    if enemie_point>=21 or player_point>=21:#进入结算
                        break
                    print("两方均到17点以上！玩家先手！")
                    player_c = input("1继续抽牌，2双倍下注(并抽牌)，3双倍下注(不抽牌)，4保留点:")
                    if player_c == '1':
                        while 1:
                            counter = random.randint(1, 10)
                            if cards['p' + str(counter)] > 0:
                                player_point += counter
                                print("[玩家抽到" + str(counter) + "点]")
                                print("玩家总共有" + str(player_point) + "points")
                                cards['p' + str(counter)] -= 1
                                break
                            else:
                                continue
                    elif player_c == '2':
                        print("玩家双倍下注并且抽牌！")
                        player_xiazhu *= 2
                        while 1:
                            counter = random.randint(1, 10)
                            if cards['p' + str(counter)] > 0:
                                player_point += counter
                                print("[玩家抽到" + str(counter) + "点]")
                                print("玩家总共有" + str(player_point) + "points")
                                cards['p' + str(counter)] -= 1
                                break
                            else:
                                continue
                    elif player_c == "3":
                        player_xiazhu *= 2
                        print("现在的押金是：" + str(player_xiazhu) + "元！")

                    else:
                        pass

                    print("庄家后手！")
                    input()
                    counter2 = str(random.randint(1, 2))
                    print(counter2)
                    if counter2 == '1':
                        while 1:
                            counter = random.randint(1, 10)
                            if cards['p' + str(counter)] > 0:
                                enemie_point += counter
                                print("[庄家抽到" + str(counter) + "点]")
                                print("庄家总共有" + str(enemie_point) + "points")
                                cards['p' + str(counter)] -= 1
                                break
                            else:
                                continue
                    elif counter2 == '2':
                        print("庄家保留牌！")

                        print("庄家总共有" + str(enemie_point) + "points")
                        input()
                    if (21 >= player_point > enemie_point > 17):
                        print("你的牌比庄家大！")
                        print("你赢了！你获得了" + str(player_xiazhu) + "元!")
                        player_data.player_data_global['player_dubuo_count']['赢'] += 1
                        player_data.player_data_global['player_money'] += player_xiazhu
                        player_data.player_data_global['player_dubuo_count']['净赚'] += player_xiazhu
                        input()
                        break
                    elif (21 >= enemie_point > player_point > 17):
                        print("你的牌比庄家小！")
                        print("你输了！你失去了" + str(player_xiazhu) + "元!")
                        player_data.player_data_global['player_dubuo_count']['输'] += 1
                        player_data.player_data_global['player_money'] -= player_xiazhu
                        player_data.player_data_global['player_dubuo_count']['净赚'] -= player_xiazhu
                        input()
                        break
                    else:
                        print('debug003,AI生成数字出错')
                        input()


                if player_point >= 17 and enemie_point<17:#玩家先到17以上
                    player_c=input("玩家先到17以上!\n1继续抽牌，2双倍下注(并抽牌)，3双倍下注(不抽牌)，4保留:")
                    if player_c=='1':
                        while 1:
                            counter = random.randint(1, 10)
                            if cards['p' + str(counter)] > 0:
                                player_point += counter
                                print("[玩家抽到" + str(counter) + "点]")
                                print("玩家总共有"+str(player_point)+"points")
                                cards['p' + str(counter)] -= 1
                                break
                            else:
                                continue
                        while 1:
                            counter = random.randint(1, 10)
                            if cards['p' + str(counter)] > 0:
                                enemie_point += counter
                                print("[庄家抽到" + str(counter) + "点]")
                                print("庄家总共有"+str(enemie_point)+"points")
                                cards['p' + str(counter)] -= 1
                                break
                            else:
                                continue
                    elif player_c=='2':
                        print("玩家双倍下注并且抽牌！")
                        player_xiazhu*=2
                        print("现在的押金是："+str(player_xiazhu)+"元！")
                        while 1:
                            counter = random.randint(1, 10)
                            if cards['p' + str(counter)] > 0:
                                player_point += counter
                                print("[玩家抽到" + str(counter) + "点]")
                                print("玩家总共有"+str(player_point)+"points")
                                cards['p' + str(counter)] -= 1
                                break
                            else:
                                continue
                        while 1:
                            counter = random.randint(1, 10)
                            if cards['p' + str(counter)] > 0:
                                enemie_point += counter
                                print("[庄家抽到" + str(counter) + "点]")
                                print("庄家总共有"+str(enemie_point)+"points")
                                cards['p' + str(counter)] -= 1
                                break
                            else:
                                continue




                    elif player_c=="3":
                        print("玩家双倍下注并且不抽牌！")
                        player_xiazhu*=2
                        print("现在的押金是：" + str(player_xiazhu) + "元！")
                        while 1:
                            counter = random.randint(1, 10)
                            if cards['p' + str(counter)] > 0:
                                enemie_point += counter
                                print("[庄家抽到" + str(counter) + "点]")
                                print("庄家总共有"+str(enemie_point)+"points")
                                cards['p' + str(counter)] -= 1
                                break
                            else:
                                continue
                        if (21 >= player_point > enemie_point > 17):
                            print("你的牌比庄家大！")
                            print("你赢了！你获得了" + str(player_xiazhu) + "元!")
                            player_data.player_data_global['player_dubuo_count']['赢'] += 1
                            player_data.player_data_global['player_money'] += player_xiazhu
                            player_data.player_data_global['player_dubuo_count']['净赚'] += player_xiazhu
                            input()
                            break
                        elif (21 >=enemie_point>player_point>17):
                            print("你的牌比庄家小！")
                            print("你输了！你失去了" + str(player_xiazhu) + "元!")
                            player_data.player_data_global['player_dubuo_count']['输'] += 1
                            player_data.player_data_global['player_money'] -= player_xiazhu
                            player_data.player_data_global['player_dubuo_count']['净赚'] -= player_xiazhu
                            input()
                            break



                    else:
                        print("玩家不抽牌！")
                        while 1:
                            counter = random.randint(1, 10)
                            if cards['p' + str(counter)] > 0:
                                enemie_point += counter
                                print("[庄家抽到" + str(counter) + "点]")
                                print("庄家总共有"+str(enemie_point)+"points")
                                cards['p' + str(counter)] -= 1
                                break
                            else:
                                continue
                        if (21 >= player_point > enemie_point > 17):
                            print("你的牌比庄家大！")
                            print("你赢了！你获得了" + str(player_xiazhu) + "元!")
                            player_data.player_data_global['player_dubuo_count']['赢'] += 1
                            player_data.player_data_global['player_money'] += player_xiazhu
                            player_data.player_data_global['player_dubuo_count']['净赚'] += player_xiazhu
                            input()
                            break
                        elif (21 >=enemie_point>player_point>17):
                            print("你的牌比庄家小！")
                            print("你输了！你失去了" + str(player_xiazhu) + "元!")
                            player_data.player_data_global['player_dubuo_count']['输'] += 1
                            player_data.player_data_global['player_money'] -= player_xiazhu
                            player_data.player_data_global['player_dubuo_count']['净赚'] -= player_xiazhu
                            input()
                            break
                    continue


                if 21>enemie_point >= 17 and player_point<17:#庄家先到17以上
                    print("【庄家先到17点以上！】")
                    counter2 = str(random.randint(1, 2))
                    print(counter2)
                    if counter2 == '1':
                        print("【庄家选择继续抽牌！】")
                        while 1:
                            counter = random.randint(1, 10)
                            if cards['p' + str(counter)] > 0:
                                enemie_point += counter
                                print("[庄家抽到" + str(counter) + "点]")
                                print("庄家总共有" + str(enemie_point) + "points")
                                cards['p' + str(counter)] -= 1
                                break
                            else:
                                continue
                    elif counter2 == '2':
                        print("庄家保留牌！")

                        print("庄家总共有" + str(enemie_point) + "points")
                        input()
                        while 1:
                            counter = random.randint(1, 10)
                            if cards['p' + str(counter)] > 0:
                                player_point += counter
                                print("[玩家抽到" + str(counter) + "点]")
                                print("玩家总共有"+str(player_point)+"points")
                                cards['p' + str(counter)] -= 1
                                break
                            else:
                                continue
                    elif counter2=='2':
                        print("庄家保留牌！")
                        while 1:
                            counter = random.randint(1, 10)
                            if cards['p' + str(counter)] > 0:
                                player_point += counter
                                print("[玩家抽到" + str(counter) + "点]")
                                print("玩家总共有"+str(player_point)+"points")
                                cards['p' + str(counter)] -= 1
                                break
                            else:
                                continue

                        input()


                    else:
                        pass
                else:
                    continue
            print("------------------------------------------")

                   #结算

            if enemie_point >21 and player_point>21:
                print("双方均失败！本回合打平！")
                input()
                break
            if player_point>21 or enemie_point==21:
                print("你输了！你失去了"+str(player_xiazhu)+"元!")
                player_data.player_data_global['player_dubuo_count']['输']+=1
                player_data.player_data_global['player_money'] -= player_xiazhu
                player_data.player_data_global['player_dubuo_count']['净赚']-=player_xiazhu
                input()
                break
            if player_point==21 or enemie_point>21:
                print("你赢了！你获得了"+str(player_xiazhu)+"元!")
                player_data.player_data_global['player_dubuo_count']['赢']+=1
                player_data.player_data_global['player_money'] += player_xiazhu
                player_data.player_data_global['player_dubuo_count']['净赚'] += player_xiazhu
                input()
                break





            #break
            else:
                continue












def Check_self():
    import player_data
    while True:
        print("^^^^^^^^^^^^^^^^^^查看角色^^^^^^^^^^^^^^^^^^")
        check_code=input("|q退出|a查看属性|b查看背包|||:")
        if check_code=='q':
            break
        elif check_code=='a':
            print("|属性|"+str(player_data.player_data_global['player_shuxing']).replace("'",""))
            print('|金钱|'+str(player_data.player_data_global['player_money'])+'元')
            print("|移动速度|"+str(player_data.player_data_global['player_move_speed'])+"分/格")
            print("|赌博成就|："+str(player_data.player_data_global['player_dubuo_count']))
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

def cundang():
    import json
    import map_data,player_data,world_data
    print("-"*30)
    print("存                           档")
    file_name="save_data.json"
    code=input("存档会删除以前的存档，确定要存档吗？(0/1)")
    if code=="0":
        print("取消存档~~")
    elif code=="1":


#保存内容

        nr=[map_data.position,world_data.Time,player_data.player_data_global]

        print("debug_MESSAGE:"+str(nr)+"\n")
        with open(file_name,"w") as file:
            file.write("")
            print("*旧存档已清除")
        with open(file_name,"a") as file_object:


            json.dump(nr,file_object)
            print("\n\n存档成功！数据已保存！！")


import pandas as pd
import numpy as np

def get_coordinates(data: pd.DataFrame, target: str):#查找数据在表中位置

    """
    根据要查找的目标，返回其在Head=None中的Pandas数据的位置
    data: excel数据,
    target: 要查找的目标
    return: 返回坐标列表
    """
    data_list = np.array(data).tolist()
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            if data_list[i][j] == target:
                return [i , j ]#行，列
    return ['找不到']
#data = pd.read_excel('all_npc.xlsx',sheet_name='名称',header=None)
#print(get_coordinates(data,"npc模板1"))
def dudang():
    import json
    print("-"*30)
    print("读                           档")
    file_name="save_data.json"
    #try:
    with open(file_name) as f:
        nr=json.load(f)
        print(nr)
        print("\n\n读档成功！数据已读取！！")

        print("\n拼命恢复数据中。。。\n")

        #print("MESSAGE:"+str(nr))
        return nr
        #.player_name, sjk.player_weapon_bag, sjk.player_mission_id, sjk.player_wearing_skill, sjk.player_completed_mission_id, sjk.player_things_bag, sjk.player_describe_bag, sjk.player_face, sjk.player_skill0, sjk.player_skill1, sjk.player_skill0_level, sjk.player_skill1_level, sjk.player_wearing_skill, sjk.player_wearing_wear, sjk.player_wearing_weapon, sjk.player_wear_bag, sjk.player_sx0, sjk.player_sx1, sjk.player_sx2=nr
    #except:
        """
        import map_data, player_data, world_data
        print("警告：未发现存档数据\n强制存档中。。。")
        nr = [map_data.position,world_data.Time,player_data.player_data_global]
        #print("MESSAGE:" + str(nr) + "\n")
        with open(file_name, "w") as file:
            file.write("")
            print("旧存档已清除")
        with open(file_name, "a") as file_object:

            json.dump(nr, file_object)
            print("\n\n强制存档成功！数据已保存！！")
            dudang()
            """