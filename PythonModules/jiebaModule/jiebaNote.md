## 引言

  [jieba](http://www.smartredirect.de/redir/clickGate.php?u=IgKHHLBT&m=1&p=8vZ5ugFkSx&t=vHbSdnLT&st=&s=&url=https%3A%2F%2Fgithub.com%2Ffxsjy%2Fjieba&r=https%3A%2F%2Fwww.jianshu.com%2Fp%2F883c2171cdb5) 是目前最好的 Python 中文分词组件，它主要有以下 3 种特性：

* 支持 3 种分词模式：精确模式、全模式、搜索引擎模式
* 支持繁体分词
* 支持自定义词典

```python
# 导入 jieba
import jieba
import jieba.posseg as pseg #词性标注
import jieba.analyse as anls #关键词提取
```

## 1 分词

  可使用 `jieba.cut` 和 `jieba.cut_for_search` 方法进行分词，两者所返回的结构都是一个**可迭代**的 generator，可使用 for 循环来获得分词后得到的每一个词语（unicode），或者直接使用 `jieba.lcut` 以及 `jieba.lcut_for_search` 直接返回 list。其中：

* `jieba.cut` 和 `jieba.lcut` 接受 3 个参数：
  * 需要分词的字符串（unicode 或 UTF-8 字符串、GBK 字符串）
  * cut_all 参数：是否使用全模式，默认值为 `False`
  * HMM 参数：用来控制是否使用 HMM 模型，默认值为 `True`
* `jieba.cut_for_search` 和 `jieba.lcut_for_search` 接受 2 个参数：
  * 需要分词的字符串（unicode 或 UTF-8 字符串、GBK 字符串）
  * HMM 参数：用来控制是否使用 HMM 模型，默认值为 `True`

*# 尽量不要使用 GBK 字符串，可能无法预料地错误解码成 UTF-8*

### 1.1 全模式和精确模式

```python
# 全模式
seg_list = jieba.cut("他来到上海交通大学", cut_all=True)
print("【全模式】：" + "/ ".join(seg_list))  
```

> 【全模式】：他/ 来到/ 上海/ 上海交通大学/ 交通/ 大学

```python
# 精确模式
seg_list = jieba.cut("他来到上海交通大学", cut_all=False)
print("【精确模式】：" + "/ ".join(seg_list))  
```

> 【精确模式】：他/ 来到/ 上海交通大学

```python
type(seg_list)
```

> generator

```python
# 返回列表
seg_list = jieba.lcut("他来到上海交通大学", cut_all=True)
print("【返回列表】：{0}".format(seg_list))
```

> 【返回列表】：['他', '来到', '上海', '上海交通大学', '交通', '大学']

```python
type(seg_list)
```

> list

### 1.2 搜索引擎模式

```python
# 搜索引擎模式
seg_list = jieba.cut_for_search("他毕业于上海交通大学机电系，后来在一机部上海电器科学研究所工作")  
print("【搜索引擎模式】：" + "/ ".join(seg_list))
```

> 【搜索引擎模式】：他/ 毕业/ 于/ 上海/ 交通/ 大学/ 上海交通大学/ 机电/ 系/ ，/ 后来/ 在/ 一机部/ 上海/ 电器/ 科学/ 研究/ 研究所/ 工作

```python
# 返回列表
seg_list = jieba.lcut_for_search("他毕业于上海交通大学机电系，后来在一机部上海电器科学研究所工作")  
print("【返回列表】：{0}".format(seg_list))
```

> 【返回列表】：['他', '毕业', '于', '上海', '交通', '大学', '上海交通大学', '机电', '系', '，', '后来', '在', '一机部', '上海', '电器', '科学', '研究', '研究所', '工作']

### 1.3 HMM 模型

  HMM 模型，即 **隐马尔可夫模型（Hidden Markov Model, HMM）** ，是一种基于概率的统计分析模型，用来描述一个系统隐性状态的转移和隐性状态的表现概率。在 jieba 中，对于未登录到词库的词，使用了基于汉字成词能力的 HMM 模型和 Viterbi 算法，其大致原理是：

> 采用四个隐含状态，分别表示为单字成词，词组的开头，词组的中间，词组的结尾。通过标注好的分词训练集，可以得到 HMM 的各个参数，然后使用 Viterbi 算法来解释测试集，得到分词结果。

*# 代码实现可参考 [HmmSeg.py](https://github.com/Leeshine/WordSeg/blob/master/src/Hmm/HmmSeg.py)*

```python
# 未启用 HMM
seg_list = jieba.cut("他来到了网易杭研大厦", HMM=False) #默认精确模式和启用 HMM
print("【未启用 HMM】：" + "/ ".join(seg_list))  
```

> 【未启用 HMM】：他/ 来到/ 了/ 网易/ 杭/ 研/ 大厦

```python
# 识别新词
seg_list = jieba.cut("他来到了网易杭研大厦") #默认精确模式和启用 HMM
print("【识别新词】：" + "/ ".join(seg_list))  
```

> 【识别新词】：他/ 来到/ 了/ 网易/ 杭研/ 大厦

## 2 繁体字分词

  jieba 还支持对繁体字进行分词。

```python
# 繁体字文本
ft_text = """人生易老天難老 歲歲重陽 今又重陽 戰地黃花分外香 壹年壹度秋風勁 不似春光 勝似春光 寥廓江天萬裏霜 """
```

```python
# 全模式
print("【全模式】：" + "/ ".join(jieba.cut(ft_text, cut_all=True)))  
```

> 【全模式】：人生/ 易/ 老天/ 難/ 老/ / / 歲/ 歲/ 重/ 陽/ / / 今/ 又/ 重/ 陽/ / / 戰/ 地/ 黃/ 花/ 分外/ 香/ / / 壹年/ 壹/ 度/ 秋/ 風/ 勁/ / / 不似/ 春光/ / / 勝/ 似/ 春光/ / / 寥廓/ 江天/ 萬/ 裏/ 霜/ /

```python
# 精确模式
print("【精确模式】：" + "/ ".join(jieba.cut(ft_text, cut_all=False)))  
```

> 【精确模式】：人生/ 易/ 老天/ 難老/  / 歲/ 歲/ 重陽/  / 今/ 又/ 重陽/  / 戰地/ 黃/ 花/ 分外/ 香/  / 壹年/ 壹度/ 秋風勁/  / 不/ 似/ 春光/  / 勝似/ 春光/  / 寥廓/ 江天/ 萬/ 裏/ 霜/

```python
# 搜索引擎模式
print("【搜索引擎模式】：" + "/ ".join(jieba.cut_for_search(ft_text)))  
```

> 【搜索引擎模式】：人生/ 易/ 老天/ 難老/  / 歲/ 歲/ 重陽/  / 今/ 又/ 重陽/  / 戰地/ 黃/ 花/ 分外/ 香/  / 壹年/ 壹度/ 秋風勁/  / 不/ 似/ 春光/  / 勝似/ 春光/  / 寥廓/ 江天/ 萬/ 裏/ 霜/

## 3 添加自定义词典

  开发者可以指定自定义词典，以便包含 jieba 词库里没有的词，词典格式如下：

> 词语 词频（可省略） 词性（可省略）

  例如：

```undefined
创新办 3 i
云计算 5
凱特琳 nz
```

*# 虽然  jieba 有新词识别能力，但自行添加新词可以保证更高的正确率。*

### 3.1 载入词典

  使用 `jieba.load_userdict(file_name)` 即可载入词典。

*# `file_name` 为文件类对象或自定义词典的路径*

```python
# 示例文本
sample_text = "周大福是创新办主任也是云计算方面的专家"
```

```python
# 未加载词典
print("【未加载词典】：" + '/ '.join(jieba.cut(sample_text)))
```

> 【未加载词典】：周大福/ 是/ 创新/ 办/ 主任/ 也/ 是/ 云/ 计算/ 方面/ 的/ 专家

```python
# 载入词典
jieba.load_userdict("userdict.txt")
```

```python
# 加载词典后
print("【加载词典后】：" + '/ '.join(jieba.cut(sample_text)))
```

> 【加载词典后】：周大福/ 是/ 创新办/ 主任/ 也/ 是/ 云计算/ 方面/ 的/ 专家

### 3.2 调整词典

  使用 `add_word(word, freq=None, tag=None)` 和 `del_word(word)` 可在程序中动态修改词典。

```python
jieba.add_word('石墨烯') #增加自定义词语
jieba.add_word('凱特琳', freq=42, tag='nz') #设置词频和词性 
jieba.del_word('自定义词') #删除自定义词语 
```

  使用 `suggest_freq(segment, tune=True)` 可调节单个词语的词频，使其能（或不能）被分出来。

```python
# 调节词频前
print("【调节词频前】：" + '/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
```

> 【调节词频前】：如果/放到/post/中将/出错/。

```python
# 调节词频
jieba.suggest_freq(('中', '将'), True)
```

> 494

```python
# 调节词频后
print("【调节词频后】：" + '/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
```

> 【调节词频后】：如果/放到/post/中/将/出错/。

## 4 关键词提取

  jieba 提供了两种关键词提取方法，分别基于 TF-IDF 算法和 TextRank 算法。

### 4.1 基于 TF-IDF 算法的关键词提取

   **TF-IDF(Term Frequency-Inverse Document Frequency, 词频-逆文件频率)** 是一种统计方法，用以评估一个词语对于一个文件集或一个语料库中的一份文件的重要程度，其原理可概括为：

> 一个词语在一篇文章中出现次数越多，同时在所有文档中出现次数越少，越能够代表该文章

  计算公式：TF-IDF = TF * IDF，其中：

* TF(term frequency, TF)：词频，某一个给定的词语在该文件中出现的次数，计算公式：

  ![](//upload-images.jianshu.io/upload_images/6533825-c69c15bcacb4ebbf.png?imageMogr2/auto-orient/strip|imageView2/2/w/250/format/webp)
* IDF(inverse document frequency, IDF)：逆文件频率，如果包含词条的文件越少，则说明词条具有很好的类别区分能力，计算公式：

  ![](//upload-images.jianshu.io/upload_images/6533825-a6a941376dfd68b1.png?imageMogr2/auto-orient/strip|imageView2/2/w/252/format/webp)

  通过 `jieba.analyse.extract_tags` 方法可以基于 TF-IDF 算法进行关键词提取，该方法共有 4 个参数：

* sentence：为待提取的文本
* topK：为返回几个 TF/IDF 权重最大的关键词，默认值为 20
* withWeight：是否一并返回关键词权重值，默认值为 False
* allowPOS：仅包括指定词性的词，默认值为空

```python
s = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
```

```python
for x, w in anls.extract_tags(s, topK=20, withWeight=True):
    print('%s %s' % (x, w))
```

> 欧亚 0.7300142700289363
>
> 吉林 0.659038184373617
>
> 置业 0.4887134522112766
>
> 万元 0.3392722481859574
>
> 增资 0.33582401985234045
>
> 4.3 0.25435675538085106
>
> 7000 0.25435675538085106
>
> 2013 0.25435675538085106
>
> 139.13 0.25435675538085106
>
> 实现 0.19900979900382978
>
> 综合体 0.19480309624702127
>
> 经营范围 0.19389757253595744
>
> 亿元 0.1914421623587234
>
> 在建 0.17541884768425534
>
> 全资 0.17180164988510638
>
> 注册资本 0.1712441526
>
> 百货 0.16734460041382979
>
> 零售 0.1475057117057447
>
> 子公司 0.14596045237787234
>
> 营业 0.13920178509021275

  使用 `jieba.analyse.TFIDF(idf_path=None)` 可以新建 TFIDF 实例，其中 `idf_path` 为 IDF 频率文件。

### 4.2 基于 TextRank 算法的关键词提取

  TextRank 是另一种关键词提取算法，基于大名鼎鼎的 PageRank，其原理可参见论文—— [TextRank: Bringing Order into Texts](http://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf) 。

  通过 `jieba.analyse.textrank` 方法可以使用基于 TextRank 算法的关键词提取，其与 'jieba.analyse.extract_tags' 有一样的参数，但前者默认过滤词性（`allowPOS=('ns', 'n', 'vn', 'v')`）。

```python
for x, w in anls.textrank(s, withWeight=True):
    print('%s %s' % (x, w))
```

> 吉林 1.0
>
> 欧亚 0.9966893354178172
>
> 置业 0.6434360313092776
>
> 实现 0.5898606692859626
>
> 收入 0.43677859947991454
>
> 增资 0.4099900531283276
>
> 子公司 0.35678295947672795
>
> 城市 0.34971383667403655
>
> 商业 0.34817220716026936
>
> 业务 0.3092230992619838
>
> 在建 0.3077929164033088
>
> 营业 0.3035777049319588
>
> 全资 0.303540981053475
>
> 综合体 0.29580869172394825
>
> 注册资本 0.29000519464085045
>
> 有限公司 0.2807830798576574
>
> 零售 0.27883620861218145
>
> 百货 0.2781657628445476
>
> 开发 0.2693488779295851
>
> 经营范围 0.2642762173558316

  使用 `jieba.analyse.TextRank()` 可以新建自定义 TextRank 实例。

### 4.3 自定义语料库

  关键词提取所使用逆向文件频率（IDF）文本语料库和停止词（Stop Words）文本语料库可以切换成自定义语料库的路径。

```python
jieba.analyse.set_stop_words("stop_words.txt")
jieba.analyse.set_idf_path("idf.txt.big");
```

```python
for x, w in anls.extract_tags(s, topK=20, withWeight=True):
    print('%s %s' % (x, w))
```

> 吉林 1.0174270215234043
>
> 欧亚 0.7300142700289363
>
> 增资 0.5087135107617021
>
> 实现 0.5087135107617021
>
> 置业 0.4887134522112766
>
> 万元 0.3392722481859574
>
> 此外 0.25435675538085106
>
> 全资 0.25435675538085106
>
> 有限公司 0.25435675538085106
>
> 4.3 0.25435675538085106
>
> 注册资本 0.25435675538085106
>
> 7000 0.25435675538085106
>
> 增加 0.25435675538085106
>
> 主要 0.25435675538085106
>
> 房地产 0.25435675538085106
>
> 业务 0.25435675538085106
>
> 目前 0.25435675538085106
>
> 城市 0.25435675538085106
>
> 综合体 0.25435675538085106
>
> 2013 0.25435675538085106

## 5 词性标注

  `jieba.posseg.POSTokenizer(tokenizer=None)` 新建自定义分词器，`tokenizer` 参数可指定内部使用的 `jieba.Tokenizer` 分词器。`jieba.posseg.dt` 为默认词性标注分词器。

*# 标注句子分词后每个词的词性，采用和 ictclas 兼容的标记法。*

```python
words = pseg.cut("他改变了中国")
```

```python
for word, flag in words:
    print("{0} {1}".format(word, flag))
```

> 他 r
>
> 改变 v
>
> 了 ul
>
> 中国 ns

## 6 并行分词

  将目标文本按行分隔后，把各行文本分配到多个 Python 进程并行分词，然后归并结果，从而获得分词速度的可观提升。用法：

* jieba.enable_parallel(4)：开启并行分词模式，参数为并行进程数
* jieba.disable_parallel() ：关闭并行分词模式

*# 可参考 [test_file.py](https://github.com/fxsjy/jieba/blob/master/test/parallel/test_file.py)*

> 注意：基于 python 自带的 multiprocessing 模块，目前暂不支持 Windows

## 7 返回词语在原文的起止位置

  使用 `jieba.tokenize` 方法可以返回词语在原文的起止位置。

> 注意：输入参数只接受 unicode

```python
result = jieba.tokenize(u'上海益民食品一厂有限公司')
print("【普通模式】")
for tk in result:
    print("word: {0} \t\t start: {1} \t\t end: {2}".format(tk[0],tk[1],tk[2]))
```

> 【普通模式】
>
> word: 上海         start: 0        end: 2
>
> word: 益民         start: 2        end: 4
>
> word: 食品         start: 4        end: 6
>
> word: 一厂         start: 6        end: 8
>
> word: 有限公司       start: 8        end: 12

```python
result = jieba.tokenize(u'上海益民食品一厂有限公司', mode='search')
print("【搜索模式】")
for tk in result:
    print("word: {0} \t\t start: {1} \t\t end: {2}".format(tk[0],tk[1],tk[2]))
```

> 【搜索模式】
>
> word: 上海         start: 0        end: 2
>
> word: 益民         start: 2        end: 4
>
> word: 食品         start: 4        end: 6
>
> word: 一厂         start: 6        end: 8
>
> word: 有限         start: 8        end: 10
>
> word: 公司         start: 10       end: 12
>
> word: 有限公司       start: 8        end: 12

作者：Gaius_Yao
链接：https://www.jianshu.com/p/883c2171cdb5
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
