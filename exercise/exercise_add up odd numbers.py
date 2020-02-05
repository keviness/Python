# exercise forth 20180929.py

def main():

    n = eval(input("how mang number do you want to calcute:"))
    sum = 2
    number = 1
    while number < n:
        sum = n/2 + n**2
        number += n
        if number > n:
            break
    print("The sum is :" , sum)

main()
