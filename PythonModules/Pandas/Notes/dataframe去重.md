# [pandas dataframe重复数据查看.判断.去重](https://www.cnblogs.com/trotl/p/11876292.html)

本文详解如何使用pandas查看dataframe的重复数据，判断是否重复，以及如何去重

**dataframe数据样本：**

```java
import pandas as pd
df = pd.DataFrame({'name':['苹果','梨','草莓','苹果'], 'price':[7,8,9,8], 'cnt':[3,4,5,4]})

   name	cnt	price
0	苹果	 3	7
1	 梨	 4	 8
2	草莓	 5	9
3	苹果	 6	8
```

## >> 查看dataframe的重复数据

```ini
a = df.groupby('price').count()>1
price = a[a['cnt'] == True].index
repeat_df = df[df['price'].isin(price)]
```

## >>duplicated()方法判断

**1. 判断dataframe数据某列是否重复**

```python
flag = df.price.duplicated()

0    False
1    False
2    False
3     True
Name: price, dtype: bool

flag.any()结果为True  (any等于对flag or判断)
flag.all()结果为False  (all等于对flag and判断)
```

**2. 判断dataframe数据整行是否重复**

```makefile
flag = df.duplicated()
判断方法同1
```

**3. 判断dataframe数据多列数据是否重复(多列组合查)**

```sql
df.duplicated(subset = ['price','cnt'])
判断方法同1
```

## >> drop_duplicats()方法去重

**1. 对dataframe数据数据去重**

```python
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)

示例：
df.drop_duplicats(subset = ['price','cnt'],keep='last',inplace=True)

drop_duplicats参数说明：
  参数subset
    subset用来指定特定的列，默认所有列
  参数keep
    keep可以为first和last，表示是选择最前一项还是最后一项保留，默认first
  参数inplace
    inplace是直接在原来数据上修改还是保留一个副本，默认为False
```

### pandas删除重复数据行

在处理pandas数据时，有时候需要删除重复数据，pandas为我们提供了drop_duplicates()函数。下面对其使用方法进行介绍：

##### 1.删除完全重复的行

##### 2.按k1进行去重，对于重复项，保留第一次出现的值

##### 3.按k2和k1两列进行去重

keep：{‘first’, ‘last’, False}, 默认值 ‘first’

* first：保留第一次出现的重复行，删除后面的重复行。
* last：删除前面的重复项，保留最后一次出现的重复行。
* False：删除所有重复项
