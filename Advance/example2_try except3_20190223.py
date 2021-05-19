#example2_try..except_20190223
while True:
    c = input("Enter 'c' continue, otherwise logout:")
    if c == 'c':
        try:
            a = input("The first number:")
            b = input("The second number:")
            print("The Division is:", float(a)/float(b))
            print("*"*20)
        except (ZeroDivisionError, ValueError):
            print("Please enter rightly.")
            print("*"*20)
    else:
        break
