### 一，Python字符串是否是数字教程
1，在开发过程中，有时候我们需要判断一个字符串是否是数字形式，在 Python 中，判断字符串是否只由数字组成的函数为:isnumeric() 
2，isnumeric() 函数只能判断 unicode 字符串，我们如果需要定义一个字符串为 Unicode 形式，只要在字符串前添加 ‘u’ 前缀即可。
3，语法
~~~py
str.isnumeric() -> bool
~~~
4，示例
~~~py
#!/usr/bin/python
str = u"this2009"
print str.isnumeric()

str = u"23443434"
print str.isnumeric()
~~~
### 二，python中str函数isdigit、isdecimal、isnumeric的区别
~~~py
num = "1"  #unicode
num.isdigit()   # True
num.isdecimal() # True
num.isnumeric() # True

num = "1" # 全角
num.isdigit()   # True
num.isdecimal() # True
num.isnumeric() # True

num = b"1" # byte
num.isdigit()   # True
num.isdecimal() # AttributeError 'bytes' object has no attribute 'isdecimal'
num.isnumeric() # AttributeError 'bytes' object has no attribute 'isnumeric'

num = "IV" # 罗马数字
num.isdigit()   # True
num.isdecimal() # False
num.isnumeric() # True

num = "四" # 汉字
num.isdigit()   # False
num.isdecimal() # False
num.isnumeric() # True

#===================
isdigit()
True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
False: 汉字数字
Error: 无

isdecimal()
True: Unicode数字，，全角数字（双字节）
False: 罗马数字，汉字数字
Error: byte数字（单字节）

isnumeric()
True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
False: 无
Error: byte数字（单字节）

#================
import unicodedata

unicodedata.digit("2")   # 2
unicodedata.decimal("2") # 2
unicodedata.numeric("2") # 2.0

unicodedata.digit("2")   # 2
unicodedata.decimal("2") # 2
unicodedata.numeric("2") # 2.0

unicodedata.digit(b"3")   # TypeError: must be str, not bytes
unicodedata.decimal(b"3") # TypeError: must be str, not bytes
unicodedata.numeric(b"3") # TypeError: must be str, not bytes

unicodedata.digit("Ⅷ")   # ValueError: not a digit
unicodedata.decimal("Ⅷ") # ValueError: not a decimal
unicodedata.numeric("Ⅷ") # 8.0

unicodedata.digit("四")   # ValueError: not a digit
unicodedata.decimal("四") # ValueError: not a decimal
unicodedata.numeric("四") # 4.0
~~~