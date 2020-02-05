# 计算两数加减法

def sumDiff(x,y):
    sum = x + y
    diff = x - y
    return sum, diff

def main():
    num1, num2 = eval(input("Please enter two numbers (num1, num2):"))
    s, d = sumDiff(num1, num2)
    
    print("The sum is :" +str(s) + "and the different is:" + str(d))
    
    
main()

    
