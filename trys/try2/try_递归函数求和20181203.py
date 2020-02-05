# try-递归函数求前n项和-20181203.py

def cal(n):
    if n ==1:
        return 1
    return pow(n, 2) + cal(n - 1)
    
def main():
    n = eval(input("How numbers:"))
    s = cal(n)
    print("the sum is :", s)

main()
