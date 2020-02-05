#review1_Fibonacci1_20190605

def Fabo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return Fabo(n-1) + Fabo(n-2)
def main():
    while True:
        n = eval(input("How numbers do you want to deal with:"))
        if n != "":
            s = Fabo(n)
            print("The Fabo-numbers is :", s)
            break
        else:
            print("The wrong! try again.")
if __name__ == "__main__":
    main()
        
    
