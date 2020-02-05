#example2_whlie循环_猜数字_20190106.py

import random
number = random.randint(1, 101)
guess, n = 0, 0
while n < 3:
    num_input = eval(input("Please input one integer:"))
    guess = 3 - n
    if num_input<0 or num_input >= 100:
        print("The number should be in 1-100")
    else:
        if number == num_input:
            print("OK,it\'s right.")
            break
        elif number > num_input:
            print("Your number is more less,please guess again \nyou only have %d times"% guess)
        elif number < num_input:
            print("Your number is bigger,please guess again \nyou only have %d times"% guess)
        else:
            print("Sorry, This a wrong.")
        n += 1
                             
