Time=[0,0,0]#天，时，分










def Time_check(input_time):
    while input_time[1]>=24 or input_time[2]>=60:
        if input_time[1]>=24:#小时数大于24
            Gap=input_time[1]-24#计算超出时间 h
            print('*一天过去了')
            input_time[1]=0#时针归零
            input_time[0]+=1
            input_time[0]+=int(Gap)#加上差值
        if input_time[2]>=60:
            Gap = input_time[2] - 60  # 计算超出时间 min
            print('*一个小时过去了')
            input_time[2]=0#分针归零
            input_time[1]+=1#进位
            input_time[2]+=int(Gap)
    return input_time
