**一、字符串转为浮点型**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

```
print("---------------转换数据类型---------------------")
vector = numpy.array(["1", "2", "3"])
print (vector.dtype)
print (vector)

vector = vector.astype(float)   # 字符串转为浮点型
print (vector.dtype)
print (vector)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

**结果图:**

![](https://img2018.cnblogs.com/blog/1588501/201901/1588501-20190123145642507-1995764056.png)

**二、字符串转为日期型、日期型转为整数型**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

```
print("========日期型数据类型转换=============")
f = np.array(["2018","2019-01-01","2019-02-01","2019-01-02 08:08:08"])
print(f)
# 将f数组的元素从字符串改为日期类型
Y = f.astype("M8[Y]")
M = f.astype("M8[M]")
D = f.astype("M8[D]")
h = f.astype("M8[h]")
m = f.astype("M8[m]")
s = f.astype("M8[s]")
print(Y)
print(M)
print(D)
print(h)
print(m)
print(s)

print("========将日期类型转为数值类型==========")
# 日期类型转为数值型，计算出来的数值是从1970年开始至我们要算的日期的间隔
YI = Y.astype("int32")
MI = M.astype("int32")
DI = D.astype("int32")
hI = h.astype("int32")
mI = m.astype("int32")
sI = s.astype("int32")
print(YI)
print(MI)
print(DI)
print(hI)
print(mI)
print(sI)
print(DI[2]-DI[1])
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

**结果图：**

![](https://img2018.cnblogs.com/blog/1588501/201901/1588501-20190123134953865-1240883339.png)

补充知识了解：

数据类型的简写字符码：

![](https://img2018.cnblogs.com/blog/1588501/201901/1588501-20190123135553844-967440758.png)
