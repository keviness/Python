# 详解pandas的read_csv方法

使用pandas做数据处理的第一步就是读取数据，数据源可以来自于各种地方，csv文件便是其中之一。而读取csv文件，pandas也提供了非常强力的支持，参数有 **四五十个** 。这些参数中，有的很容易被忽略，但是在实际工作中却用处很大。比如：

> **文件读取时设置某些列为时间类型**
> **导入文件, 含有重复列**
> **过滤某些列**
> **每次迭代指定的行数**
> **值替换**

pandas在读取csv文件是通过read_csv这个函数读取的，下面就来看看这个函数都支持哪些不同的参数。

**以下代码都在jupyter notebook上运行！**

**一、基本参数**

1、 **filepath_or_buffer：** 数据输入的路径：可以是文件路径、可以是URL，也可以是实现read方法的任意对象。这个参数，就是我们输入的第一个参数。

```text
import pandas as pd
pd.read_csv("girl.csv")

# 还可以是一个URL，如果访问该URL会返回一个文件的话，那么pandas的read_csv函数会自动将
该文件进行读取。比如：我们用fastapi写一个服务，将刚才的文件返回。
pd.read_csv("http://localhost/girl.csv")

# 里面还可以是一个 _io.TextIOWrapper，比如：
f = open("girl.csv", encoding="utf-8")
pd.read_csv(f)
```

