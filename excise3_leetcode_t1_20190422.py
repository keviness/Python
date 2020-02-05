#exercise3_leetcode_t1_20190422
enter_numbers = input("Enter some numbes(a b c):")
ls = enter_numbers.split(" ")
s = ""
for i in  ls:
    s  += i
data = eval(s)
print(s[: : -1])


    
