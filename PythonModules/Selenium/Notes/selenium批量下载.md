# Python Selenium，让浏览器自动帮你下文献

在做学术、搞科研的过程中，我们往往需要针对一个特定的主题下载海量的文献。在把几百篇文献下载到电脑的过程中，假如遇到不够友好的数据库不提供批量下载的功能，怎么办？我恰好遇到了这样的批量下载的科研任务和批量下载功能受限的数据库网站……

![](https://upload-images.jianshu.io/upload_images/12875160-a9b71e9ece4444ae.png?imageMogr2/auto-orient/strip|imageView2/2/w/1198/format/webp)

做了几天，觉得有点无聊……这个时候，我们多希望自己的浏览器可以变得聪明一点，帮我们完成这个无聊又机械的过程。如何让浏览器替我们搬砖呢？万能的谷歌给我找到了一篇教程[python 批量下载知网(CNKI)论文](http://www.voidcn.com/article/p-skhtfrqg-bpw.html)，嗯，使用python+selenium，就把浏览器调教成我们想要的样子，让它自动帮我们下文献。感谢前人提供巨人的肩膀！在这篇文章、以及这篇文章作者提供的代码的基础上，通过学习和改造，就可以将其适用于外文数据库。这里以Chrome浏览器和SpringLink数据库为例子进行说明。

![](https://upload-images.jianshu.io/upload_images/12875160-394c76620f0976cb.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/440/format/webp)

### 一、需求分析

搞科研很重要的一步就是找文献，其中最基础的工作是先在特定主题词下找到文献。那我们需要浏览器做的事情就清楚了，就是帮我们下文献，特别是海量的文献。

### 二、流程分析

我们知道，在输入主题词后，下载文献的过程重重复复就是那几个步骤：

> 1. 点击下载按钮；
> 2. 开始下载，下载完成；
> 3. 回到列表页面；
> 4. 点击下一个文献，继续下载；
> 5. 完成这一个页面的下载流程后，点击下一页，重复上述过程。

这么简单的流程，为啥不能交给电脑呢？点击下载按钮，实质上就是打开下载链接，那么我们可以将上述过程简化为两步：

> 1. 获取所有下载链接；
> 2. 分别点击每一个下载链接进行下载。

### 三、编程实现

#### 1、Python

编程需要选择一种编程语言，这里我选择的语言是简单、容易上手的Python，本文所有代码均为Python。关于Python的安装、使用和语法规则可以参考[廖雪峰的Python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)；运行环境我用的是jupytor notebook，关于这个可以参考[Jupyter Notebook介绍、安装及使用教程](https://www.jianshu.com/p/91365f343585)。这里都不再进行赘述了，因为我也不怎么懂……

#### 2、Selenium

在开始编程之前，我们需要先了解一个能够自动控制浏览器的工具——Selenium。Selenium是一个用于Web应用程序测试的工具，直接运行在浏览器中，就像真正的用户在操作一样。*（引自：[Selenium百度百科](https://baike.baidu.com/item/selenium/18266)）*

安装和启动，我觉得比较好的、能用的参考资料是[selenium webdriver 启动三大浏览器Firefox,Chrome,IE](https://blog.csdn.net/azsx02/article/details/68947429)、[Python爬虫环境常用库安装](https://blog.csdn.net/qq_29186489/article/details/78581249)等。注意一定要根据自己的浏览器下载浏览器驱动，我用的是Chrome浏览器，需要先看好自己的自己浏览器的版本，具体方法是在导航栏输入[chrome://version/](chrome://version/)，我的版本是70.0.3538。

![](https://upload-images.jianshu.io/upload_images/12875160-d272328ed7717d8c.png?imageMogr2/auto-orient/strip|imageView2/2/w/923/format/webp)

之后进入[http://chromedriver.storage.googleapis.com/index.html](http://chromedriver.storage.googleapis.com/index.html)下载最近版本的chromedriver（[selenium webdriver 启动三大浏览器Firefox,Chrome,IE](https://blog.csdn.net/azsx02/article/details/68947429)这篇文章里的下载链接失效了）。

![](https://upload-images.jianshu.io/upload_images/12875160-93786b2a7244c70f.png?imageMogr2/auto-orient/strip|imageView2/2/w/735/format/webp)

在解压、安装完成后，需要把这个.exe放到python的lib文件夹，我的文件夹路径是：F:\SOFTWARE\Anaconda3\Library\bin。之后，使用如下代码测试是否Selenuim能用。

#### 3、网站分析

这里以[SpringerLink数据库](http://link.springer.com/)为例进行说明。批量下载文献的工作本质上属于爬虫，在进行爬虫之前，我们首先需要分析起点网页和目标网站的结构（这里需要有HTML的知识基础，可以参考[w3school的HTML 教程](http://www.w3school.com.cn/html/index.asp)）。对于我这种半吊子编程选手，当然是希望涉及到编程的部分越少越好，所以我选择的起始页是输入关键词、约束好条件之后的页面。在进入数据库，输入关键词 *higher education* ，选择学科为 *education* ，选择时间为2018-2019之后，得到了文章开头的那张图，嗯，3430篇文献数据，恰好你有某项科研任务要把它们都下下来，网站还不提供批量下载的按钮。嗯，感觉…还可行。我们把这个页面的链接[https://link.springer.com/search?just-selected-from-overlay-value=%22Education%22&amp;date-facet-mode=between&amp;just-selected-from-overlay=facet-discipline&amp;facet-start-year=2018&amp;facet-discipline=%22Education%22&amp;facet-end-year=2019&amp;facet-content-type=%22Article%22&amp;query=higher+education](https://link.springer.com/search?just-selected-from-overlay-value=%22Education%22&date-facet-mode=between&just-selected-from-overlay=facet-discipline&facet-start-year=2018&facet-discipline=%22Education%22&facet-end-year=2019&facet-content-type=%22Article%22&query=higher+education)复制下来。

![](https://upload-images.jianshu.io/upload_images/12875160-a9b71e9ece4444ae.png?imageMogr2/auto-orient/strip|imageView2/2/w/1198/format/webp)

接下来，分析网站结构。我们发现，在[SpringerLink数据库](http://link.springer.com/)中，只要有权限，点击Download PDF就可以下载。那么我们只要把这些链接获取到，就可以实现批量下载。

![](https://upload-images.jianshu.io/upload_images/12875160-2c747149ce5c84a6.png?imageMogr2/auto-orient/strip|imageView2/2/w/814/format/webp)

一般按F12可以进入浏览器的开发者工具，选取这个元素，发现还真是。

![](https://upload-images.jianshu.io/upload_images/12875160-63e1affaf778fb27.png?imageMogr2/auto-orient/strip|imageView2/2/w/840/format/webp)

之后，我们选取“下一页”的元素。

![](https://upload-images.jianshu.io/upload_images/12875160-c374f8c1a301d8bb.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

#### 4、阅读文档

在[Selenium中文文档](https://selenium-python-zh.readthedocs.io/en/latest/index.html)中，我们可以看到要实现我们的想法，需要什么命令。主要用的部分列举如下：

**1）等待页面加载完成**
等待页面加载完成(Waits)可以分为显式等待和隐式等待。显式等待就像我们等网页加载好再操作一样，浏览器等待网页加载完再进行操作。

**2）查找元素**
经过分析，本次编程使用到的元素主要是 `<a>`，css选择器主要是class和id，那么可以通过xpath、class_name、id_name、css_selector等方式查找元素。代码如下：

**3）点击效果**
要实现点击效果，只需要在查找的元素之后，加上.click()。

#### 5、编程过程

首先，是要引进我们用到的库。

按照我们设计的流程编写程序的主干部分，涉及到具体函数先编个名字取代。

具体函数如下：

### 四、结果

嗯，写好代码之后，就该干嘛干嘛，让Chrome自动帮你下载文献吧，中间可以打把游戏什么的（逃）。python基础不扎实改编个现成的代码都显得吃力，嗯……我需要提高的地方还有很多。希望这篇文章能够帮到同在学术半道上的你。

![img](https://upload-images.jianshu.io/upload_images/12875160-f8702d1ef021af79.gif?imageMogr2/auto-orient/strip|imageView2/2/w/934/format/webp)
