# Python的GUI图形界面工具大全

总结了一下Python下的图形界面GUI工具，暂时能找到的资料就这么多，后续会补充推荐学习资料。

## **图形界面的定义**

> [图形界面](https://link.zhihu.com/?target=https%3A//baike.baidu.com/item/GUI/479966%3Ffromtitle%3D%25E5%259B%25BE%25E5%25BD%25A2%25E7%2594%25A8%25E6%2588%25B7%25E7%2595%258C%25E9%259D%25A2%26fromid%3D3352324)
> 图形用户界面（Graphical User Interface，简称 GUI，又称图形用户接口）是指采用图形方式显示的计算机操作用户界面。图形用户界面是一种人与计算机通信的界面显示格式，允许用户使用鼠标等输入设备操纵屏幕上的图标或菜单选项，以选择命令、调用文件、启动程序或执行其它一些日常任务。

说人话就是你拿鼠标箭头点来点去的界面，点开计算器图标就跳出个计算器等。

## **Python的GUI工具**

Python作为一个容易上手，简单方便的编程语言，第三方的优秀工具数不胜数，在GUI这个方向同样是有很多的工具可以使用，比较常用的工具无非是 **Tkinter** 、 **wxWidgets** 、 **Qt** 、 **Gtk** +、 **Kivy** 、**FLTK** 和 **OpenGL**这几个，但是除了这几个之外还有不少的工具。接下来我会按照常用工具，跨浏览器工具，跨平台工具，特定平台工具和GUI设计工具进行分类，进行一个全面的介绍，这篇文章主要参考维基百科和各个平台的相关介绍。

在介绍GUI工具之前，我觉得对于大多数人来说，我其实是推荐把数据分析当做一个方向来学的，首先python的优势就在**数据处理分析**与 **人工智能** 。

人工智能的从业门槛很高，自学基本上属于纯玩，性价比不高。

数据分析处理，我觉得是未来各行各业都可能碰到的问题，虽然现在有很多自动化数据处理工具，但是毕竟通用的场景并不多，而那些熟悉某个特定行业领域+数据处理能力的复合型人才就相对可能更吃香。

这里有一门知乎出品的数据处理精品课程，对于在本职工作之外想要学习一门实用技能的同学，建议免费体验一下，记住，那这个找工作很难，属于锦上添花的技能。

[![](https://pic3.zhimg.com/v2-840e50b732c458a138350738922da9ee_720w.jpg?source=b555e01d)训练营知乎数据分析3天实战训练营「开课」-0704作者 知乎研职在线**¥0.10**去查看](https://api.zhihu.com/poisson-marketing/recommendation/url/97ab0cb85be5bebb6c0634f263a68f26)

## **最常用的GUI工具**

### **Tkinter**

 **主页链接** ：[https://**docs.python.org/3/libra**ry/tk.html](https://link.zhihu.com/?target=https%3A//docs.python.org/3/library/tk.html)

 **简介** ：Tkinter Python 的标准 Tk GUI 工具包的接口，可以在大多数的 Unix 平台下使用, 同样可以应用在 Windows 和 Mac 系统里。Tk8.0 的后续版本可以实现本地窗口风格,并良好地运行在绝大多数平台中。

![](https://pic3.zhimg.com/80/v2-ef8962edfa764336a171c7c168b1acee_1440w.jpg)

 **优点** ：是python的内置库，无需额外下载，不存在兼容问题，且又非常详细的说明文档。

 **缺点** ：实现效果较为普通

### **wxPython**

 **主页链接** ：[https://www.**wxpython.org**](https://link.zhihu.com/?target=https%3A//www.wxpython.org)

 **简介** ：wxPython是一个创建桌面GUI应用的跨平台工具包(toolkit)，它的主要开发者是Robin Dunn。使用wxPython，开发者可以在Windows、Mac和多种Unix系统上开发应用程序。

![](https://pic1.zhimg.com/80/v2-9b47894dd14ad1f67cd086eb8fd853d8_1440w.jpg)

 **优点** ：是一个免费的，可移植的GUI类库，用C++编写，可在Windows，Mac OS X，GTK，X11等许多平台上使用。可用于多种语言，包括Python，Perl，Ruby等。

 **缺点** ：设计的界面美观程度和灵活性较为普通

### **PyQT**

 **主页链接** ：[https://**docs.python.org/3/libra**ry/tk.html](https://link.zhihu.com/?target=https%3A//docs.python.org/3/library/tk.html)

 **简介** ：PyQt是Qt框架的Python语言实现，由Riverbank Computing开发，是最强大的GUI库之一。 PyQt提供了一个设计良好的窗口控件集合，每一个PyQt控件都对应一个Qt控件，因此PyQt的API接口与Qt的API接口很接近，但PyQt不再使用QMake系统和Q_OBJECT宏。

![](https://pic4.zhimg.com/80/v2-8451498077c7066056c3b09ff166d1e3_1440w.jpg)

 **优点** ：功能非常强大，可以用PyQt5开很漂亮的界面；另外它支持可视化界面设计，对新手非常友好。什么意思呢，就是你可以通过拖动一些模块就可以完成一些代码才能完成的工作，就跟C++的QT是一样的。

![](https://pic2.zhimg.com/80/v2-91ce47761d86f5e389e9f04380b59ecd_1440w.jpg)

 **缺点** ：学习起来有一定难度。

### **PyGtk**

 **主页链接** ：[https://**docs.python.org/3/libra**ry/tk.html](https://link.zhihu.com/?target=https%3A//docs.python.org/3/library/tk.html)

![](https://pic3.zhimg.com/80/v2-e0d412df1b15f9b8c2dafcdd3b218d22_1440w.jpg)

 **优点** ：跟PyQt一样，可以实现很不错的效果，但是稍逊于PyQt，并且同样有UI设计工具Glade

![](https://pic1.zhimg.com/80/v2-7fb6b0a6462b3a3395e147ef7a252e9c_1440w.jpg)

 **缺点** ：更适合GNOME平台。

### **Kivy**

 **主页链接** ：[https://**kivy.org/#**home](https://link.zhihu.com/?target=https%3A//kivy.org/%23home)

![](https://pic4.zhimg.com/80/v2-011e450ec79278f4cacdf6ff62aa39ab_1440w.jpg)

 **优点** ：Kivy 是一个开源的 Python 框架，用于快速开发应用，实现各种当前流行的用户界面，比如多点触摸等等。 Kivy 可以运行于 Windows， Linux， MacOS， Android， iOS 等当前绝大部分主流桌面/移动端操作系统。 Kivy 基于 Python，界面文件和程序文件相互分离的设计思路，设计简洁优雅，语法易学，适合新人入门。

 **缺点** ：缺点只有一个中文文档还是特别全面，大多数教程还是英文版本。

 **推荐学习资料** ：

[Kivy中文教程](https://link.zhihu.com/?target=https%3A//cycleuser.gitbooks.io/kivy-guide-chinese/content/)

[Github Kivy项目](https://link.zhihu.com/?target=https%3A//github.com/topics/kivy-application)

### **FLTK**

 **主页链接** ：[https://**pyfltk.sourceforge.io/**](https://link.zhihu.com/?target=https%3A//pyfltk.sourceforge.io/)

![](https://pic3.zhimg.com/80/v2-26671e87619445842eeb989a86718f02_1440w.jpg)

 **优点** ：一个致力于跨平台，快速开发，轻量化和容易使用的python GUI工具。

 **缺点** ：中文资料极为罕见。

### **OpenGL**

 **主页链接** ：[https://**pypi.org/project/PyOpen**GL/](https://link.zhihu.com/?target=https%3A//pypi.org/project/PyOpenGL/)

 **简介** ：OpenGL 是 Open Graphics Library 的简写，意为“开放式图形库”，是用于渲染 2D、3D 矢量图形的跨语言、跨平台的应用程序编程接口（API）。OpenGL 不是一个独立的平台，因此，它需要借助于一种编程语言才能被使用。C / C++ / python / java 都可以很好支持 OpengGL。

![](https://pic3.zhimg.com/80/v2-38e0b4389a4c0a12c34808c38210b042_1440w.jpg)

 **优点** ：功能极为强大，几乎可以做出任何2D，3D图形。

 **缺点** ：学习难度较高，适合具有刚需的同学

### **DearPyGui**

 **主页链接** ：[https://**lawsie.github.io/guizer**o/](https://link.zhihu.com/?target=https%3A//lawsie.github.io/guizero/)

![](https://pic1.zhimg.com/80/v2-d94a07eaee252858e9c586a937d92cac_1440w.jpg)

### **PySimpleGUI**

 **主页链接** ：[https://**pysimplegui.readthedocs.io**/en/latest/](https://link.zhihu.com/?target=https%3A//pysimplegui.readthedocs.io/en/latest/)

![]()

### **Guietta**

 **主页链接** ：[https://**guietta.readthedocs.io/**en/stable/](https://link.zhihu.com/?target=https%3A//guietta.readthedocs.io/en/stable/)

这个是一个我觉得很优美的实现简单GUI的框架，推荐，不过中文文档很少。

![]()

### **PyGame**

 **主页链接** ：[https://www.**pygame.org/news**](https://link.zhihu.com/?target=https%3A//www.pygame.org/news)

![]()

 **资源推荐** ：[https://www.**zhihu.com/question/2596**0850/answer/330772593](https://www.zhihu.com/question/25960850/answer/330772593)

Python是一种非常有趣且有益的语言，我认为只要找到合适的动机，任何人都可以熟练掌握它。但是要记住的是，如果你只想着凭借python去找一份工作的话，不是不行，但是很难。python这种语言更适合已经有一份工作的人，多学一个技能。

如果你能坚持看到这里，那么就去学吧，去学不被定义的python，从最简单也是最直观的数据分析学起来吧，并且试着从知乎出品的数据分析课开始吧。

[![](https://pic3.zhimg.com/v2-840e50b732c458a138350738922da9ee_720w.jpg?source=b555e01d)训练营知乎数据分析3天实战训练营「开课」-0704作者 知乎研职在线**¥0.10**去查看](https://api.zhihu.com/poisson-marketing/recommendation/url/a5751812c88887a3f99e820814340869)

编辑于 2022-06-02 05:04

「真诚赞赏，手留余香」

赞赏

还没有人赞赏，快来当第一个赞赏的人吧！

[Python](https://www.zhihu.com/topic/19552832)

[编程](https://www.zhihu.com/topic/19554298)

[GUI设计](https://www.zhihu.com/topic/19703816)

赞同 35122 条评论分享

喜欢收藏
