#练习1
name="罗云坤";
major="电子科学与技术";
age=24;
print(name)
print(major)
print(age)
#练习2
a=1;
b=2;
c=a+b;
print(c)
#练习3
distance_km=100
speed_km_s=20
time_s=(distance_km/speed_km_s)
print(time_s)  #python里面/表示除法，结果是浮点数
#练习4
P_dbm=10
P_mw=10*(P_dbm/10)
print(P_mw)
#练习5:修改变量名
frequency_Ghz=10
print("当前频率为： ",frequency_Ghz,"Ghz")
frequency_Ghz=20
print("修改后频率为： ",frequency_Ghz,"Ghz")
#练习6:字符串拼接
first_name="罗"
last_name="坤"
full_name=first_name+"云"+last_name
print(full_name)
#练习7:检查变量类型
name="罗云坤"
print(type(name))
age=24
print(type(age))
c=3.0
print(type(c))
is_active=True
print(type(is_active))
#练习8:类型转换//将字符串转换为整数
age_str="24"
age_int=int(age_str)
print(age_int)
#将浮点数转换为整数，不是四舍五入，而是直接去掉小数部分
c_float=3.14
c_int=int(c_float)
print(c_int)
#每行代码输出打印都带上代码行号怎么做？
#可以使用Python的内置函数`enumerate()`来实现。`enumerate()`函数会返回一个包含索引和值的迭代器，可以在打印时显示行号。以下是一个示例：
for i, value in enumerate([age_int, c_int]):
    print(f"Line {i+1}: {value}")  
#练习9：输入链路距离，计算传播时间
distance_km = input("请输入链路距离（公里）：")
speed_km_s = 20  
distance_km=float(distance_km)
time_s=distance_km/speed_km_s
print(f"链路距离为{distance_km}公里时,经历时间为{time_s}秒")