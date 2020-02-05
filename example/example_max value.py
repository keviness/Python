# find the largest value.py

def main():

    n = eval(input("How many numbers are there:"))
    max = eval(input("Enter a number:"))
    for i in range(n - 1):
        x = eval(input("Enter a number>>"))
        if x > max:
            max = x
        print("The largest value is:",max)
        
main()
