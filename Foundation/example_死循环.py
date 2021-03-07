#coding:UTF-8
while True:
    try:
        x = int(input("please enter a number:"))
        break
    except ValueError:
        print("Oops, that was no valid number. Try again...")
