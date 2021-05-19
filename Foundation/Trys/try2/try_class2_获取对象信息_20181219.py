# try_class_获取对象信息_20181219.py

class Mouse(object):
    def call(self):
        print("This is a beautiful fenature.")
class Desk(Mouse):
    def call(self):
        print("This is a desk")
class Wooden(Desk):
    def Call(self):
        print("The desk made with wooden.")
desk = Mouse()
chair = Wooden()
def print_name(fen):
    fen.call()
    fen.call()
