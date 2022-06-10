使用python对目录下的文件进行分类

 之前关注了一个公众号“李云景”，推送了一个好玩的代码，使用python对目录下杂乱无章的文件按文件类型分类，如pdf，docx，jpg,刚好复习[NLP](https://so.csdn.net/so/search?q=NLP&spm=1001.2101.3001.7020)学不下去，就去尝试一下，还是有几个小坑，自己的代码技术还是太弱啊，有点扎心。

废话少说，原理很简单，就是先获取当前目录下所有文件名字的列表然后对每个文件提取文件类型，然后将文件放到对应的文件夹去。主要用的库就是os和shutil，shutil是一个用于拷贝文件的库。但是使用他的代码时，我发现，如果类型文件夹已经存在某文件的时候，就会报错，提示已经存在这个文件，所以我在原来文件的基础上修改了一下，每次提取到文件类型时，去文件类型文件夹看看这个文件是否存在，如果存在则跳过，不存在的话再去移动。

代码及注释如下：

```Python
import os,shutil
# shutil模块主要是用于拷贝文件

# 取得当前目录下的文件名称列表
files_list = os.listdir()
# 取得python脚本的名字
# __file__是取得当前脚本路径,如果路径是“\anaconda3\python”这样的格式，则要使用“\\”做切分
py_name = __file__.split('/')[-1]

for file in files_list:
# 如果是文件是当前执行的py脚本，则跳过
if file == py_name:
continue
# 如果当前文件格式不是一个文件如“.”，则跳过
if not os.path.isfile(file):
continue

# 取得当前文件名称的格式，（切分文件名，取最后的列表元素）
file_type = file.split('.')[-1]
# 如果没有某个格式的文件夹，则创建这个文件夹
if not os.path.exists(file_type):
os.mkdir(file_type)

# 获取当前路径
path = os.getcwd()
# 获取分类文件夹路径
subdir = os.path.join(path,'%s'%file_type)
# 进入分类文件夹
os.chdir(subdir)
if os.path.exists(file):
# 如果文件夹存在当前文件，则跳过
continue
else:
# 返回之前文件夹进行归类
os.chdir(path)
# shutil.move(源文件，指定路径):递归移动一个文件
shutil.move(file,file_type)
```

主要是在python进出目录这里花了很长时间，汗颜，乖乖复习NLP去了，希望自己以后可以每天都写点关于python好玩的东西。

参考：

李云景原文：[自动整理分类文件代码](https://mp.weixin.qq.com/s/t3Euza2LaoNOH3ibWNBsJw)

[os操作（1）](https://www.cnblogs.com/mttnor/p/python.html)

[os操作（2）](https://blog.csdn.net/niedongri/article/details/80662158)
