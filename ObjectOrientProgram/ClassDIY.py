class Chain(object):
    def __init__(self, path=''):
       self.__path = path

    def __getattr__(self, path):
       return Chain('%s/%s' % (self.__path, path))

    def __call__(self, path):
       return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
       return self.__path

    __repr__ = __str__

print(Chain().users('michael').repos) # /users/michael/repo


#Step 1：
#Chain()  # 实例化

#Step 2：
#Chain().users
# 由于没有给实例传入初始化对应属性的具体信息，从而自动调用__getattr__()函数，从而有：
#Chain().users = Chain('\users') # 这是重建实例

#Step 3:
#Chain().users('michael')
#Chain().users('michael') = Chain('\users')('michael') # 这是对实例直接调用，相当于调用普通函数一样
# 关键就在这步，上面的朋友没有说明晰（并不是说你们不懂），这一步返回的是Chain('\users\michael'),再一次重建实例，覆盖掉Chain('\users'),
#记 renew = Chain('\users\michael')， 此时新实例的属性renew.__path = \users\michael;

#Step 4:
#Chain().users('michael').repos
# 这一步是查询renew实例的属性repos，由于没有这一属性，就会执行__getattr__()函数，再一次返回新的实例Chain('\users\michael\repos')并且覆盖点之前的实例，
# 这里记 trinew =Chain('\users\michael\repos')，不要忘了，一单定义了一个新的实例，就会执行__init__方法；

#Step 5：
#print(Chain().users('michael').repos) = print(trinew)  
#由于我们定义了__str__()方法，那么打印的时候就会调用此方法，据此方法的定义，打印回来的是trinew的__path属性，即——\users\michael\repos  。至此，我们也把所有定义的有特殊用的方法都用上了，完毕。