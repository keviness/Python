#exercise3_t4_20190425
'''输入：格式：a + b
输出：求取：值'''
while True:
    num = input("Enter(a+b) :")
    if num != "":
        ls = num.split("+")
        a, b = eval(ls[0]), eval(ls[1])
        s = a + b
        print(num,"=",s)
    else:
        print("The end!")
        break
    
        
