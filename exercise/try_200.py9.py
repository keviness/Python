n = eval(input(""))
lst = []
for i in range(n):
    a, b, c, d, e = input("").split(' ')
    a, b, c, d, e = eval(a), eval(b), eval(c), eval(d), eval(e)
    lst.append(((e/(7*(a+b+c+d))),e))
    lst.sort(key=lambda x:x[0], reverse=False)
for ele, ke in enumerate(lst, start=1):
    print(ele, ke[1])
