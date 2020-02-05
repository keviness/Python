#exercise3_t6_20190425
'''input:商品序号，商品
   output:相应商品，添加商品'''
menue = ["西瓜","西红柿","香蕉"]
while True:
    thing = input("Enter(number or string):")
    if thing != "":
        if thing in ["1","2","3","4","5","6","7","8","9"]:
            print("The food you want:", menue[eval(thing)-1])
        else:
            menue.append(thing)
            print("Hello! your food menue has built!\nyour food is:%s"%(menue[-1]))
        continue
    else:
        print("The end!")
        break
    
        
    
