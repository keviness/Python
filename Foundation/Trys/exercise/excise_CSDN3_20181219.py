#exercise_回文数_20181219.py

n = input("Enter a random number:")
x = len(n)
flag = True
for i in range(1, x//2):
    if n[i-1] != n[-i]:
        flag = False
        break
if flag:
    print("It is True")
else:
    print("It is wrong")
