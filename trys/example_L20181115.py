def add(x, y, f):
    return f(x) + f(y)
 
a = add(-5, 6, abs)
print(a)

