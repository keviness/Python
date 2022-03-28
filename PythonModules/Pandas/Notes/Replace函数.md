# [pandas replace() 替换用法](https://www.cnblogs.com/cgmcoding/p/13362539.html)

之前写的替换都是整个值，也即是说如果被替换值='asdfg'，之前的只有值等于='asdfg'，才可以被替换，但是我们很多时候是值想替换局部的，比如说‘深圳地区’，替换为‘深圳市’，那么就得先str,代码如下：

```
main_copy['city']=main_copy['city'].str.replace('地区','市')
```

====================================================================

# replace()

既可以替换某列，也可以替换某行，还可以全表替换

df.replace() 或者 df[col]replace()

```
#参数如下：
df.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad',)
```

# 参数说明：

* to_replace：被替换的值
* value：替换后的值
* inplace：是否要改变原数据，False是不改变，True是改变，默认是False
* limit：控制填充次数
* regex：是否使用正则,False是不使用，True是使用，默认是False
* method：填充方式，pad,ffill,bfill分别是向前、向前、向后填充

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

```
import pandas as pd
import numpy as np

#构造数据
df=pd.DataFrame({'a':['?',7499,'?',7566,7654,'?',7782],'b':['SMITH', '.','$','.' ,'MARTIM','BLAKE','CLARK'],
'c':['CLERK','SALESMAN','$','MANAGER','$','MANAGER','$'],
'd':[7902,7698,7698,7839,7698,7839,7839],
'e':['1980/12/17','1981/2/20','1981/2/22','1981/4/2','1981/9/28','1981/5/1','1981/6/9'],
'f':[800,1600,1250,2975,1230,2859,2450],
'g':[np.nan,300.0,500.0,np.nan,1400.0,np.nan,np.nan],
'h':[20,30,30,20,30,30,10]})


#替换全部或者某行某列
#全部替换，这二者效果一样
df.replace(20,30)
df.replace(to_replace=20,value=30)

#某一列或者某几列
df['h'].replace(20,30)
df[['b','c']].replace('$','rmb')

#某一行或者几行
df.iloc[1].replace(1600,1700)
df.iloc[1:3].replace(30,40)

#inplace=True
df.replace(20,30,inplace=True)
df.iloc[1:3].replace(30,40,inplace=True)


#用list或者dict进行单值或者多值填充,
#单值
#注意，list是前者替换后者，dict字典里的建作为原值，字典里的值作为替换的新值
df.replace([20,30])
df.replace({20:30})
#多值,list是list逗号后的值替换list的值，dict字典里的建作为原值，字典里的值作为替换的新值
df.replace([20,1600],[40,1700])  #20被40替换，1600被1700替换
df.replace([20,30],'b')  #20,30都被b替换
df.replace({20:30,1600:1700})
df.replace({20,30},{'a','b'})  #这个和list多值用法一样

#,method
#其实只需要传入被替换的值，
df.replace(['a',30],method='pad')
df.replace(['a',30],method='ffill')
df.replace(['a',30],method='bfill')

#可以直接这样表达
df.replace(30,method='bfill')  #用30下面的最靠近非30的值填充
df.replace(30,method='ffill')  #用30上面最靠近非30的值填充
df.replace(30,method='pad')   #用30上面最靠近非30的值填充

#一般用于空值填充
df.replace(np.nan,method='bfill') 

#limit
df.replace(30,method='bfill',limit=1)  #现在填充的间隔数
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

## 正则替换的需要先补充一下正则表达式

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

```
#正则替换
#转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
df.replace(r'\?|\.|\$',np.nan)  #和原来没有变化
df.replace(r'\?|\.|\$',np.nan,regex=True)#用np.nan替换？或.或$原字符
df.replace([r'\?',r'\$'],np.nan,regex=True)#用np.nan替换？和$
df.replace([r'\?',r'\$'],[np.nan,'NA'],regex=True)#用np.nan替换？用NA替换$符号
df.replace(regex={r'\?':None})

#当然，如果不想使用inplace=True，也可以这样子表达
df=df.replace(20,30)
df.replace(20,30,inplace=True)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

## 全部代码如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

```
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:52:00 2020

@author: Admin
"""



import pandas as pd
import numpy as np

#构造数据
df=pd.DataFrame({'a':['?',7499,'?',7566,7654,'?',7782],'b':['SMITH', '.','$','.' ,'MARTIM','BLAKE','CLARK'],
'c':['CLERK','SALESMAN','$','MANAGER','$','MANAGER','$'],
'd':[7902,7698,7698,7839,7698,7839,7839],
'e':['1980/12/17','1981/2/20','1981/2/22','1981/4/2','1981/9/28','1981/5/1','1981/6/9'],
'f':[800,1600,1250,2975,1230,2859,2450],
'g':[np.nan,300.0,500.0,np.nan,1400.0,np.nan,np.nan],
'h':[20,30,30,20,30,30,10]})


#替换全部或者某行某列
#全部替换，这二者效果一样
df.replace(20,30)
df.replace(to_replace=20,value=30)

#某一列或者某几列
df['h'].replace(20,30)
df[['b','c']].replace('$','rmb')

#某一行或者几行
df.iloc[1].replace(1600,1700)
df.iloc[1:3].replace(30,40)

#inplace=True
df.replace(20,30,inplace=True)
df.iloc[1:3].replace(30,40,inplace=True)


#用list或者dict进行单值或者多值填充,
#单值
#注意，list是前者替换后者，dict字典里的建作为原值，字典里的值作为替换的新值
df.replace([20,30])
df.replace({20:30})
#多值,list是list逗号后的值替换list的值，dict字典里的建作为原值，字典里的值作为替换的新值
df.replace([20,1600],[40,1700])  #20被40替换，1600被1700替换
df.replace([20,30],'b')  #20,30都被b替换
df.replace({20:30,1600:1700})
df.replace({20,30},{'a','b'})  #这个和list多值用法一样

#,method
#其实只需要传入被替换的值，
df.replace(['a',30],method='pad')
df.replace(['a',30],method='ffill')
df.replace(['a',30],method='bfill')

#可以直接这样表达
df.replace(30,method='bfill')  #用30下面的最靠近非30的值填充
df.replace(30,method='ffill')  #用30上面最靠近非30的值填充
df.replace(30,method='pad')   #用30上面最靠近非30的值填充

#一般用于空值填充
df.replace(np.nan,method='bfill') 

#limit
df.replace(30,method='bfill',limit=1)  #现在填充的间隔数



#正则替换
#转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
df.replace(r'\?|\.|\$',np.nan)  #和原来没有变化
df.replace(r'\?|\.|\$',np.nan,regex=True)#用np.nan替换？或.或$原字符
df.replace([r'\?',r'\$'],np.nan,regex=True)#用np.nan替换？和$
df.replace([r'\?',r'\$'],[np.nan,'NA'],regex=True)#用np.nan替换？用NA替换$符号
df.replace(regex={r'\?':None})

#当然，如果不想使用inplace=True，也可以这样子表达
df=df.replace(20,30)
df.replace(20,30,inplace=True)
```
