#try_for循环寻找一组数的偶数_20190106.py
lt = input("Enter some numbers please(x, y, z, ...):")
lst = lt.split(",")
s = []
t = []
num_lst = []
for i in lst:
    num_lst.append(int(i))
for n in num_lst:
    if n %2 ==0:
        s.append(n)
    else:
        t.append(n)
print("the double numbers are:",s)
print("The odd numbers are:",t)
