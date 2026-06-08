p=20
if (p>10):
    print("p大于10")
else:
    print("p不大于10")
#多分支判断
delay=15
if (delay>30):
    print("高时延")
elif (delay>20):
    print("中时延")
else:
    print("低时延")
#多条件判断
power_dbm = -25
delay_ms = 10
frequency_ghz = 6

if power_dbm > -30 and delay_ms < 20 and 1 <= frequency_ghz <= 10:
    print("链路可用")
else:
    print("链路不可用") 
#嵌套判断
power_dbm = -25
delay_ms = 10

if power_dbm > -30:
    print("功率合格")
    
    if delay_ms < 20:
        print("时延合格")
        print("链路可用")
    else:
        print("时延过高")
        print("链路不可用")
else:
    print("功率过低")
    print("链路不可用")
#练习1
power_input = float(input("输入功率："))
delay_input = float(input("输入时延："))
if power_input > -30 and delay_input < 20:
    print("链路可用")
else:
    print("链路不可用")
#练习2
if power_input < -30:
    print("链路不可用，功率过低")
elif delay_input >= 20:
        print("链路不可用，时延过高")
else:
        print("链路可用")
#练习三
inputfrequency_Ghz=float(input("输入频率："))
if 1<= inputfrequency_Ghz <= 10:
    print("频率在测量范围内")
else:
    print("频率超出测量范围")

#练习四
P1=float(input("输入功率1(dbm)："))
delay1=float(input("输入时延1(ms)："))
f1=float(input("输入频率1(GHz)："))
if P1 <= -30:
    print("功率过低")
elif delay1 >= 20:
    print("时延过高")
elif f1 < 1 or f1 > 10:
    print("频率超出测量范围")
else:    
    print("链路质量合格")
