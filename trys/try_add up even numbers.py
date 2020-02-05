# 计算前n个偶数之和.py

def main():

    n = eval(input("how many even numbers do you want to add up:"))
    sum = 2
    i = 1
    while i < n:
       sum = n + n**2
       i += 1
       
    print("The sum is :", sum)

main()
