#example2_learn try..except.._20190223
while True:
    print("This is a division program.")
    c = input("enter a 'c' continue, otherwise logout:")
    if c == 'c':
        try:
            a = input("The first number:")
            b = input("The second number:")
            print("the division is:", (float(a)/float(b)))
            print("*"*20)
        except ZeroDivisionError:
            print("The second number can\'t be zero")
            print("*"*20)
        except ValueError:
            print("Please input number")
            print("*"*20)
    else:
        break
