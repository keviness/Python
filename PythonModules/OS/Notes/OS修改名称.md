文件名（文件夹名） 排序： 按字符串排序、 按数字排序 Python

# 文件夹名 排序

如下图，获取Data路径下的文件夹名，并排序

![](https://fjjwhjwd3p.feishu.cn/space/api/box/stream/download/asynccode/?code=OWE5ZjE2NGRkNjE5NTQyMDMyODk3ZDZlODRiYTgyMWJfaGMzUEI3ZnNRRGtDZ1BNZU9ma1BSZmR2Z1hyZVdXMzBfVG9rZW46Ym94Y25lcUdtbVN3VTNGV2pmcEw5TVBYaVFiXzE2NTQ0NDUzMzU6MTY1NDQ0ODkzNV9WNA)

具体实现如下：

```Plain%20Text
import os


''' 获取 文件夹名 列表 '''
path1 = './Data/'
file_list = next(os.walk(path1))[1]


''' 文件夹名 排序 '''
# 文件夹名 按字符串排序
file_list.sort()
print(file_list)
# ['file1', 'file101', 'file102', 'file103', 'file11', 'file12',
# 'file13', 'file2', 'file21', 'file22', 'file23', 'file3']

# 文件夹名 按数字排序
file_list.sort(key=lambda x: int(x[4:]))
print(file_list)
# ['file1', 'file2', 'file3', 'file11', 'file12', 'file13',
# 'file21', 'file22', 'file23', 'file101', 'file102', 'file103']
```

# 文件名 排序

如下图，获取file1文件夹下的文件名，并排序

![](https://fjjwhjwd3p.feishu.cn/space/api/box/stream/download/asynccode/?code=ZmU0NWUwNmQ2NzUyOTEwZjNhNmZhNWZlOWVkMmE3ODlfem5NZW1rUFhYNkZnWXpRM05nWW84TVhzZE8wVzVnODVfVG9rZW46Ym94Y253SGxXRmkxVVVqR25mSTR0ZnYwTzlqXzE2NTQ0NDUzMzU6MTY1NDQ0ODkzNV9WNA)

具体实现如下：

```Plain%20Text
import os

''' 获取 文件名 列表 '''
path2 = './Data/file1/'
test_list = next(os.walk(path2))[2]

''' 文件名 排序 '''
# 文件名 按字符串排序
test_list.sort()
print(test_list)
# ['test001_1.txt', 'test001_101.txt', 'test001_102.txt', 'test001_103.txt', 'test001_11.txt',
# 'test001_12.txt', 'test001_13.txt', 'test001_2.txt', 'test001_21.txt', 'test001_22.txt',
# 'test001_23.txt', 'test001_3.txt', 'test001_31.txt', 'test001_32.txt', 'test001_33.txt']

# 文件名 按数字排序
test_list.sort(key=lambda x: int(x.split('_')[1][:-4]))
print(test_list)
# ['test001_1.txt', 'test001_2.txt', 'test001_3.txt', 'test001_11.txt', 'test001_12.txt',
# 'test001_13.txt', 'test001_21.txt', 'test001_22.txt', 'test001_23.txt', 'test001_31.txt',
# 'test001_32.txt', 'test001_33.txt', 'test001_101.txt', 'test001_102.txt', 'test001_103.txt']
```

***附 1：***

## 列表元素 逆序排序

list**.reverse() # **可直接在原来的列表里面将元素进行***逆序排列***，不需要创建新的副本用于存储结果。

## 按文件名[字符串](https://so.csdn.net/so/search?q=字符串&spm=1001.2101.3001.7020)小写排序

list.sort(key=lambda x: x.lower())

## 按创建时间排序

```Plain%20Text
list.sort(key=lambda x: os.path.getctime(x))  # 精确到秒
```

或

```Plain%20Text
list.sort(key=lambda x: os.stat(x).st_ctime_ns)  # 精确到纳秒
```

***附 2：***

## 随机排序 列表/序列 元素

```Plain%20Text
import random

list = …

random.shuffle(list)
```
