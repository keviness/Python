#example2_try..except.._3_20190223
while True:
    print("This is a division program.")
    c = input("Enter 'c' continue, otherwise logout:")
    if c == "c":
        try:
            a = input("The first number:")
            b = input("The second number:")
            print("The division is:", float(a)/float(b))
        except (ZeroDivisionError, ValueError) as e:
            print(e)
            print("-"*20)
    else:
        break
    
                  
