# Matplotlib figure图形对象

**<** [PyLab模块绘制曲线](http://c.biancheng.net/matplotlib/pylab-module.html)[Matplotlib axes类](http://c.biancheng.net/matplotlib/axes.html) **>**

[C语言中文网推出辅导班啦，包括「C语言辅导班、C++辅导班、算法/数据结构辅导班」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践 + 永久学习。QQ在线，随时响应！](http://fudao.biancheng.net/)

通过前面的学习，我们知道 `matplotlib.pyplot`模块能够快速地生成图像，但如果使用面向对象的编程思想，我们就可以更好地控制和自定义图像。

在 Matplotlib 中，面向对象编程的核心思想是创建图形对象（figure object）。通过图形对象来调用其它的方法和属性，这样有助于我们更好地处理多个画布。在这个过程中，pyplot 负责生成图形对象，并通过该对象来添加一个或多个 axes 对象（即绘图区域）。

Matplotlib 提供了 `matplotlib.figure`图形类模块，它包含了创建图形对象的方法。通过调用 pyplot 模块中 figure() 函数来实例化 figure 对象。如下所示：

<pre class="python sh_python snippet-formatted sh_sourceCode"><ol class="snippet-num"><li><p><span class="sh_preproc">from</span> matplotlib <span class="sh_preproc">import</span> pyplot as plt</p></li><li data-node-id="20211128235838-8i3ghdp"><p><span class="sh_comment">#创建图形对象</span></p></li><li><p>fig <span class="sh_symbol">=</span> plt<span class="sh_symbol">.</span><span class="sh_function">figure</span><span class="sh_symbol">()</span></p></li></ol></pre>

该函数的参数值，如下所示：

| 参数      | 说明                                                   |
| --------- | ------------------------------------------------------ |
| figsize   | 指定画布的大小，(宽度,高度)，单位为英寸。              |
| dpi       | 指定绘图对象的分辨率，即每英寸多少个像素，默认值为80。 |
| facecolor | 背景颜色。                                             |
| dgecolor  | 边框颜色。                                             |
| frameon   | 是否显示边框。                                         |

下面使用 figure() 创建一个空白画布：
fig = plt.figure()

我们使用 add_axes() 将 axes 轴域添加到画布中。如下所示：
ax=fig.add_axes([0,0,1,1])

add_axes() 的参数值是一个序列，序列中的 4 个数字分别对应图形的左侧，底部，宽度，和高度，且每个数字必须介于 0 到 1 之间。

设置 x 和 y 轴的标签以及标题，如下所示：

<pre class="python sh_python snippet-formatted sh_sourceCode"><ol class="snippet-num"><li><p>ax<span class="sh_symbol">.</span><span class="sh_function">set_title</span><span class="sh_symbol">(</span><span class="sh_string">"sine wave"</span><span class="sh_symbol">)</span></p></li><li data-node-id="20211128235838-cdh1lqx"><p>ax<span class="sh_symbol">.</span><span class="sh_function">set_xlabel</span><span class="sh_symbol">(</span><span class="sh_string">'angle'</span><span class="sh_symbol">)</span></p></li><li><p>ax<span class="sh_symbol">.</span><span class="sh_function">set_ylabel</span><span class="sh_symbol">(</span><span class="sh_string">'sine'</span><span class="sh_symbol">)</span></p></li></ol></pre>

调用 axes 对象的 plot() 方法，对 x 、 y 数组进行绘图操作：
ax.plot(x,y)

完整的代码如下所示：

<pre class="python sh_python snippet-formatted sh_sourceCode"><ol class="snippet-num"><li><p><span class="sh_preproc">from</span> matplotlib <span class="sh_preproc">import</span> pyplot as plt</p></li><li data-node-id="20211128235838-3pjkdfq"><p><span class="sh_preproc">import</span> numpy as np</p></li><li><p><span class="sh_preproc">import</span> math</p></li><li data-node-id="20211128235838-44j6zf3"><p>x <span class="sh_symbol">=</span> np<span class="sh_symbol">.</span><span class="sh_function">arange</span><span class="sh_symbol">(</span><span class="sh_number">0</span><span class="sh_symbol">,</span> math<span class="sh_symbol">.</span>pi<span class="sh_symbol">*</span><span class="sh_number">2</span><span class="sh_symbol">,</span> <span class="sh_number">0.05</span><span class="sh_symbol">)</span></p></li><li><p>y <span class="sh_symbol">=</span> np<span class="sh_symbol">.</span><span class="sh_function">sin</span><span class="sh_symbol">(</span>x<span class="sh_symbol">)</span></p></li><li data-node-id="20211128235838-vp3lngl"><p>fig <span class="sh_symbol">=</span> plt<span class="sh_symbol">.</span><span class="sh_function">figure</span><span class="sh_symbol">()</span></p></li><li><p>ax <span class="sh_symbol">=</span> fig<span class="sh_symbol">.</span><span class="sh_function">add_axes</span><span class="sh_symbol">([</span><span class="sh_number">0</span><span class="sh_symbol">,</span><span class="sh_number">0</span><span class="sh_symbol">,</span><span class="sh_number">1</span><span class="sh_symbol">,</span><span class="sh_number">1</span><span class="sh_symbol">])</span></p></li><li data-node-id="20211128235838-nlgj4wy"><p>ax<span class="sh_symbol">.</span><span class="sh_function">plot</span><span class="sh_symbol">(</span>x<span class="sh_symbol">,</span>y<span class="sh_symbol">)</span></p></li><li><p>ax<span class="sh_symbol">.</span><span class="sh_function">set_title</span><span class="sh_symbol">(</span><span class="sh_string">"sine wave"</span><span class="sh_symbol">)</span></p></li><li data-node-id="20211128235838-fojf9qn"><p>ax<span class="sh_symbol">.</span><span class="sh_function">set_xlabel</span><span class="sh_symbol">(</span><span class="sh_string">'angle'</span><span class="sh_symbol">)</span></p></li><li><p>ax<span class="sh_symbol">.</span><span class="sh_function">set_ylabel</span><span class="sh_symbol">(</span><span class="sh_string">'sine'</span><span class="sh_symbol">)</span></p></li><li data-node-id="20211128235838-4gvv50a"><p>plt<span class="sh_symbol">.</span><span class="sh_function">show</span><span class="sh_symbol">()</span></p></li></ol></pre>

输出结果如下：

![面向对象接口matplotlib](http://c.biancheng.net/uploads/allimg/210906/1533434O9-0.gif)
图1：运行结果图

在 Jupyter Notebook 中运行程序，结果如下：

![面向对象接口matplotlib](http://c.biancheng.net/uploads/allimg/210906/1533433500-1.gif)
