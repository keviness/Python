#t16

N = eval(input("N:"))
tup=[]
if N<1000:
    for  i in range(N):
        string_list=input("element:").split(" ")
        for ele in string_list:
            element= eval(ele)
            if element%6==0:
                tup.append(element)
            else:
                print(-1)
    for w in tup:
        print(w, end=" ")
