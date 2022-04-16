# 手把手教你用Pandas作出花里胡哨的表格

0 前言

对很多数据分析师而言，用Pandas清理、展现数据几乎是日常工作中必不可少的一环。通常，我们会配合Jupyter的notebook或者lab去形成交互，方便我们及时观察DataFrame每一步的变化。往往到了最后的展示环节，我们又需要把DataFrame导出成csv或者excel，因为DataFrame本身很难像Excel那样去灵活调整数据的样式。

但是！！！在Style功能的加持下，我们不依赖Excel，就纯粹用Pandas也能做出美观大方(花里胡哨)的表格来，下图就是例子：

![](https://pic4.zhimg.com/80/v2-17792f4208447cdf87da3b6cd3959ed3_1440w.jpg)
一个花里胡哨的表格

推荐自学能力强的同学直接去看官网文档：[点击查看官方文档](https://link.zhihu.com/?target=https%3A//pandas.pydata.org/pandas-docs/stable/user_guide/style.html%23Building-styles)。后面的教程我就来教大家如何一步一步让我们的表格变得美观大方(花里胡哨)起来吧~

### 1 Style入门

Style是Pandas内置的一个渲染功能，通过html/css等前端的呈现方法去改变dataframe在Jupyter中的呈现，从而实现更为美观的表格。

目前来看，虽然低版本的pandas也能使用style功能，但最好确保pandas的版本大于等于1.2.0，因为部分style的高级功能需要pandas的版本大于等于1.2.0才能支持使用。

下面我们通过代码先生成一个随机的df

```python
np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))], axis=1)
df.iloc[3, 3] = np.nan
df.iloc[0, 2] = np.nan
df['F'] = ['apple','banana','cat','dog','eye','food','girl','hook','imagine','jackeylove']
df['A'] = df['A'].map(int)
df
```

![](https://pic2.zhimg.com/80/v2-e89a53c13f61c90e7e23d70586f80dd9_1440w.jpg)
原始的DataFrame

### 1.1 处理缺失值

假设目前这个数据是我们最后需要展示的数据。那么首先我们观察这个数据，很辣眼的就是两个缺失值。那么如何用style去处理缺失值呢？

* `set_na_rep(na_rep)`接受 `na_rep`作为参数，`str`类型，作用在整个DataFrame上

代码：

```python
df.style\
  .set_na_rep('-') # 处理缺失值
```

可以看到，style的调用十分简单，只需要在df的后面接一个 `.style`即可，接完了之后可以用 `.function`的方式去调用style的各种function。这里的 `set_na_rep()`就是其中一个用于处理缺失值的，下面可以看到使用后的效果：

![](https://pic3.zhimg.com/80/v2-8ae50a8f883607bda8f33c55f9d07e92_1440w.jpg)

我们还可以把缺失值设置为任何字符串：

![](https://pic4.zhimg.com/80/v2-180b533d46f93dc3344b0a59fa6a6c3b_1440w.jpg)

### 1.2 调整单元格内容的格式

对于数字而言，通常我们希望是展现出小数点后两位即可，或者是带个百分比。要实现这个需求，可以用format功能，注意这里的format和格式化字符串的 `'a string {}'.format()`的语法格式是类似的。

* `format(formatter, subset=None, na_rep=None)`
* 参数formatter代表数字要呈现的格式，需要传入符合格式化字符串语法规范的字符串，[参考](https://link.zhihu.com/?target=https%3A//www.python.org/dev/peps/pep-3101/)
* `subset`可以帮助指定对特定的column和row进行调整，`na_rep`代表nan值的表现形式

```python
df.style\
  .set_na_rep('缺失')\ # 处理缺失值
  .format('{:.2f}',subset=list('BCDE')) # 对BCDE四列应用格式化字符串
```

注意这里格式化字符串 `'{:.2f}'`的意思是，保留浮点数后两位。结果如下：

![](https://pic3.zhimg.com/80/v2-00c3cbbc02c2c072f721771b7e351ad2_1440w.jpg)

眼光犀利的你，肯定发现了nan值又变回来了，这是由于nan值无法接受 `':.2f'`这个浮点数形式的语法，所以可以看到通过 `set_na_rep`改变了全局的nan值后，又被后面的format覆盖掉了，最终又变回了nan值。

这个时候，我们需要用更为复杂的字典格式来调整数据，可以看到，在字典中不仅可以改变数据展示的正负值、百分数，还能接受函数，这就使得数据展示变得十分强大。

```python
# func1代表着：如果o在字符里面则返回原字符加上特殊的unicode码(代表笑脸)否则返回原字符
func1 = lambda x: x + '\U0001F600' if 'o' in x else x
# func2代表着：返回一个带后缀的格式化字符串
func2 = lambda x: '{:+.2f}'.format(x) + '$'

df.style\
  .set_na_rep('缺失')\
  .format({'F': func1, 'B':func2,'D':'{:.4f}','E':'{:.2%}'},na_rep="-")
  # 注意这里na_rep="-"是针对前面所有的列，即FBDE，会覆盖影响全局的的set_na_rep
```

结果如下：

![](https://pic2.zhimg.com/80/v2-fa9e72679ebc5447da99bd44cb935ba1_1440w.jpg)
可爱的emoji

提醒：format的展示功能其实是非常复杂且强大的，这里我们只用了常用的一些功能，如保留小数点位数和展现百分数。感兴趣的盆友可以去看上面给的format的参考。

### 1.3 切片与highlight

上面的部分演示是为了展示功能，所以有些花里胡哨，下面我们搞普通一点。顺带再介绍两个功能：

* highlight_null(null_color='red', subset=None) 用null_color指定颜色，subset指定column和row
* 注意这里subset的使用方式是指定 `pd.IndexSlice`这和 `DataFrame.iloc`类似

```python
df.style\
  .set_na_rep('-')\
  .format({'B':func2,'C':'{:.4f}','D':'{:.4f}','E':'{:.2%}'},na_rep="-")\
  .highlight_null("darkorange",subset=pd.IndexSlice[2:4,['D']])
  # 对于第2/3/4行，D列，的数据，存在nan值的数据用darkorange这个颜色进行高亮显示
```

![](https://pic1.zhimg.com/80/v2-a8ba84dacd0a506cee69356521a96364_1440w.jpg)

学完上面三个功能，style就算是入门啦，相对较难的点是在于 `format`部分，因为用 `format`配合各种函数去操作数据的时候，会存在多种功能的嵌套，导致有些难以理解，这一块需要多多coding才能理解掌握。

### 2 Style进阶

在进阶部分，我们着重关注数据中色彩的展示。一般我们采用apply或applymap的功能传入函数去带条件地展示数据的颜色。

### 2.1 灵活的Apply

* apply可以控制是针对行或者列，applymap针对全部元素
* `apply(func, axis=0, subset=None, \*\*kwargs)`
* Apply to each column (axis=0 or 'index'), to each row (axis=1 or 'columns'), or to the entire DataFrame at once with axis=None.

我们通过下面的代码和结果来理解这个功能：

```python
def color1(val):
    c1,c2 = ('red','yellow') if val < 0 else ('black','none')
    return f'color: {c1}; background-color: {c2}'

def color2(vals):
    func = lambda s: 'color: orange' if 'o' in s else 'background-color: darkorange'
    return [func(val) for val in vals]

df.style\
  .set_na_rep('-')\
  .format({'B':func2,'C':'{:.4f}','D':'{:.4f}','E':'{:.2%}'},na_rep="-")\
  .highlight_null("gray")\
  .applymap(color1,subset=['B'])\ # 针对B列使用color1这个函数
  .apply(color2,subset=['F']) # 针对F列使用color2这个函数
```

结果如下：

![](https://pic2.zhimg.com/80/v2-47b8f8751b619698be8aa55cef49bb01_1440w.jpg)
好看+1

灰常神奇，顿时有了颜色！

这里要认真观察函数的输入和输出到底是什么，才能明白为什么颜色会发生改变。以B列为例，B列的数据通过applymap的方式传入了color1这个我们自己写好的函数里面，color1这个函数再根据输入进行判断，输出特定的字符串。特别需要注意的是，只有输出符合HTML CSS样式的字符串，才能确保颜色、样式会被改变。这也是如最开始说的那种，style是通过改变dataframe的HTML CSS来进行渲染呈现的。

我们把B列最后的输出拿出来看一下究竟是啥：

![](https://pic1.zhimg.com/80/v2-f8c3f87e569a3e6519f36682e5d7d9c0_1440w.jpg)

可以看到输出的字符串都是“attribute: value; ...”这种类型的字符串，这里的attribute是指CSS的attribute，value是指针对这个attribute而言的取值。下面我们来写一个标准的HTML CSS字符串：

```python
my_style = '''
font-family: "Times New Roman"; font-size: 20px; 
font-style: italic; font-weight: bold; 
color: red; background-color: white
'''
# 通过my_style指定使用Times New Roman字体，字体大小为20px，
# 字体为斜体加粗，颜色为红色，背景填充为白色
df.style.applymap(lambda x: my_style,subset=['E'])
```

效果如下：

![](https://pic3.zhimg.com/80/v2-80e00aa275b4b55e91092c842a121b62_1440w.jpg)

### 2.2 渐变色

除了用apply去渲染颜色，我个人还有个非常喜欢的功能就是 `gradient_color`，这个功能可以快速的实现丰富的渐变色，可选项多，无脑快速。

* `background_gradient(cmap='PuBu', low=0, high=0, axis=0, subset=None, text_color_threshold=0.408, vmin=None, vmax=None)`
* background_gradient的参数比较复杂一点，但是实际用到的只有cmap和subset。cmap是根据matplotlib指定的颜色参数，subset上面有讲过
* cmap的取值可以在[matplotlib cmap](https://link.zhihu.com/?target=https%3A//matplotlib.org/stable/tutorials/colors/colormaps.html%3Fhighlight%3Dcolormap)中找到，个人比较推荐的参数是'PuBu','PuBuGn','Pastel1'。
* 喜欢花里胡哨的盆友可以参考这几个：'viridis', 'plasma', 'inferno', 'magma', 'cividis'

代码：

```python
df.style\
  .set_na_rep('-')\
  .format({'B':func2,'C':'{:.4f}','D':'{:.4f}','E':'{:.2%}'},na_rep="-")\
  .highlight_null("gray")\
  .applymap(color1,subset=['B']).apply(color2,subset=['F'])\
  .background_gradient(cmap='Pastel1',subset=['C','D','E'])
  # 对列CDE使用名为'Pastel1'的渐变色map
```

效果：

![](https://pic3.zhimg.com/80/v2-ba31930eec29726ee9ef9a1bb57ad69e_1440w.jpg)
好看+2

渐变色可以选择的范围很广，大家可以多调试一下色彩看看效果。

### 2.3 内容条形图

style还有个神奇的bar功能，可以让数据在单元格内部形成一个条形图，这就让我们的图表看起来更加丰富了。

* `bar(subset=None, axis=0, color='#d65f5f', width=100, align='left', vmin=None, vmax=None)`
* 这里要注意的参数是subset,color,和align。color如果是单个字符串，代表一个颜色，如果是元组，则分别代表负值和正值的颜色，align是指对其的方向
* color的颜色除了'red','blue'这种类型，还可以使用html类型，[参考](https://link.zhihu.com/?target=https%3A//htmlcolorcodes.com/zh/yanse-biao/)

代码：

```python
df.style\
  .set_na_rep('-')\
  .format({'B':func2,'C':'{:.4f}','D':'{:.4f}','E':'{:.2%}'},na_rep="-")\
  .highlight_null("gray")\
  .applymap(color1,subset=['B']).apply(color2,subset=['F'])\
  .background_gradient(cmap='Pastel1',subset=['C','D'])\
  .bar(subset=['E'], align='mid', color=['#00BCD4','#6A1B9A'])
  # 对E列使用条形图功能，条形从中间往左右展开，color列表中的颜色分布代表左边和右边的颜色
```

![](https://pic4.zhimg.com/80/v2-28136eb6cef5dd81777c1297f0eb5013_1440w.jpg)
渐渐华丽起来...

### 2.4 标题与隐藏列

设置表格的标题，隐藏指定的列都很好理解，直接看代码就行~

* `set_caption(caption)` caption是一个字符串
* `hide_index()`可以隐藏索引
* `hide_columns()`通过参数subset指定隐藏的column

代码：

```python
title = '这是一个比较 \U0001F42E\U0001F37A 的标题'

df.style\
  .set_na_rep('-')\
  .format({'B':func2,'C':'{:.4f}','D':'{:.4f}','E':'{:.2%}'},na_rep="-")\
  .highlight_null("gray")\
  .applymap(color1,subset=['B']).apply(color2,subset=['F'])\
  .background_gradient(cmap='Pastel1',subset=['C','D'])\
  .bar(subset=['E'], align='mid', color=['#00BCD4','#6A1B9A'])\
  .set_caption(title).hide_index().hide_columns(subset=['A'])
  # 把字符串title设置为标题，隐藏索引，隐藏A列
```

结果：

![](https://pic3.zhimg.com/80/v2-a0b4ee197ffbdb6ee46802dae05cf0d6_1440w.jpg)
花里胡哨+1

我们发现数据本身这样处理已经差不多到极限了，剩下的要想进行美观，其实需要调整整个表格，如表格长宽，字体大小和样式，对齐方式等等。

### 3 Style高级

要想对表格的全局做修改，需要用到两个非常重要的功能。说实话，由于我也不是搞前端，很多东西自己也是摸黑抓瞎研究出来的，所以欢迎大佬们来指导交流。

* `set_properties(subset=None, **kwargs)`参数：A dictionary of property, value pairs to be set for each cell. 这个功能可以看成是快速针对table的所有内容做操作
* `set_table_styles(table_styles, axis=0, overwrite=True)`这个table_styles的参数稍微复杂点，需要通过实际案例来讲述。

代码：

```python
style1 = [
    dict(selector="th", props=[("font-size", "175%"), ("text-align", "center"),("background-color", "#FCF3CF"),('width',"150px"),('height','50px')]),
    dict(selector="td", props=[("font-size", "125%"), ("text-align", "right"),('width',"150px"),('height','50px')]),
    dict(selector="caption", props=[("caption-side", "top"),("font-size","150%"),("font-weight","bold"),("text-align", "left"),('height','50px'),('color','#E74C3C')])
]

# overwrite需要pandas1.2.0
style2 = {
    'F': [dict(selector='td', props=[('text-align','center'),("font-weight","bold"),("text-transform","capitalize")])],
    'B': [dict(selector='td', props=[('text-align','left'),("font-style","italic")])],
    'E': [dict(selector='td', props=[('text-align','center')])],
    'C': [dict(selector='td', props=[('text-decoration','underline'),('text-decoration-color','red'),('text-decoration-style','wavy')])]
}

df.style\
  .set_na_rep('-')\
  .format({'B':func2,'C':'{:.4f}','D':'{:.4f}','E':'{:.2%}'},na_rep="-")\
  .highlight_null("gray")\
  .applymap(color1,subset=['B']).apply(color2,subset=['F'])\
  .background_gradient(cmap='Pastel1',subset=['C','D'])\
  .bar(subset=['E'], align='mid', color=['#00BCD4','#6A1B9A'])\
  .set_caption(title).hide_index().hide_columns(subset=['A'])\
  .set_table_styles(style1).set_table_styles(style2,overwrite=False)\
  .set_properties(**{'font-family': 'Microsoft Yahei','border-collapse': 'collapse',
                     'border-top': '1px solid black','border-bottom': '1px solid black'})
  # 先使用style1，再用style2，保证不推翻Style1的设定，最后进行全局设定
```

结果：

![](https://pic4.zhimg.com/80/v2-17792f4208447cdf87da3b6cd3959ed3_1440w.jpg)
花里胡哨拉满

`set_properties`比较好理解，里面的语句规范和html css的一样，就是一个key:value的pair，key相当于是html的属性，如font-family这些，value相当于是对应的key的取值。至于html和css到底有哪些属性可以调整，可以去下面网址自行查阅：[https://www.**w3schools.com/cssref/cs**s3_pr_font-variant-caps.asp](https://link.zhihu.com/?target=https%3A//www.w3schools.com/cssref/css3_pr_font-variant-caps.asp)

`set_table_styles`这个功能中的table_styles参数值的好好研究下，这是实现表格精细化调整的关键所在！

table_styles这个参数接受两种形式的参数，一个是列表，一个是字典。

* 列表。列表里面必须是字典，且字典必须用selector=A,props=B这个固定的方式。其中selector=A代表要选择的属性，常见的有'th','td','caption'。意思是表格的列名那一行，表格每一行的内容（不包括列名那一行），表格的标题。这个列表的方式一般用于控制表格的整体。
* 字典。key必须是每一个列名，value必须是一个列表，且这个列表的形式需要和table_styles的列表形式一致。这个方式一般用于控制单个列的形式。
* overwrite参数是说当这个style是否要取代前一个style。这里取False说明我们第二个style在沿用第一个style的情况下去操作。

我们必须考虑清楚参数在对什么调整。

* 其实这里最为关键的变量在于props，这个列表指定了要调整的具体细节是什么，比如说font-size,backgroud-color这些，都是表格的属性。

虽然set_table_styles只是一个功能，但这个功能涉及的操作其实比前面所有的东西都多，因为这里本质上是在写html css了，唯一的好处是，用这个写足够方便。

接下来我们再对细节稍微调整一下，然后把style打包成一个函数。

```python
def decorative(df):
    func1 = lambda x: x + '\U0001F600' if 'o' in x else x
    func2 = lambda x: '{:+.2f}'.format(x) + '$'

    def color1(val):
        c1,c2 = ('red','yellow') if val < 0 else ('black','none')
        return f'color: {c1}; background-color: {c2}'

    def color2(vals):
        func = lambda s: 'color: orange' if 'o' in s else 'background-color: darkorange'
        return [func(val) for val in vals]

    title = 'Pandas\' Style Function is Amazing!'
    style1 = [
        dict(selector="th", props=[("font-size", "155%"), ("text-align", "center"),("background-color", "#FCF3CF"),('width',"150px"),('height','50px')]),
        dict(selector="td", props=[("font-size", "125%"), ("text-align", "center"),('width',"130px"),('height','40px')]),
        dict(selector="caption", props=[("caption-side", "top"),("font-size","150%"),("font-weight","bold"),("text-align", "center"),('color','#E74C3C'),
                                        ('border','1px dotted red'),
                                        ('padding','30px'),('background-clip', 'padding-box'),
                                        ('background-image',"url('https://i.loli.net/2021/04/13/lZS9gj6CybK1cWv.png')"),
                                        ("background-size","900px 100px")
                                       ])
    ]
    # overwrite需要pandas1.2.0
    style2 = {
        'F': [dict(selector='td', props=[('text-align','center'),("font-weight","bold"),("text-transform","capitalize")])],
        'B': [dict(selector='td', props=[('text-align','center'),("font-style","italic")])]
    }
    show =  df.style\
              .set_na_rep('-')\
              .format({'B':func2,'C':'{:.4f}','D':'{:.4f}','E':'{:.2%}'},na_rep="-")\
              .highlight_null("gray")\
              .applymap(color1,subset=['B']).apply(color2,subset=['F'])\
              .background_gradient(cmap='PuBu',subset=['C','D'])\
              .bar(subset=['E'], align='mid', color=['#33FF00','#FF0000'])\
              .set_caption(title).hide_index().hide_columns(subset=['A'])\
              .set_table_styles(style1).set_table_styles(style2,overwrite=False)\
              .set_properties(**{'font-family': 'Times New Roman','border-collapse': 'collapse','text-align':'center',
                                 'border-top': '2px solid black','border-bottom': '2px solid black'
                                 })
    return show

decorative(df)
```

效果：

![](https://pic1.zhimg.com/80/v2-af1201b34ed78b0c9d1068629514d878_1440w.jpg)
美观大方

可以看到，在CSS的强力加持下，设置在caption内部嵌入了图片！就是written by ocean那一行，没错，那是图片，不是单纯的html文字。

最后可以说一下这个功能其他用途，我们把style风格的表格直接输出为html文件，有了这个html文件，我们就能直接把表格用于邮件发送了~也就是说，把Python脚本写好以后，每次都能通过邮箱发送html文件，从而得到非常好看的自动化格式的表格。

```python
ret = decorative(df)
html = ret.render()

with open('table_html.txt','w',encoding='utf-8') as f:
    f.write(html)
```

HTML文件：

![](https://pic4.zhimg.com/80/v2-3420075c2f5849416454c675042b3557_1440w.jpg)

### 4 总结

1. df.style调出style格式
2. set_na_rep调整全局nan值
3. format精细化控制数值/字符内容的呈现
4. highlight_null对nan值进行颜色调节
5. applymap/apply针对性地调节行和列的颜色
6. background_gradient设置渐变色
7. bar展示单元格内部的条形图
8. set_caption设置标题
9. hide_index隐藏索引
10. hide_columns隐藏特定列
11. set_table_styles精细化调整全局各元素的样式
12. set_properties快速设置全局格式

发布于 2021-04-15 01:52

[Pandas(Python)](https://www.zhihu.com/topic/20179633)

[数据分析](https://www.zhihu.com/topic/19559424)

[Python](https://www.zhihu.com/topic/19552832)

赞同 226 条评论

分享

喜欢
