#exercise3_t9_20190427
'''求素数个数
   input:a~b
   output:a,b间素数'''
while True:
    s = []
    limit = input("Enter(a~b):")
    if limit != "":
        lst = limit.split("~")
        a, b = eval(lst[0]), eval(lst[1])
        for i in range(a, b+1):
            target = True
            for x in range(2, i):
                if i%x == 0 :
                    target = False
            if target:
                s.append(i)
        print("The single number is:", s)
    else:
        print("The End, good\nGoodBye!~")
        break
                    