![](https://pic1.zhimg.com/80/v2-3ea174ddf38cf8619db4d10db2b81d2c_1440w.jpg) **2、sep：** 读取csv文件时指定的分隔符，默认为逗号。注意："csv文件的分隔符" 和 "我们读取csv文件时指定的分隔符" 一定要一致。

```python3
pd.read_csv("girl.csv")
```

![](https://pic1.zhimg.com/80/v2-1c532d49e1019a940a0685dd916af21c_1440w.jpg)由于指定的分隔符 和 csv文件采用的分隔符 不一致，因此多个列之间没有分开，而是连在一起了。 所以，我们需要将分隔符设置成"\t"才可以。

```text
pd.read_csv('girl.csv', sep='\t')
```

![](https://pic1.zhimg.com/80/v2-3ea174ddf38cf8619db4d10db2b81d2c_1440w.jpg) **3、delimiter ：** 分隔符的另一个名字，与 sep 功能相似。

**4、delim_whitespace ：** 默认为 False，设置为 True 时，表示分割符为空白字符，可以是空格、"\t"等等。不管分隔符是什么，只要是空白字符，那么可以通过delim_whitespace=True进行读取。

```text
pd.read_csv('girl.csv',delim_whitespace=True)
```

![](https://pic1.zhimg.com/80/v2-3ea174ddf38cf8619db4d10db2b81d2c_1440w.jpg) **5、header：** 设置导入 DataFrame 的列名称，默认为 "infer"，注意它与下面介绍的 names 参数的微妙关系。

**6、names：** 当names没被赋值时，header会变成0，即选取数据文件的第一行作为列名；当 names 被赋值，header 没被赋值时，那么header会变成None。如果都赋值，就会实现两个参数的组合功能。

*举个栗子：*

1) names 没有被赋值，header 也没赋值：

```text
# 这种情况下，header为0，即选取文件的第一行作为表头
pd.read_csv('girl.csv',delim_whitespace=True)
```

![](https://pic1.zhimg.com/80/v2-3ea174ddf38cf8619db4d10db2b81d2c_1440w.jpg)2) names 没有被赋值，header 被赋值：

```python3
# 不指定names，指定header为1，则选取第二行当做表头，第二行下面为数据
pd.read_csv('girl.csv',delim_whitespace=True, header=1)
```

![](https://pic2.zhimg.com/80/v2-756db88dd3b80bef96a4f5cf471520f1_1440w.jpg)

3) names 被赋值，header 没有被赋值：

```python
pd.read_csv('girl.csv', delim_whitespace=True, names=["编号", "姓名", "地址", "日期"])
```

![img](https://pic3.zhimg.com/80/v2-7eafe4f10c2400cf692064f77c562d5e_1440w.jpg)

可以看到，names适用于没有表头的情况，指定names没有指定header，那么header相当于None。

> 一般来说，读取文件的时候会有一个表头，一般默认是第一行，但是有的文件中是没有表头的，那么这个时候就可以通过names手动指定、或者生成表头，而文件里面的数据则全部是内容。所以这里id、name、address、date也当成是一条记录了，本来它是表头的，但是我们指定了names，所以它就变成数据了，表头是我们在names里面指定的。

4) names和header都被赋值：

```text
pd.read_csv('girl.csv', delim_whitespace=True, names=["编号", "姓名", "地址", "日期"], header=0)
```

![](https://pic3.zhimg.com/80/v2-372a5d4afe65f7eae5848c0a9084a972_1440w.jpg)> 这个时候，相当于先不看names，只看header，header为0代表先把第一行当做表头，下面的当成数据；然后再把表头用names给替换掉。

***所以names和header的使用场景主要如下：***

> 1. csv文件有表头并且是第一行，那么names和header都无需指定;
> 2. csv文件有表头、但表头不是第一行，可能从下面几行开始才是真正的表头和数据，这个时候指定header即可;
> 3. csv文件没有表头，全部是纯数据，那么我们可以通过names手动生成表头;
> 4. csv文件有表头、但是这个表头你不想用，这个时候同时指定names和header。先用header选出表头和数据，然后再用names将表头替换掉，就等价于将数据读取进来之后再对列名进行rename；

**7、index_col：** 我们在读取文件之后所得到的DataFrame的索引默认是0、1、2……，我们可以通过set_index设定索引，但是也可以在读取的时候就指定某列为索引。

```text
pd.read_csv('girl.csv', delim_whitespace=True, index_col="name")
```

![](https://pic4.zhimg.com/80/v2-e16fbade997d4da1f01297d54c8dd057_1440w.jpg)> 这里，我们在读取的时候指定了name列作为索引；

> 此外，除了指定单个列，还可以指定多列作为索引，比如["id", "name"]。同时，我们除了可以输入列名外，还可以输入列对应的索引。比如："id"、"name"、"address"、"date"对应的索引就分别是0、1、2、3。

**8、usecols：** 如果一个数据集中有很多列，但是我们在读取的时候只想要使用到的列，我们就可以使用这个参数。

```text
pd.read_csv('girl.csv', delim_whitespace=True, usecols=["name", "address"])
```

![](https://pic2.zhimg.com/80/v2-f72979fc1d502fe9acd2e7c801fdf729_1440w.png) 

**9、mangle_dupe_cols：** 在实际工作中，我们得到的数据会很复杂，有时导入的数据会含有名字相同的列。参数 mangle_dupe_cols 会将重名的列后面多一个 .1，该参数默认为 True，如果设置为 False，会抛出不支持的异常：

```text
# ValueError: Setting mangle_dupe_cols=False is not supported yet
```

**10、prefix：** 当导入的数据没有 header 时，设置此参数会自动加一个前缀。比如：

```python3
pd.read_csv('girl.csv', delim_whitespace=True, header=None, prefix="夏色祭")
```

![](https://pic2.zhimg.com/80/v2-e28ff626338d395d66977142d5cf1bfd_1440w.jpg)

**二、通用解析参数**

**1、dtype：** 在读取数据的时候，设定字段的类型。比如，公司员工的id一般是：00001234，如果默认读取的时候，会显示为1234，所以这个时候要把他转为**字符串**类型，才能正常显示为00001234：

```text
df = pd.read_csv('girl.csv', delim_whitespace=True)
df = pd.read_csv('girl.csv', delim_whitespace=True, dtype={"id": str})
df
```

![](https://pic2.zhimg.com/80/v2-1f8ffd4d015e3b2c9fedfdbea61699ed_1440w.jpg)![](https://pic4.zhimg.com/80/v2-2cd6b8439ef6605cf15ed25c78f965bb_1440w.jpg) **2、engine：** pandas解析数据时用的引擎，目前解析引擎有两种：c、python。默认为 c，因为 c 引擎解析速度更快，但是特性没有 python 引擎全。如果使用 c 引擎没有的特性时，会自动退化为 python 引擎。

比如使用分隔符进行解析，如果指定分隔符不是单个字符、或者 `"\s+"`，那么c引擎就无法解析了。我们知道如果分隔符为空白字符的话，那么可以指定 `delim_whitespace=True`，但是也可以指定sep=r"\s+"。

```text
pd.read_csv('girl.csv', sep=r"\s+")
```

![](https://pic1.zhimg.com/80/v2-3ea174ddf38cf8619db4d10db2b81d2c_1440w.jpg)

如果sep是单个字符，或者字符串\s+，那么C是可以解决的。但如果我们指定的sep比较复杂，这时候引擎就会退化。

```text
# 我们指定的\s{0}相当于没指定，\s+\s{0}在结果上等同于\s+。
# 但是它不是单个字符，也不是\s+，因此此时的C引擎就无法解决了，而是会退化为python引擎
pd.read_csv('girl.csv', sep=r"\s+\s{0}", encoding="utf-8")
```

![](https://pic4.zhimg.com/80/v2-c9a70eaa4042002b5a1ddd7ff9c226bf_1440w.jpg)此时我们可以看到弹出了警告，这个时候需要手动指定engine="python"来避免警告。这里面还用到了encoding参数，因为引擎一旦退化，在Windows上会读出乱码，所以要进行设定。

**3、converters：** 在读取数据的时候对列数据进行变换，例如将id增加10，但是注意 int(x)，在使用converters参数时，解析器默认所有列的类型为 str，所以需要进行类型转换。

```text
pd.read_csv('girl.csv', sep="\t", converters={"id": lambda x: int(x) + 10})
```

![](https://pic2.zhimg.com/80/v2-fa254a79fe1fdd29cd71a2f4177ffa75_1440w.jpg) **4、true_values和false_value：** 指定哪些值应该被清洗为True，哪些值被清洗为False。这里增加一个字段：result。

![](https://pic1.zhimg.com/80/v2-77d50d504c065238c859a54edf1d0fd8_1440w.jpg)

```text
pd.read_csv('girl.csv', sep="\t", true_values=["对"], false_values=["错"])
```

![](https://pic2.zhimg.com/80/v2-8078733f1808085987d9b92473d5c549_1440w.jpg)

```text
pd.read_csv('girl.csv', sep="\t", false_values=["错"])
```

![](https://pic3.zhimg.com/80/v2-5d21b827a801a8946bf500ea7e5f487a_1440w.jpg)

```text
pd.read_csv('girl.csv', sep="\t",  false_values=["错", "对"])
```

![](https://pic1.zhimg.com/80/v2-2ab438de81d8d5d81be957a4d7c97948_1440w.jpg)

> 这里的替换规则为，只有当某一列的数据类别全部出现在 `true_values + false_values`里面，才会被替换。

> 我们看到"错"并没有被替换成False，原因就是result字段中只有"错"这个类别的值在 `true_values + false_values`中，而"对"并没有出现，所以不会替换。
> 而最后的对、错都出现在了 `<b>true_values + false_values</b>`中，所以全部被替换。

**5、skiprows：** 表示过滤行，想过滤掉哪些行，就写在一个列表里面传递给skiprows即可。注意的是：这里是先过滤，然后再确定表头，比如：

```text
pd.read_csv('girl.csv', sep="\t", skiprows=[0])
```

![](https://pic3.zhimg.com/80/v2-fbc3d666ca6eab1c15f7524620bac48e_1440w.jpg)

> 这里把第一行过滤掉了，因为第一行是表头，所以在过滤掉之后第二行就变成表头了。

> 当然里面除了传入具体的数值，来表明要过滤掉哪些行，还可以传入一个函数。

```text
pd.read_csv('girl.csv', sep="\t", skiprows=lambda x: x > 0 and x % 2 == 0)
```

![](https://pic1.zhimg.com/80/v2-4ec696d72c767b9807c968245f3327a4_1440w.jpg)

> 由于索引从0开始，所以凡是索引大于0、并且%2等于0的记录都过滤掉。索引大于0，是为了保证表头不被过滤掉。

**6、skipfooter：** 从文件末尾过滤行，解析引擎退化为 Python。这是因为 C 解析引擎没有这个特性。

```text
pd.read_csv('girl.csv', sep="\t", skipfooter=3, encoding="utf-8", engine="python")
```

![img](https://pic1.zhimg.com/80/v2-914cbb15f1cc51690ac968aff1281e88_1440w.jpg)

> skipfooter接收整型，表示从结尾往上过滤掉指定数量的行，因为引擎退化为python，那么要手动指定engine="python"，不然会警告。另外需要指定encoding="utf-8"，因为csv存在编码问题，当引擎退化为python的时候，在Windows上读取会乱码。

**7、nrows：** 设置一次性读入的文件行数，在读入大文件时很有用，比如 16G 内存的PC无法容纳几百 G 的大文件。

```text
 pd.read_csv('girl.csv', sep="\t", nrows=1)
```

![](https://pic1.zhimg.com/80/v2-afe529bfa165370419f461746a438564_1440w.jpg) 

**8、low_memory：** 这个参数看起来是和内存有关，其实它是和数据类型相关的。

我们知道DataFrame的每一列都是有类型的，在读取csv的时候，pandas会根据数据来判断每一列的类型。但pandas主要是靠 **"猜"** 的方法，因为在读取csv的时候是分块读取的，每读取一块的时候，会根据数据来判断每一列是什么类型；然后再读取下一块，会再对类型进行一个判断，得到每一列的类型，如果得到的结果和上一个块得到结果不一样，那么就会发出警告，提示有以下的列存在多种数据类型。

而为了保证正常读取，就会把类型像大的方向兼容，比如第一块的user_id被解析成整型，但是在解析第二个块发现user_id有的值无法解析成整型，那么类型整体就会变成字符串，于是pandas提示该列存在混合类型。而一旦设置low_memory=False，那么pandas在读取csv的时候就不分块读了，而是直接将文件全部读取到内存里面，这样只需要对整体进行一次判断，就能得到每一列的类型。但是这种方式也有缺陷，一旦csv过大，就会内存溢出。

不过从数据库读取就不用担心了，因为数据库是规定了每一列的类型的。如果是从数据库读取得到的DataFrame，那么每一列的数据类型和数据库表中的类型是一致的。之前，我们在上面介绍了dtype，这个是我们手动规定类型，那么pandas就会按照我们规定的类型去解析指定的列，但是一旦无法解析就会报错。

**三、空值处理相关参数**

**na_values：** 该参数可以配置哪些值需要处理成 NaN：

```text
pd.read_csv('girl.csv', sep="\t", na_values=["对", "古明地觉"])
```

![](https://pic2.zhimg.com/80/v2-91293afc6ae18c1a14470eef0b1a7cf1_1440w.jpg)

> 可以看到将"对"和"古明地觉"设置成了NaN，这里的情况是不同的列中包含了不同的值。但如果两个列中包含相同的值，只想将其中一个列的值换成NaN的话，则通过字典实现只对指定的列进行替换。

```text
pd.read_csv('girl.csv', sep="\t", na_values={"name": ["古明地觉", "博丽灵梦"], "result": ["对"]})
```

![](https://pic3.zhimg.com/80/v2-44fdd500ad28404b5b14a188b4309d52_1440w.jpg)

**四、时间处理相关参数**

**1、parse_dates：** 指定某些列为时间类型，这个参数一般搭配date_parser使用。

**2、date_parser：** 是用来配合parse_dates参数的，因为有的列虽然是日期，但没办法直接转化，需要我们指定一个解析格式：

```python3
from datetime import datetime
pd.read_csv('girl.csv', sep="\t", parse_dates=["date"], date_parser=lambda x: datetime.strptime(x, "%Y年%m月%d日"))
```

![](https://pic4.zhimg.com/80/v2-f5b0683e318d8f11b7d9afb974810063_1440w.jpg) 

**3、infer_datetime_format：** infer_datetime_format 参数默认为 False。如果设定为 True 并且 parse_dates 可用，那么 pandas 将尝试转换为日期类型，如果可以转换，转换方法并解析，在某些情况下会快 5~10 倍。

**五、分块读入相关参数**

**1、iterator：** iterator 为 bool类型，默认为False。如果为True，那么返回一个 TextFileReader 对象，以便逐块处理文件。这个在文件很大、内存无法容纳所有数据文件时，可以分批读入，依次处理。

```text
chunk = pd.read_csv('girl.csv', sep="\t", iterator=True)
print(chunk)  
# <pandas.io.parsers.TextFileReader object at 0x000002550189C0A0>

print(chunk.get_chunk(2))
```

![](https://pic3.zhimg.com/80/v2-2e07257bac04ef3f72ead67ddd53a176_1440w.png)

```text
# 文件还剩下三行，但是我们指定读取100，那么也不会报错，不够指定的行数，那么有多少返回多少
print(chunk.get_chunk(100))
```

![](https://pic2.zhimg.com/80/v2-80b98ca6ec58f06ce91b21b8c287f1e9_1440w.png)

```text
try:
    # 但是在读取完毕之后，再读的话就会报错了
    chunk.get_chunk(5)
except StopIteration as e:
    print("读取完毕")
# 读取完毕  
```

**2、chunksize：** 整型，默认为 None，设置文件块的大小。

```text
chunk = pd.read_csv('girl.csv', sep="\t", chunksize=2)
# 还是返回一个类似于迭代器的对象
print(chunk)  
# <pandas.io.parsers.TextFileReader object at 0x0000025501143AF0>

# 调用get_chunk，如果不指定行数，那么就是默认的chunksize
print(chunk.get_chunk())
```

![](https://pic3.zhimg.com/80/v2-bbc07d07dce9be68daf7521ac28a618e_1440w.png)

```text
# 也可以指定
print(chunk.get_chunk(100))
```

![](https://pic2.zhimg.com/80/v2-eb3682a5a1f0c4914839eb9e7cd956d5_1440w.jpg)

```text
try:
    chunk.get_chunk(5)
except StopIteration as e:
    print("读取完毕")
# 读取完毕  
```

> 以上便是pandas的read_csv函数中绝大部分参数了，同时其中的部分参数也适用于读取其它类型的文件。
> 其实在读取csv文件时所使用的参数不多，很多参数平常我们都不会用到的，不过不妨碍我们了解一下，因为在某些特定的场景下它们是可以很方便地帮我们解决一些问题的。个人感觉**分块读取这个参数**最近在工作中提高了很大的效率。
> 上面列到的read_csv函数中的参数并不是全部，有几个还没有介绍到，个人觉得，掌握这些的用法基本已经完全够用，其它有兴趣大家可以自己看一下，也欢迎大家补充。
>
