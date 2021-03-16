#try2_a game of guess number_20190321
import random
target = random.randint(1, 20)
count = 0
while True:
    try:
        goal = eval(input("Enter a number(1-20):"))
        count += 1
        if goal > target:
            print("It is so large, try again")
        elif goal < target:
            print("It is less than the number you enter!")
        else:
            print("It is right!")
            break
    except:
        print("The wrong, please enter again!")
        continue
print("the times you have used:",count)
