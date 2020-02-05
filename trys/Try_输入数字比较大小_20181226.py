#try-输入数字，判断最大值_20181226.py

def main():
    n = eval(input("How many numbers?"))
    l = []
    for i in range(n):
        a = eval(input("Enter a number please:"))
        l.append(a)
        b = max(l)
    print("The max number is:", b)
main()
