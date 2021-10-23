# [selenium+Python(select定位)](https://www.cnblogs.com/101718qiong/p/7929731.html)

传统的下拉菜单 Select 元素，由一个 Select + 一系列的 option 元素构成。

```html
<select id="source" name="source">
 <option value="">--请选择--</option>
 <option value="1001">网络营销</option>
 <option value="1002">公开媒体</option>
 <option value="1003">合作伙伴</option>
    …
</select>
```

对于下拉菜单，我们操作时是先点击下拉选项，再在展开的选项中点击一项来完成选择。

如果用 Selenium 模拟，就需要先点击 Select 元素，再点击 Option，就稍微麻烦了一些。我们可以通过两种方法来处理。

## 1. 直接通过 Xpath 点击选项

通过 Xpath 点击直接选项，可以不用点击下拉，一句代码完成操作。

以上面的局部 HTML 代码为例：

```python
driver.find_element_by_xpath('//*[@id="source"]/option[@value="1002"]').click()
```

## 2. 使用 Select 类

使用 Xpath 虽然可行，但是稍微缺乏一些灵活性。

在 WebDriver 中专门提供了一个 Select 类来处理下拉菜单。

```python
# 导入 Select 类
from selenium.webdriver.support.select import Select
# 找到下拉菜单元素
e = driver.find_element_by_id('source')
select = Select(e)
# 按文本选择
select.select_by_visible_text('合作伙伴')
```

Select 类中还提供了通过 option 索引选取、通过 value 值选取：

```python
select.select_by_index(1)
select.select_by_value('1003')
```

由于我们经常使用 index 和 visible text (可见文本) 的方式选择选项。所以我们简单封装一下：

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def select(driver, locator, option=0):
    e = Select(driver.find_element(*locator))
    # 如果选项为整数，则通过 index 选择
    if isinstance(option, int):
        e.select_by_index(option)
    # 如果选项为字符串，则通过 visible_text 选择
    elif isinstance(option, str):
        e.select_by_visible_text(option)
    else:
        raise ValueError('只能通过index或可见文本进行下拉选项选择！')

# 使用
select(driver, (By.ID, 'source'), '合作伙伴')
```

> 在处理下拉菜单的时候需要注意，这里只针对 Select 标签元素，现在有很多网页上的下拉菜单由 ul 或者 span 构成，这种方法就无法处理。
