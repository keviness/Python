# time库的使用220181209.py

from time import *
s = 50
print("start".center(s//2, "*"))
for i in range(s+1):
    a = "*" * i
    b = "-" * (s-i)
    c = (i/s) * 100
    print("\r {:^3.0f} % [{} >{}]".format(c, a, b))
    sleep(0.1)
print("the end".center(s//2, "*"))
