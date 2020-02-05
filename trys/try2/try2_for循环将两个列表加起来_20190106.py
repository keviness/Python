#try_for循环将两个列表加起来_20180106.py
lst1 = input("Enter some number please:")
lst2 = input("Enter something again please:")
lst_1 = lst1.split(",")
lst_2 = lst2.split(",")
for x, y in zip(lst_1, lst_2):
    a, b = int(x), int(y)
    print("the sum is:", a+b)
