# 1

我有一个 numpy.ndarray

我有一个 [numpy](https://www.itbaoku.cn/tag/numpy "numpy").ndarray

```python
a = [['-0.99' '' '0.56' ..., '0.56' '-2.02' '-0.96']]
```

如何将其转换为 int?

输出:

```python
a = [[-0.99 0.0 0.56 ..., 0.56 -2.02 -0.96]]
```

我想要 0.0 代替空白 ''

## 推荐答案

```python
import numpy as np

a = np.array([['-0.99', '', '0.56', '0.56', '-2.02', '-0.96']])
a[a == ''] = 0.0
a = a.astype(np.float)
```

结果是:

```python
[[-0.99  0.    0.56  0.56 -2.02 -0.96]]
```

您的值是[浮点](https://www.itbaoku.cn/tag/floating-point "浮点")数，而不是整数.目前尚不清楚您是否想要[列表](https://www.itbaoku.cn/tag/list "列表")列表或 numpy 数组作为最终结果.您可以轻松获得这样的列表列表:

```python
a = a.tolist()
```

结果:

```python-repl
[[-0.99, 0.0, 0.56, 0.56, -2.02, -0.96]]
```

```python
a = [['-0.99' '' '0.56' ..., '0.56' '-2.02' '-0.96']]
```

如何将其转换为int？

输出 :

```python
a = [[-0.99 0.0 0.56 ..., 0.56 -2.02 -0.96]]
```

我想要 0.0 代替空白 ''

**最佳答案**

```python
import numpy as np

a = np.array([['-0.99', '', '0.56', '0.56', '-2.02', '-0.96']])
a[a == ''] = 0.0
a = a.astype(np.float)
```

结果是:

```python
[[-0.99  0.    0.56  0.56 -2.02 -0.96]]
```

您的值是浮点数，而不是整数。目前尚不清楚您想要一个列表列表还是一个 numpy 数组作为最终结果。您可以轻松获得如下列表:

```python
a = a.tolist()
```

结果:

```python
[[-0.99, 0.0, 0.56, 0.56, -2.02, -0.96]]
```

关于python - 将 numpy 字符串数组转换为 int 数组，我们在Stack Overflow上找到一个类似的问题： [https://stackoverflow.com/questions/21451776/](https://stackoverflow.com/questions/21451776/)

# 2

我在Python3中有一个string Numpy数组，像这样的[Numpy array](https://i.stack.imgur.com/bn1hU.png)，

```javascript
array[['(155)'],['(255)'],['(165)'],['(147)']]
```

复制

我需要把它转换成int Numpy数组，就像这样，

```javascript
array[[115],[255],[165],[147]]
```

### 1 个回答

剥离它们并解析它们：

```python
np.core.defchararray.strip(a, '()').astype(int)
```
