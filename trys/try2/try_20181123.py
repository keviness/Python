# try_返回前n项的平方和_20181123.py

def main():
    Q = eval(input("How many numbers do you want to calculate?"))
    i, a, s = 0, 0, 0
    while i < Q+1:
        a = i * i
        s += a
        i += 1
    print("The sum is :", s)

main()
        
    
