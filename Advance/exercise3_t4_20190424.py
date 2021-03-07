#exercise3_T4_20190424
ls = []
while True:
    num = eval(input("Enter the number:"))
    ls.append(num)
    if len(ls) == 6:
        break
    ls.sort()
print(ls)
