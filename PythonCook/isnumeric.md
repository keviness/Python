## Python字符串是否是数字教程
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