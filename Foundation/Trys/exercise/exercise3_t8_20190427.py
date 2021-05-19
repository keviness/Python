#exercise3_t8_20190427
'''input:"abcdefghijklmn"
   output:a:1  b:3 c:4...'''
while True:
    st = input("Enter(a string):")
    if st !="":
        d = {}
        ls = st.split(" ")
        new_st = "".join(ls)
        for w in new_st:
            if w in ["!",",","?",".","。"]:
                continue
            d[w] = d.get(w, 0) + 1
        for key in d:
            print("{}:{}".format(key, d[key]))
    else:
        print("The End, GoodBye!~")
        break
            
            
