def main():
    n = eval(input("How many numbers do you whant?"))
    i, s, a = 1, 0, 0
    while i < n:
        a = i * i
        s = a + s
        i = i +1
    print("the sum is:", s)
main()
