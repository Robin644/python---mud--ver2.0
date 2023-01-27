def skill_huiquan(A_shuxing,A_name,B_name,B_shuxing):
    import random
    print("【"+A_name+"挥拳砸向了"+B_name+"!】")

    damage=A_shuxing["力量"]*random.randint(2,3)-B_shuxing["防御"]


    consumption=0
    buff=None

    list=["躯干","左肢","右肢","头"]
    destination=list[random.randint(0,3)]
    if destination=="头":
        damage*=2
        print("爆头！伤害加倍！")
    if damage<=0:
        print("未破防！造成0点伤害!")
        damage=0
    print("拳头砸中了"+B_name+"的【"+destination+"】!造成了【" + str(damage) + "】点伤害！")
    return [damage,consumption,buff,destination]#【伤害，法力消耗,buff名，部位】
def skill_yingchang(A_shuxing,A_name,B_name,B_shuxing):
    import random
    print("【"+A_name+"风情万种地倩笑一声，从大红色棉衣里掏出一团残破的纸张，口中念念有词地朝着"+B_name+"微笑!】")
    print("！仿佛来自【地狱深渊】的呓语萦绕在【"+B_name+"】的耳边！"+A_name+"的吟唱无视了所有防御，直击他的面门！")
    damage=A_shuxing["智力"]*random.randint(2,3)

    destination='头'
    consumption=1#法力消耗
    buff=None
    print(""+B_name+"的【"+destination+"】因吟唱造成了【" + str(damage) + "】点伤害！")
    print(A_name+"乘胜追击，继续对"+B_name+"【喊】道：吾亦知矣为德意志之反战君子也已!")
    damage+=A_shuxing['力量']*6
    print("总计造成了【"+str(damage)+"】点伤害！")
    return [damage,consumption,buff,destination]#【伤害，法力消耗,buff名，部位】
"""
skill_id='huiquan'
data=eval('skill_'+str(skill_id))({"力量":1111},'a','b',{'力量':1,'防御':1})
print(data)
"""
