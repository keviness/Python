# exercise-CSDN1-20181218.py

x = int(input("请输入一个整数："))
if 0 < x < 99:
    print("enter more than three bits numbers")
else:
    x = x // 100
    print(x)
