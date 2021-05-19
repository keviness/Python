# plots the growth of a 10-year investment 2.py

 #计算和绘图
def creatTable(principal, apr):
    for year in range(1, 11):
        principal = principal * (1 + apr)
        total = caculateNum(principal)
        print("*" * total)
    print("0.0k  2.5k  5.0k  7.5k  10.0k ")
#计算星号数量
def caculateNum(principal):
    total = int(principal * 4 / 1000.0)
    return total


#提示输入本金和利息，提出绘图函数
def main():
    print("This program plots the growth of a 10-year investment")
    principal = eval(input("Enter the initial principal:"))
    apr = eval(input("Enter the annualize interest rate:"))
    creatTable(principal, apr)

main()
    
