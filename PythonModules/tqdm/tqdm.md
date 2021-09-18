Tqdm 是 Python 进度条库，可以在 Python 长循环中添加一个进度提示信息。用户只需要封装任意的迭代器，是一个快速、扩展性强的进度条工具库。

用法：`tqdm(iterator)`

* 代码地址：[https://github.com/tqdm/tqdm](https://github.com/tqdm/tqdm)
* 安装：

```sh
pip install tqdm
```

## 使用方法一: 传入可迭代对象

```python
import time
from tqdm import *
for i in tqdm(range(1000)):
    time.sleep(.01)    #进度条每0.1s前进一次，总时间为1000*0.1=100s
```

```
100%|██████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:10<00:00, 93.97it/s]
```

## 使用方法二: `trange`

`trange(i)` 是 `tqdm(range(i))` 的简单写法

```python
from tqdm import trange
for i in trange(100):
    #do something
    pass
```

```
100%|█████████████████████████████████████████████████████████████████████████████| 100/100 [00:00<00:00, 99344.01it/s]
```

## 使用方法三: 可以为进度条设置描述

在 `for` 循环外部初始化 `tqdm`，可以打印其他信息：

```python
import time
from tqdm import tqdm

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    # 设置描述
    pbar.set_description("Processing %s" % char)
    time.sleep(1)
```

```
Processing d: 100%|██████████████████████████████████████████████████████████████████████| 4/4 [00:04<00:00,  1.00s/it]
```

手动控制进度：

```python
import time
from tqdm import tqdm

# 一共200个，每次更新10，一共更新20次
with tqdm(total=200) as pbar:
    for i in range(20):
        pbar.update(10)
        time.sleep(0.1)
```

```
100%|████████████████████████████████████████████████████████████████████████████████| 200/200 [00:01<00:00, 98.87it/s]
```

```

 1 from tqdm import trange
 2 from random import random, randint
 3 from time import sleep
 4 with trange(100) as t:
 5     for i in t:
 6         # Description will be displayed on the left
 7         t.set_description('下载速度 %i' % i)
 8         # Postfix will be displayed on the right,
 9         # formatted automatically based on argument's datatype
10         t.set_postfix(loss=random(), gen=randint(1,999), str='详细信息',
11                      lst=[1, 2])
12         sleep(0.1)
```

类似显示一个标题和详细信息。

效果：![](https://img2018.cnblogs.com/blog/1324057/201812/1324057-20181211130752937-721230118.png)

## tqdm 的 write 方法

```python
bar = trange(10)
for i in bar:
    time.sleep(0.1)
    if not (i % 3):
        tqdm.write("Done task %i" % i)
```

```
Done task 0
  0%|                                                                                           | 0/10 [00:10<?, ?it/s]
  0%|                                                                                           | 0/10 [00:00<?, ?it/s]
 10%|████████▎                                                                          | 1/10 [00:00<00:01,  8.77it/s]
 20%|████████████████▌                                                                  | 2/10 [00:00<00:00,  9.22it/s]  
  
Done task 3
  0%|                                                                                           | 0/10 [00:10<?, ?it/s]
 30%|████████████████████████▉                                                          | 3/10 [00:00<00:01,  6.91it/s]
 40%|█████████████████████████████████▏                                                 | 4/10 [00:00<00:00,  9.17it/s]
 50%|█████████████████████████████████████████▌                                         | 5/10 [00:00<00:00,  9.28it/s]
  
Done task 6
  0%|                                                                                           | 0/10 [00:10<?, ?it/s]
 60%|█████████████████████████████████████████████████▊                                 | 6/10 [00:00<00:00,  7.97it/s]
 70%|██████████████████████████████████████████████████████████                         | 7/10 [00:00<00:00,  9.25it/s]
 80%|██████████████████████████████████████████████████████████████████▍                | 8/10 [00:00<00:00,  9.31it/s]
   
Done task 9
  0%|                                                                                           | 0/10 [00:11<?, ?it/s]
 90%|██████████████████████████████████████████████████████████████████████████▋        | 9/10 [00:01<00:00,  8.37it/s]
100%|██████████████████████████████████████████████████████████████████████████████████| 10/10 [00:01<00:00,  9.28it/s]
```
