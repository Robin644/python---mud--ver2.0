#npc功能相关
def npc_function_battle(npc_data):
    npc_data=list(npc_data)
    npc_name=npc_data[0]
    import battle
    battle.battle(['player'],[npc_name])

    #print("战斗系统还没做好，别急")

def npc_function_talk(npc_data:str):
    npc_data=list(npc_data)#[npc_name]
    import map_data
    import random
    sentence1=["干嘛？","怎么了？","你是？","哈？","什么?"]
    sentence2=["有什么事？","我没空理你。","我好累，别跟我说话。","你站在这干嘛？","什么情况？","你看过《郁经》吗？"]
    print(npc_data[0]+"盯着你说："+sentence1[random.randint(0,4)]+sentence2[random.randint(0,4)])
    input()
#npc_function_talk("0")
