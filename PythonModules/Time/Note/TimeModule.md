# python time模块详解

**一、在Python中，时间的表示通常有以下三方式：**

1. UTC（Coordinated Universal Time，世界协调时）亦即格林威治天文时间，世界标准时间。在中国为UTC+8。DST（Daylight Saving Time）即夏令时。
2. 时间戳（timestamp）的方式：通常来说，时间戳表示的是从**1970年1月1日00:00:00**开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。返回时间戳方式的函数主要有time()，clock()等。
3. 元组（struct_time）方式：struct_time元组共有9个元素，返回struct_time的函数主要有gmtime()，localtime()，strptime()。下面列出这种方式元组中的几个元素：

![](https://pic4.zhimg.com/80/v2-087c3ecbd841f2d364bde04ba6fc15e3_1440w.jpg)

**二、time模块中常用的几个函数：**

 **1）** time. **localtime([secs])** ：将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。

![](https://pic4.zhimg.com/80/v2-a0eb724187e6eb3a8de6458903180bff_1440w.png)

 **2）** time. **gmtime([secs])** ：和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）

![](https://pic3.zhimg.com/80/v2-bcbe10a954eb444878c4e61edce6b186_1440w.png)

 **3）** time. **time()** ：返回当前时间的时间戳。

![](https://pic2.zhimg.com/80/v2-d90ab26f85bb897e6df2adecbe974121_1440w.jpg)

 **4）** time. **mktime(t)** ：将一个struct_time转化为时间戳。

![](https://pic2.zhimg.com/80/v2-7b9e3fb10465a10f35d8ccfeb32f7649_1440w.jpg)

 **5）** time. **sleep(secs)** ：线程推迟指定的时间运行。单位为秒。

 **6）** time. **asctime([t])** ：把一个表示时间的元组或者struct_time表示为这种形式： **'Sun Jun 20 23:21:05 1993'** 。如果没有参数，将会将time.localtime()作为参数传入。

![](https://pic1.zhimg.com/80/v2-94b90e75df3ad6f0fa87c0335c330fec_1440w.jpg)

 **7）** time. **ctime([secs])** ：把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。

![](https://pic4.zhimg.com/80/v2-25d56cab421adc0d5febcfd76bb17fe3_1440w.png)

 **8）** time. **strftime(format[, t])** ：把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。如果元组中任何一个元素越界，ValueError的错误将会被抛出。

![](https://pic2.zhimg.com/80/v2-433be3bb21069f947250030808949ac1_1440w.jpg)

 **备注** ：

1. “%p”只有与“%I”配合使用才有效果。
2. 文档中强调确实是0 - 61，而不是59，闰年秒占两秒（汗一个）。
3. 当使用strptime()函数时，只有当在这年中的周数和天数被确定的时候%U和%W才会被计算。

举个例子：

![](https://pic2.zhimg.com/80/v2-31feea9d953d8932573e71cae0a92dc9_1440w.png)

 **9）** time **.strptime(string[, format])** ：把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。

![](https://pic2.zhimg.com/80/v2-99a1468f3278196912b83235106fe861_1440w.png)

在这个函数中，format默认为： **"%a %b %d %H:%M:%S %Y"** 。

最后，我们来对time模块进行一个总结。根据之前描述，在Python中共有三种表达方式：

1）timestamp

2）格式化字符串

3）tuple或者struct_time

它们之间的转化如图所示：

![img](https://pic4.zhimg.com/80/v2-41b40a235f51814a7d167260768bca3b_1440w.jpg)
