#example2_try..except..else_20190223
while True:
    try:
        a = input("The first number:")
        b = input("The second number:")
        print("The division is :", float(a)/float(b))
    except Exception as e:
        print(e)
        print("Try again please.")
    else:
        print("*"*20)
    finally:
        print("-"*20)
