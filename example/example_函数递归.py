# 函数递归2018.10.13 .py

def reverse(s):

    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
    print(s)
reverse("year")
