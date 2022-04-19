# Graphpad Prism 9教程，不会 SPSS，也能搞定卡方检验！

**卡方检验**是一种常用的假设检验方法，属于 **非参数检验** ，主要是 **比较两个及两个以上样本率（构成比）以及两个分类变量的关联性分析** 。

它包括两个率或两个构成比比较的卡方检验；多个率或多个构成比比较的卡方检验以及分类资料的相关分析等。

今天继续给大家介绍 **graphpad ** **统计分析系列教程中的卡方检验** 。同样还是以** sample data** 来给大家介绍。

**1. **打开软件，在 contingency 模块下，如下图进行选择

![0.png](https://www.51xxziyuan.com/ueditor/php/upload/image/20210301/1614613796732479.png "1614613796732479.png")

注：如果期望频数有**其中之一** **小于 5** ，那么就应该使用 ** Fisher 精确检验** ，如果每个频数 **都大于 5，** 那么就应该使用 **卡方检验** 。

**2. **进入数据页面

![0 (1).png](https://www.51xxziyuan.com/ueditor/php/upload/image/20210301/1614613808487325.png "1614613808487325.png")

**Sample data **是一组新英格兰杂志的前瞻性研究数据。两横行代表随机分配给受试者的两种处理，分别为阿司匹林和安慰剂。两纵列代表两种不同的结果，分别为罹患心肌梗死和未罹患心肌梗死。

**3. **继续点击 analyze 或者 results 下的 new analysis 进入下一级选择对话框：

![0 (2).png](https://www.51xxziyuan.com/ueditor/php/upload/image/20210301/1614613814441891.png "1614613814441891.png")

**4. **选择 contingency table analyses 下的 chi-square(and Fisher’s exact) test，并选择右侧的 A:Myocardial Infarction 和 B:No MI。点击 ok。

**5. **进一步选择对话框：按下图选择图中 ①-③ 解释如下

![0 (3).png](https://www.51xxziyuan.com/ueditor/php/upload/image/20210301/1614613827638394.png "1614613827638394.png")

* **RR:** (Relative Risk, 相对危险度)（用于前瞻性研究）: 暴露组研究对象的发病风险是非暴露组研究对象的多少倍？
* **AR：** （Attributable Risk, 归因危险度）和是指暴露组发病率与非暴露组发病率之差，它反映发病归因于暴露因素的程度。
* **NNT:** （Number Needed to Treat, 需治疗人数）又称需处理数，可把抽象的率转变为 1 个具体的频数，使临床试验结果转化为临床实践应用的指标，具有表达统计学意义及临床意义的双重作用，是一个衡量临床治疗效果、指导临床决策的有用工具。
* **OR：** （用于回顾性研究）（Odds Ratio, 比值比)，在回顾性研究中可以评价暴露因素（阿司匹林）和疾病（心肌梗死）的关联强度。

**6. **Option 选项卡按下图进行选择：

![0 (4).png](https://www.51xxziyuan.com/ueditor/php/upload/image/20210301/1614613837442891.png "1614613837442891.png")

**7. **点击 ok 得到统计分析结果：

![0 (5).png](https://www.51xxziyuan.com/ueditor/php/upload/image/20210301/1614613843386702.png "1614613843386702.png")

软件提示用 ** Fisher’s test 代替 Chi-square test** 。前者可以计算出一个 **确切的 P 值** ，而后者只计算一个 **近似值** 。对于大样本，差异是微不足道的。对于小样本，差异可能很重要。

* 一般来说：总样本数 ≥ 40，所有理论频数 ≥ 5，用 pearson 卡方检验；
* 总样本数 ≥ 40，出现 1 个理论频数 ≥ 1 并且 ≤ 5，需连续性校正；
* 总样本数 ≥ 40，至少两个理论频数 ≥ 1 并且 ≤ 5，使用 Fisher 精确检验；
* 总样本数＜40 或理论频数＜1，使用 Fisher 精确检验。

![0 (7).png](https://www.51xxziyuan.com/ueditor/php/upload/image/20210301/1614613849750904.png "1614613849750904.png")

注：P＜0.0001，表示两样本频率的差异具有统计学意义。

**8. **为此我还特意去搜了这篇文献：

![0 (7).png](https://www.51xxziyuan.com/ueditor/php/upload/image/20210301/1614613878875235.png "1614613878875235.png")

![0 (6).png](https://www.51xxziyuan.com/ueditor/php/upload/image/20210301/1614613885128695.png "1614613885128695.png")

![0 (8).png](https://www.51xxziyuan.com/ueditor/php/upload/image/20210301/1614613890187512.png "1614613890187512.png")
