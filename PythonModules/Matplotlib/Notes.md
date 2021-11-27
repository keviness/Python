# Matplotlib.pyplot接口汇总

**<** [Matplotlib下载和安装](http://c.biancheng.net/matplotlib/download-and-install.html)[第一个绘图程序](http://c.biancheng.net/matplotlib/the-first-plot.html) **>**

[C语言中文网推出辅导班啦，包括「C语言辅导班、C++辅导班、算法/数据结构辅导班」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践 + 永久学习。QQ在线，随时响应！](http://fudao.biancheng.net/)

Matplotlib 中的 pyplot 模块是一个类似命令风格的函数集合，这使得 Matplotlib 的工作模式和 MATLAB 相似。

pyplot 模块提供了可以用来绘图的各种函数，比如创建一个画布，在画布中创建一个绘图区域，或是在绘图区域添加一些线、标签等。以下表格对这些函数做了简单地介绍。

## 绘图类型

| 函数名称         | 描述                                         |
| ---------------- | -------------------------------------------- |
| Bar              | 绘制条形图                                   |
| Barh             | 绘制水平条形图                               |
| Boxplot          | 绘制箱型图                                   |
| Hist             | 绘制直方图                                   |
| his2d            | 绘制2D直方图                                 |
| Pie              | 绘制饼状图                                   |
| Plot             | 在坐标轴上画线或者标记                       |
| Polar            | 绘制极坐标图                                 |
| Scatter          | 绘制x与y的散点图                             |
| Stackplot        | 绘制堆叠图                                   |
| Stem             | 用来绘制二维离散数据绘制（又称为“火柴图”） |
| Step             | 绘制阶梯图                                   |
| Quiver           | 绘制一个二维按箭头                           |

## Image函数

| 函数名称     | 描述                               |
| ------------ | ---------------------------------- |
| Imread       | 从文件中读取图像的数据并形成数组。 |
| Imsave       | 将数组另存为图像文件。             |
| Imshow       | 在数轴区域内显示图像。             |

## Axis函数

| 函数名称        | 描述                          |
| --------------- | ----------------------------- |
| Axes            | 在画布(Figure)中添加轴        |
| Text            | 向轴添加文本                  |
| Title           | 设置当前轴的标题              |
| Xlabel          | 设置x轴标签                   |
| Xlim            | 获取或者设置x轴区间大小       |
| Xscale          | 设置x轴缩放比例               |
| Xticks          | 获取或设置x轴刻标和相应标签   |
| Ylabel          | 设置y轴的标签                 |
| Ylim            | 获取或设置y轴的区间大小       |
| Yscale          | 设置y轴的缩放比例             |
| Yticks          | 获取或设置y轴的刻标和相应标签 |

## Figure函数

| 函数名称        | 描述             |
| --------------- | ---------------- |
| Figtext         | 在画布上添加文本 |
| Figure          | 创建一个新画布   |
| Show            | 显示数字         |
| Savefig         | 保存当前画布     |
| Close           | 关闭画布窗口     |
