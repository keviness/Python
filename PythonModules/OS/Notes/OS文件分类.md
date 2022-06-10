python 递归获取子文件夹下的文件名和文件类别标签

[深度学习](https://so.csdn.net/so/search?q=深度学习&spm=1001.2101.3001.7020)中，常常要获取文件夹下文件名和类别，为提取训练数据和测试数据准备

 本文采用的一个文件下的40类数据做实验：

![](https://fjjwhjwd3p.feishu.cn/space/api/box/stream/download/asynccode/?code=MTRhNjIyZmJjNmY2YmI3MWY0MjU3MDQ3MjRkMjYxMWRfbDlXZ0ROVkNSQjVtaDB1UFloRzJPVlpOUzduaThyV2RfVG9rZW46Ym94Y241Ymk1a1RHa0dtQm1VMUJVcVZIYzBlXzE2NTQ3ODE4MjI6MTY1NDc4NTQyMl9WNA)

 最后保存成如下文件形式： 文件路径+文件名+类别标签

![](https://fjjwhjwd3p.feishu.cn/space/api/box/stream/download/asynccode/?code=N2VjOTYyZmQ4MjA3OGU3NzAzYjBkODk2MDFmYmFlMDJfNGtFZDV1WEJuVkJVcHdqbnVFNlVWRnJvaGdMRjgxbUxfVG9rZW46Ym94Y25IeDNsbnh5SE5RZlh6N1FDYjBjb1JlXzE2NTQ3ODE4MjI6MTY1NDc4NTQyMl9WNA)

 具体代码如下：

```Python
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:51:04 2020

filenameToCSV

@author: administration
"""
import os
import re

allpath=[]
allname=[]

#获取文件列表
def getallfile(path):
    allfilelist=os.listdir(path)
    # 遍历该文件夹下的所有目录或者文件
    for file in allfilelist:
        filepath=os.path.join(path,file)
        # 如果是文件夹，递归调用函数
        if os.path.isdir(filepath):
            getallfile(filepath)
        # 如果不是文件夹，保存文件路径及文件名
        elif os.path.isfile(filepath):
            allpath.append(filepath)
            allname.append(file)
    return allpath, allname


def Test():
    path="F:/project/2020/vs_project_2020/face_recog_opencv/source/facesdata/" #文件夹
    outfile="save.txt"#保存文件名
 
    file = open(outfile,"w")
    if not file:
        print ("cannot open the file %s for writing" % outfile)

    allpath, allname = getallfile(path) #获取文件目录 + 文件名
  
    for name in allpath:
      
        st =re.findall(".*a/s(.*)\.*",name)  #正则化匹配类别位置，获取图像类别
        st = ''.join(st)
        loc = st.split("\\")
        loc = ''.join(loc[0])#图像类别
        #print(loc)
        file.write(name+";" + loc)#写入文件中
        if name != allpath[-1]:   #最后一行不回车
            file.write("
")
      
    file.close()

Test()
```

其中正则化提取图像的类别根据自己的需要进行修改即可
