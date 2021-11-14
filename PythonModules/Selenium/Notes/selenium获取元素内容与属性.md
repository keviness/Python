# [python用selenium获取元素标签内容和属性值]()

百度搜索右上角有个“百度首页”的小标签链接

html:

```
<a class="toindex" href="/">百度首页</a>
```

xpath为：

```
//*[@id="u"]/a[1]
```

获取标签内容，也就是“百度首页“”这几个字

python：

```
a=driver.find_element_by_xpath('//*[@id="u"]/a[1]')
print(a.text)
```

输出：

```
百度首页
```

获取class属性内容（其他属性同理，把class替换成属性名称就可以）

```
a=driver.find_element_by_xpath('//*[@id="u"]/a[1]')
print(a.get_attribute('class'))
```

输出：

```
toindex
```
