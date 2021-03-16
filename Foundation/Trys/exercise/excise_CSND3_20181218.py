#excise_CSDN3_20181218.py

week = eval(input("enter a number(1-7):"))
a = "MonTueWedThuFriStaSun"
p = (week - 1) * 3
print("today is :" , a[p : p+3],".")
