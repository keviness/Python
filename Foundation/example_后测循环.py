number = -1
while number < 0 :
    number = eval(input("Enter a positive number:"))
    if number < 0:
        print("The number you entered was not positive,Please enter again!")
    else :
        print("The number you entered was positive, Over!")
    
