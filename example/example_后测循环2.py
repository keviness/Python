# break实现后测循环

while True:
    number = eval(input("Enter a positive number:"))
    if number >= 0:
        print("The number you entered was positive , Over!")
        break
    else:
        print("The number you entered was not positive,Please enter again.")
