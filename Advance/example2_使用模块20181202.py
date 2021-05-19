# 使用模块—201812.2

def _private_1 (name):
    print( "hello, world, %s" % name)
def _private_2 (name):
    print ("Hi, %s" % name)
def greeting():
    name = input("what\'s your name?")
    if len(name) > 3:
        return _private_1 (name)
    else:
        return _private_2 (name)

greeting()
