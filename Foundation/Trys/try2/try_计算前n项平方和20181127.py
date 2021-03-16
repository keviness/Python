#  计算前几项的平方和-20181127.py

def main():
    n = int(input("How many numbers do you whant?"))  
    i, s, a = 0, 0, 0   
    while i < n + 1: 
        a = i * i  
        s = a + s
        i = i +1
    print("the sum is:", s)

main()
