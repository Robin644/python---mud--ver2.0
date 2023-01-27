
#战斗最多支持1v1,伪nvn模式，即可以发动队友的技能?
def battle(F_name_list:list,E_name_list:list):#class:玩家与npc冲突b:npc冲突
    import pandas as pd
    import Small_Function as SF
    import random
    import player_data
    import skillFunction
    #list第一个就是战斗人员。
    F_attacker_name=F_name_list[0]
    F_attacker_buff=[]
    E_attacker_name=E_name_list[0]
    E_attacker_buff=[]
    #属性赋值
    #友方
    if F_attacker_name =="player":

        F_attacker_shuxing=player_data.player_data_global["player_shuxing"]
        F_attacker_skill=player_data.player_data_global["player_skill"]
    else:#若是npc打架

        data = pd.read_excel('all_npc.xlsx', sheet_name='名称', header=None)
        position=SF.get_coordinates(data,F_attacker_name)
        F_attacker_shuxing=eval(pd.read_excel('all_npc.xlsx', sheet_name='属性', header=None).values[position[0],position[1]])
        F_attacker_skill=eval(pd.read_excel('all_npc.xlsx', sheet_name='技能', header=None).values[position[0],position[1]])
        #print(F_attacker_shuxing)
    #敌人
    if E_attacker_name =="player":#若玩家是敌人

        E_attacker_skill=player_data.player_data_global["player_skill"]
        E_attacker_shuxing=player_data.player_data_global["player_shuxing"]
    else:#若npc是敌人


        data = pd.read_excel('all_npc.xlsx', sheet_name='名称', header=None)
        position=SF.get_coordinates(data,E_attacker_name)
        #print(position)
        E_attacker_shuxing=eval(pd.read_excel('all_npc.xlsx', sheet_name='属性', header=None).values[position[0],position[1]])
        E_attacker_skill=eval(pd.read_excel('all_npc.xlsx', sheet_name='技能', header=None).values[position[0],position[1]])

        #print(F_attacker_shuxing)
    turn=0
    print("【"+F_attacker_name+"】 大叫一声：“领教阁下高招！”，向 【"+E_attacker_name+"】 发起了战斗！")
    while len(F_name_list) !=0 and len(E_name_list) != 0:#战斗主循环
        turn+=1
        input()
        print("--------战斗中！回合:"+str(turn)+"---------")
        #友方
        if F_attacker_name=='player':#是玩家操作
            player_choose=input("|0:休息一回合|1:攻击|:")
            if player_choose=="0":
                print("&&&友方:" + F_attacker_name + "选择了休息！躯干恢复少许生命！")
                F_attacker_shuxing['health']['躯干'] += F_attacker_shuxing['health']['躯干'] // 10

            elif player_choose=="1":
                list1=player_data.player_data_global['player_skill']
                #print(list)
                try:
                    skill=int(input("请选择使用的技能！(0——x):"))
                    a=list1[skill]
                except:
                    skill=0
                data = pd.read_excel('skill.xlsx', sheet_name='名称', header=None)
                position = SF.get_coordinates(data, list1[skill])
                skill_id=pd.read_excel('skill.xlsx', sheet_name='技能ID', header=None).values[position[0],position[1]]
                return_data=eval('skillFunction.skill_'+str(skill_id))(F_attacker_shuxing,F_attacker_name,E_attacker_name,E_attacker_shuxing)
                #【伤害0，1法力消耗,2 buff名,3扣血点】

                F_attacker_shuxing['法力']-= return_data[1]
                E_attacker_buff.append(return_data[2])
                if (E_attacker_shuxing['health'][return_data[3]] - return_data[0]) <=0:#
                    print(E_attacker_name+"的【"+return_data[3]+'】被这一击打爆了！被这一击打爆了！伤害扩散到了躯干部位')
                    if E_attacker_shuxing['health'][return_data[3]]>0:#先前没爆
                        E_attacker_shuxing['health']['躯干']-=return_data[0] - E_attacker_shuxing['health'][return_data[3]]
                        E_attacker_shuxing['health'][return_data[3]]=0
                    else:
                        E_attacker_shuxing['health']['躯干'] -= return_data[0]
                else:
                    E_attacker_shuxing['health'][return_data[3]] -= return_data[0]


            else:
                print("\n&&&友方:" + F_attacker_name + "选择了发呆！躯干恢复少许生命！")
                F_attacker_shuxing['health']['躯干'] += F_attacker_shuxing['health']['躯干'] // 20

                #2023.1.27停工符号
        else:#自动打架,不是玩家
            ran_number=str(random.randint(0,1))
            if ran_number=="0" and 0<F_attacker_shuxing['health']['躯干']<=30:
                print("&&&友方:"+F_attacker_name+"体力不支！选择了休息！躯干恢复少许生命！")
                F_attacker_shuxing['health']['躯干'] += F_attacker_shuxing['health']['躯干'] // 10



            else:
                list1=F_attacker_skill
                #print(list)
                if len(list1)>1:


                    skill=F_attacker_skill[random.randint(0,len(list1)-1)]
                else:
                    skill=list1[0]
                data = pd.read_excel('skill.xlsx', sheet_name='名称', header=None)
                position = SF.get_coordinates(data, skill)
                skill_id=pd.read_excel('skill.xlsx', sheet_name='技能ID', header=None).values[position[0],position[1]]
                return_data = eval('skillFunction.skill_' + str(skill_id))(F_attacker_shuxing, F_attacker_name, E_attacker_name,
                                                                   E_attacker_shuxing)
                #print(return_data)

                F_attacker_shuxing['法力'] -= return_data[1]
                E_attacker_buff.append(return_data[2])

                #伤势警告
                if (E_attacker_shuxing['health'][return_data[3]] - return_data[0]) <=0:#
                    print(E_attacker_name+"的【"+return_data[3]+'】被这一击打爆了！被这一击打爆了！伤害扩散到了躯干部位')
                    if E_attacker_shuxing['health'][return_data[3]]>0:#先前没爆
                        E_attacker_shuxing['health']['躯干']-=return_data[0] - E_attacker_shuxing['health'][return_data[3]]
                        E_attacker_shuxing['health'][return_data[3]]=0
                    else:
                        E_attacker_shuxing['health']['躯干'] -= return_data[0]
                else:
                    E_attacker_shuxing['health'][return_data[3]] -= return_data[0]


                print("-"*26)
                """
            else:
                #print(ran_number)

                print("&&&友方:" + F_attacker_name + "选择了休息！躯干恢复少许生命！")
                F_attacker_shuxing['health']['躯干'] += F_attacker_shuxing['health']['躯干'] // 10
                print("-" * 26)"""




        # 敌方
        ran_number = str(random.randint(0, 1))
        if ran_number=="0" and 0<E_attacker_shuxing['health']['躯干']<=30:
            print("&&&敌人:"+E_attacker_name + "体力不支,选择了休息！躯干恢复少许生命值！")
            E_attacker_shuxing['health']['躯干']+=E_attacker_shuxing['health']['躯干']//10
            print("-" * 26)



        else:
            list1 = E_attacker_skill
            if len(list1) > 1:
                list1=list(E_attacker_skill)
                skill = list1[random.randint(0, len(list1)-1)]
            else:
                skill = list1[0]
            data = pd.read_excel('skill.xlsx', sheet_name='名称', header=None)
            position = SF.get_coordinates(data, skill)
            skill_id = pd.read_excel('skill.xlsx', sheet_name='技能ID', header=None).values[position[0], position[1]]
            return_data = eval('skillFunction.skill_' + str(skill_id))(E_attacker_shuxing, E_attacker_name,
                                                                       F_attacker_name,
                                                                       F_attacker_shuxing)
            #print(return_data)
            #F_attacker_shuxing['health'][return_data[3]] -= return_data[0]
            E_attacker_shuxing['法力'] -= return_data[1]
            F_attacker_buff.append(return_data[2])
            if (F_attacker_shuxing['health'][return_data[3]] - return_data[0]) <= 0:  #
                print(F_attacker_name + "的【" + return_data[3] + '】被打爆了！溢出伤害扩散到了躯干部位')
                if F_attacker_shuxing['health'][return_data[3]] > 0:  # 先前没爆
                    F_attacker_shuxing['health']['躯干'] -= return_data[0] - F_attacker_shuxing['health'][return_data[3]]
                    F_attacker_shuxing['health'][return_data[3]] = 0
                else:
                    F_attacker_shuxing['health']['躯干'] -= return_data[0]
            else:
                F_attacker_shuxing['health'][return_data[3]] -= return_data[0]
            print("-" * 26)
            """
        else:
            #print(ran_number)
            print("&&&友方:" + E_attacker_name + "选择了休息！躯干恢复少许生命！")
            E_attacker_shuxing['health']['躯干'] += E_attacker_shuxing['health']['躯干'] // 10
            #print("&&&敌人:"+E_attacker_name + "选择了休息！")

            print("-" * 26)"""





        #致命伤伤势判断
        print(E_attacker_name+"："+str(E_attacker_shuxing['health']))
        print(F_attacker_name+":"+str(F_attacker_shuxing['health']))
        if F_attacker_shuxing['health']['头']<=0 or F_attacker_shuxing['health']['躯干']<=0:
            if F_attacker_shuxing['health']['头']<=0:
                print("【"+F_attacker_name+" 因【头】被"+E_attacker_name+"打爆了而死亡！】")
            if F_attacker_shuxing['health']['躯干']<=0:
                print("【"+F_attacker_name+" 因【躯干】被"+E_attacker_name+"打爆了而死亡！】")
            del F_name_list[0]
        if E_attacker_shuxing['health']['头']<=0 or E_attacker_shuxing['health']['躯干']<=0:
            if E_attacker_shuxing['health']['头']<=0:
                print("【"+E_attacker_name+" 因【头】被"+F_attacker_name+"打爆了而死亡！】")
            if E_attacker_shuxing['health']['躯干']<=0:
                print("【"+E_attacker_name+" 因【躯干】被"+F_attacker_name+"打爆了而死亡！】")
            del E_name_list[0]

    #战斗结算
    if len(F_name_list) ==0:
        print(F_attacker_name+"失败了!")
    elif len(E_name_list) == 0:
        print(E_attacker_name + "失败了!")
        #print(F_attacker_shuxing["health"])
    else:
        print("bugbugbug")
        print(len(F_name_list))
        print(len(E_name_list))
















#battle(['鱼线龙'],['蒙面人'])




    




