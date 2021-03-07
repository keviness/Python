#example2_learn try..except_20190223
class Calculator(object):
    is_raise = True
    def cal(self, express):
        try:
            return eval(express)
        except :
            if self.is_raise:
                print("Zero can\'t be division.")
            else:
                raise ZeroDivisionError
if __name__ == "__main__":
    c = Calculator()
    print(c.cal("20/0"))
