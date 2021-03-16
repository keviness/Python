import random
target = random.randint(1, 20)
count = 5
while count >= 0:
    try:
        guess_num = eval(input("Enter a number(1-20):"))
        count -= 1
        if guess_num > target:
            print("It is more than the number. \nyou only have {:2} times".format(count))
        elif guess_num < target:
            print("It is less than the number. \nyou only have {:2} times".format(count))
        else:
            print("It is right!Congratulation!")
            break
    except:
        print("The wrong,enter again!")
        continue
