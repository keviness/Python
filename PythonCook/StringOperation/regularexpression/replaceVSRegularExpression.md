# str.replace() VS 正则表达式的替换
## 一，str.replace(oldchar, newchar， count=0)
* oldchar : 旧字符串
* newchar : 新字符串
* count : 替换次数，默认0
## 二，re.sub(pattern, repl, string, count=0, flags=0)
re.sub(pattern, repl, string, count=0, flags=0)
* pattern : 正则中的模式字符串。
* repl : 替换的字符串，也可为一个函数。
* string : 要被查找替换的原始字符串。
* count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
* flags : 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

## 二，示例
~~~py
import re
# 1，用字符串本身的replace方法:
print('=======replace()替换=======')
a1 = 'Hello world'
b1 = a1.replace('world', 'python')
print('1原始字符串:{}'.format(a1))
print('1替换字符串:{}'.format(b1))
 
a2 = 'Hello world world world world World'
b2 = a2.replace('world', 'python')
print('2原始字符串:{}'.format(a2))
print('2替换字符串:{}'.format(b2))
 
a3 = 'Hello world world world world World'
b3 = a3.replace('world', 'python', 2)    # 数字2表示替换2次
print('3原始字符串:{}'.format(a3))
print('3替换字符串:{}'.format(b3))
 
a4 = 'Hello world world world world World'
b4 = a4.replace('world', 'python', 2).replace('W', 'H').replace(' ', '_')    # replace()可连续使用
print('4原始字符串:{}'.format(a4))
print('4替换字符串:{}'.format(b4))
 
print('*****替换特殊字符*****')
a5 = 'Hello\world\hello/python:World*Python?555"666<777>888|999OK'
b5 = a5.replace('\\', '_')    # 注意\\表示\
print('5原始字符串:{}'.format(a5))
print('5替换字符串:{}'.format(b5))
 
b6 = a5.replace('/', '_')
print('6原始字符串:{}'.format(a5))
print('6替换字符串:{}'.format(b6))
b7 = a5.replace(':', '_').replace('"', '_')
print('7原始字符串:{}'.format(a5))
print('7替换字符串:{}'.format(b7))
 
print('=======正则表达式替换=======')
# 2用正则表达式来完成替换:
c1 = 'hello world'
strinfo = re.compile('world')
d1 = strinfo.sub('python', c1)
print('1原始字符串:{}'.format(c1))
print('1替换字符串:{}'.format(d1))
 
c2 = 'hello world world world World'
strinfo = re.compile('world')
d2 = strinfo.sub('python', c2,)
print('2原始字符串:{}'.format(c2))
print('2替换字符串:{}'.format(d2))
 
c2_1 = 'hello world world world World'
strinfo = re.compile('world')
d2_1 = strinfo.sub('python', c2_1, 2)    # 只替换2次
print('2_1原始字符串:{}'.format(c2_1))
print('2_1替换字符串:{}'.format(d2_1))
 
c2_2 = 'hello world world world World'
strinfo = re.compile('world', re.I)   # re.I 表示忽略大小写
d2_2 = strinfo.sub('python', c2_2)
print('2_2原始字符串:{}'.format(c2_2))
print('2_2替换字符串:{}'.format(d2_2))
 
print('*****替换特殊字符*****')
c3 = 'Hello-world\hello/python:World*Python?555"666<777>888|999OK'
strinfo = re.compile('[/:*?"<>|\\\\]')    # 注意用4个\\\\来替换\
d3 = strinfo.sub('_', c3)
print('3原始字符串:{}'.format(c3))
print('3替换字符串:{}'.format(d3))
 
c4 = 'Hello-world\hello/python:World*Python?555"666<777>888|999OK'
strinfo = re.compile(r'[/:*?"<>|\\]')    # 加r,2个\即可
d4 = strinfo.sub('_', c4)
print('4原始字符串:{}'.format(c4))
print('4替换字符串:{}'.format(d4))

#替换结果：
#=======replace()替换=======
1原始字符串:Hello world
1替换字符串:Hello python
2原始字符串:Hello world world world world World
2替换字符串:Hello python python python python World
3原始字符串:Hello world world world world World
3替换字符串:Hello python python world world World
4原始字符串:Hello world world world world World
4替换字符串:Hello_python_python_world_world_Horld
*****替换特殊字符*****
5原始字符串:Hello\world\hello/python:World*Python?555"666<777>888|999OK
5替换字符串:Hello_world_hello/python:World*Python?555"666<777>888|999OK
6原始字符串:Hello\world\hello/python:World*Python?555"666<777>888|999OK
6替换字符串:Hello\world\hello_python:World*Python?555"666<777>888|999OK
7原始字符串:Hello\world\hello/python:World*Python?555"666<777>888|999OK
7替换字符串:Hello\world\hello/python_World*Python?555_666<777>888|999OK
=======正则表达式替换=======
1原始字符串:hello world
1替换字符串:hello python
2原始字符串:hello world world world World
2替换字符串:hello python python python World
2_1原始字符串:hello world world world World
2_1替换字符串:hello python python world World
2_2原始字符串:hello world world world World
2_2替换字符串:hello python python python python
*****替换特殊字符*****
3原始字符串:Hello-world\hello/python:World*Python?555"666<777>888|999OK
3替换字符串:Hello-world_hello_python_World_Python_555_666_777_888_999OK
4原始字符串:Hello-world\hello/python:World*Python?555"666<777>888|999OK
4替换字符串:Hello-world_hello_python_World_Python_555_666_777_888_999OK
~~~