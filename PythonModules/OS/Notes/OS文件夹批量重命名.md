python自动化办公之——批量重命名文件夹

# python自动化办公之——批量重命名文件夹

重命名是我们平时操作计算机时经常会用到的操作，如果只是重命名单个文件或者少量文件，完全可以使用windows自带的重命名功能进行操作。但是如果需要对成百上千个文件进行重命名，或者需要**按照一定的规律**对一批文件进行重命名，这时再手动进行操作，就会显得既浪费时间，又影响工作效率。这里同样根据前面的例子，按照一定的规律对文件进行重命名。

**知识点：**实现批量重命名的重点是os.rename()方法，该方法可以对文件进行重命名，要实现批量重命名，仍然需要用到**for循环**和**os.listdir()**来遍历要重命名的所有文件。

**添加前缀、后缀**

 下图为原始文件夹名，我们在其前后加上前缀和后缀。

![](https://fjjwhjwd3p.feishu.cn/space/api/box/stream/download/asynccode/?code=ZGJjMjlhMDg4MDE5MDE1ZjdjNjlhN2RkOTYwZGE2NTlfbXlPNjRvS0xtdU44YXp6TFByY2Z0eU1qVVp1WkhvY3BfVG9rZW46Ym94Y25Id2JoU0NpYzlxMEE4djN2SHdabGZiXzE2NTQ3ODM2MjM6MTY1NDc4NzIyM19WNA)

未重命名前的文件夹

示例代码如下：

import oswhile True:

    path = input('请输入要重命名的文件所在路径')

    try:

    list = os.listdir(path)

    num = 0        #记录文件数量

    for i in range(0,len(list)):

    filepath = os.path.join(path,list[i])  #记录遍历到的文件名

    template = '{:0>3d}'  #设置编号格式化为3位

    newfilename = template.format(num+1) +list[i] +'_销售部'  #新文件名格式

    newfilepath = os.path.join(path,newfilename)     #新文件名，包括路径

    os.rename(filepath,newfilepath)   #子文件夹重命名

    num += 1

    print('批量重命名完成，共处理文件' + str(num) + '个')

    except:

    print('请输入一个有效路径')

运行结果如下，已经将文件夹重命名成功：

![](https://fjjwhjwd3p.feishu.cn/space/api/box/stream/download/asynccode/?code=ODhhNjdhYjU5MmIzNDE0Y2VmMDk5NTNjMmY5OWE2ODNfeXVZWlp2Z1psWldjNjYzR3NYRWU3OFRPcW02ZTdJVWtfVG9rZW46Ym94Y25RcWg0Rm1xcWd1NFUxdHNzTnhPMGllXzE2NTQ3ODM2MjM6MTY1NDc4NzIyM19WNA)

重命名后的文件夹
