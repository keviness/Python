#example2_try..except_4_20190223
while True:
    print("This is a division program.")
    c = input("Enter 'c' comtinue, otherwise logout:")
    if c == "c":
        try:
            a = input("The first number:")
            b = input("The second number:")
            print("The division is :", float(a)/float(b))
        except Exception as e:
            print(e)
            print("-"*30)
    else:
        break
