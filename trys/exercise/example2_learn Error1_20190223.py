#example2_learn Error_1_20190223
n = 0
while n < 5:
    print("This is a division program.")
    c = input("input 'c' continue, otherwise logout:")
    if c == 'c':
        a = input("The first number:")
        b = input("The second number:")
        try:
            print(float(a)/float(b))
            print("*"*20)
        except ZeroDivisionError:
            print("The second number can\'t be zero")
            print("*"*20)
    else:
        break
    n += 1 
