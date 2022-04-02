1.DataFrame去重

但是对于pandas的DataFrame格式就比较麻烦，我看了其他博客优化了如下三种方案。

我们先引入数据集：

```
import pandas as pd
data=pd.read_csv(r'D:/home/nohup.out.20191028.startloan.csv',encoding='utf-8')
print(data.info())
```

![](https://img2018.cnblogs.com/blog/1353331/201911/1353331-20191101112026122-572816556.png)

 共有14936条数据，那我们还是按 custId和applyNo去重。

### 1.使用list后手写去重

定义去重函数：我这里使用了遍历行，添加列表的的方式去重。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

```
# 定义去重函数
def dropRep(df):
    list2=[]
    for _,i in df.iterrows():
        i=list(i)
        if i not in list2:
            list2.append(i)
    return list2
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

```
keydata=data[['custId','applyNo']]
len1=keydata.count()
print('去重之前custId +applyNo:',len1)


list2=dropRep(keydata)
print('去重之后custId +applyNo:',len(list2))
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

### 2.使用list后set去重

 用set去重其实遇到了很多问题，set里面的数据必须是不可变数据类型，可hash等等。。所以只能把key1+key2拼成字符串作为一个元素。

```
# 定义去重函数
def dropRepBySet(df):
    set1=set()
    for _,i in df.iterrows():
        set1.add("_".join(list(map(lambda x:str(x),list(i)))))
    return list(set1)
```

而且明显感觉这个方法比上面手写list遍历去重快一些

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

```
keydata=data[['custId','applyNo']]
len1=keydata.count()
print('去重之前custId +applyNo:',len1)


list2=dropRepBySet(keydata)

print('去重之后custId +applyNo:',len(list2))
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

![](https://img2018.cnblogs.com/blog/1353331/201911/1353331-20191101115446079-591170876.png)

### 3.使用pd.DataFrame自带drop_duplicates（）函数去重

```
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
```

* subset : column label or sequence of labels, optional

　　　　用来指定特定的列，默认所有列

* keep : {‘first’, ‘last’, False}, default ‘first’

　　　　first删除重复项并保留第一次出现的项,last删除重复保留最后一条，False就是删除重复、只要不重复的数据

* inplace : boolean, default False

　　　　是直接在原来数据上修改还是保留一个副本

```
keydata.drop_duplicates().count()
```

![](https://img2018.cnblogs.com/blog/1353331/201911/1353331-20191101120133348-936956449.png)

```
keydata.drop_duplicates(keep=False).count()
```

![](https://img2018.cnblogs.com/blog/1353331/201911/1353331-20191101120150275-1535932518.png)

### 补充提取重复数据

```
# 剔除重复的数据
data1=keydata.drop_duplicates(keep=False)
data1.count()
```

```
#至少保留一条
data2=keydata.drop_duplicates(keep="first")
data2.count()
```

```
#这样正常的数据就重复了，重复的数据就只有一条
data1.append(data2).drop_duplicates(keep=False).count()
```

## 2.Series去重

我也是最近才遇到series去重这个场景，比较了一下两种去重的性能比较。

场景如下

sql==>pd.dataframe【数据量为8000rows】==>取出这个df的cust_id字段【series】==>转为list===>下一个sql：'''···where cust_id not in (%s)'''%".".join(list)

方法1：

方法2：seiries.drop_duplicates()

![](https://img2018.cnblogs.com/i-beta/1353331/201911/1353331-20191105160741242-1075231202.png)
