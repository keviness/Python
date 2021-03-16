#exercise3_t5_20190425
'''input:[a, b, c]
   output:[ab, ac, bc, ba, bc, ca, cb]'''
while True:
    lst = input("Enter([a, b, c]):")
    built_lst = []
    if lst != "":
        new_lst = eval(lst)
        for i in new_lst:
            for j in new_lst:
                if i != j:
                    built_lst.append(str(i)+str(j))
        print(built_lst)
    else:
        print("The End!")
        break
                    
