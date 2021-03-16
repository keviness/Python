# exercise average 20180927


def main():

    sum = 0
    count = 0
    xstr = input("Enter a number(<enter> to quit):")
    while xstr != "":
        x = eval(xstr)
        sum += x
        count += 1
        xstr = input("Enter a number (<enter> to quit)>>")

    print("\n The average of the number is:" , sum/count )

main()
    
