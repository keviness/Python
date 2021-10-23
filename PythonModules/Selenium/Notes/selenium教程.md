# Python中Selenium库使用教程详解

2020-10-20**阅读** **982**0

**selenium介绍**

selenium最初是一个自动化测试工具,而爬虫中使用它主要是为了解决requests无法直接执行[JavaScript](https://cloud.tencent.com/product/sms?from=10680)代码的问题 selenium本质是通过驱动浏览器，完全模拟浏览器的操作，比如跳转、输入、点击、下拉等，来拿到网页渲染之后的结果，可支持多种浏览器

中文参考文档

官网

**环境安装**

下载安装selenium

```
pip install selenium -i https://mirrors.aliyun.com/pypi/simple/
```

谷歌浏览器驱动程序下载地址：

http://chromedriver.storage.googleapis.com/index.html

**使用示例**

```javascript
from selenium import webdriver
from time import sleep

# 实例化一款浏览器
bor = webdriver.Chrome(executable_path='chromedriver.exe')

# 对指定的url发起请求
bor.get('https://www.jd.com/')
sleep(1)
# 进行标签定位
search_input = bor.find_element_by_id('key')

# 向搜索框中录入关键词
search_input.send_keys("mac pro")

# 点击搜索按钮
btn = bor.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
btn.click()
sleep(2)

# 执行js，让滚轮向下滚动
bor.execute_script('window.scrollTo(0, document.body.scrollHeight)')
sleep(2)

page_text = bor.page_source

print(page_text)

bor.quit()
```

**浏览器创建**

Selenium支持非常多的浏览器，如Chrome、Firefox、Edge等，还有Android、BlackBerry等手机端的浏览器。另外，也支持无界面浏览器PhantomJS。

```javascript
from selenium import webdriver
 
browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser = webdriver.Edge()
browser = webdriver.PhantomJS()
browser = webdriver.Safari()
```

**元素定位**

webdriver 提供了一系列的元素定位方法，常用的有以下几种：

| 定位一个元素                      | 定位多个元素                       | 含义                  |
| --------------------------------- | ---------------------------------- | --------------------- |
| find_element_by_id                | find_elements_by_id                | 通过元素id定位        |
| find_element_by_name              | find_elements_by_name              | 通过元素name定位      |
| find_element_by_xpath             | find_elements_by_xpath             | 通过xpath表达式定位   |
| find_element_by_link_text         | find_elements_by_link_tex          | 通过完整超链接定位    |
| find_element_by_partial_link_text | find_elements_by_partial_link_text | 通过部分链接定位      |
| find_element_by_tag_name          | find_elements_by_tag_name          | 通过标签定位          |
| find_element_by_class_name        | find_elements_by_class_name        | 通过类名进行定位      |
| find_elements_by_css_selector     | find_elements_by_css_selector      | 通过css选择器进行定位 |

**注意：**

1、find_element_by_xxx找的是第一个符合条件的标签，find_elements_by_xxx找的是所有符合条件的标签。

2、根据ID、CSS选择器和XPath获取，它们返回的结果完全一致。

3、另外，Selenium还提供了通用方法 `find_element()`，它需要传入两个参数：查找方式 `By`和值。实际上，它就是 `find_element_by_id()`这种方法的通用函数版本，比如 `find_element_by_id(id)`就等价于 `find_element(By.ID, id)`，二者得到的结果完全一致。

**实例演示**

假如有一个web页面，通过前端工具查看到一个元素的属性是这样的。

```javascript
<html 
 <head 
 <body link="#0000cc" 
 <a href="/" rel="external nofollow" onmousedown="return c({'fm':'tab','tab':'logo'})" 
 <form name="f" action="/s" 
  <span  </span 
  <input name="wd" value="" maxlength="255" autocomplete="off" 
```

通过id定位：

```
dr.find_element_by_id("kw")
```

通过name定位：

```
dr.find_element_by_name("wd")
```

通过class name定位：

```
dr.find_element_by_class_name("s_ipt")
```

通过tag name定位：

```
dr.find_element_by_tag_name("input")
```

通过xpath定位，xpath定位有N种写法，这里列几个常用写法：

```
dr.find_element_by_xpath("//*[@]")
dr.find_element_by_xpath("//*[@name='wd']")
dr.find_element_by_xpath("//input[@]")
dr.find_element_by_xpath("/html/body/form/span/input")
dr.find_element_by_xpath("//span[@]/input")
dr.find_element_by_xpath("//form[@]/span/input")
dr.find_element_by_xpath("//input[@ and @name='wd']")
```

通过css定位，css定位有N种写法，这里列几个常用写法：

```
dr.find_element_by_css_selector("#kw")
dr.find_element_by_css_selector("[name=wd]")
dr.find_element_by_css_selector(".s_ipt")
dr.find_element_by_css_selector("html   body   form   span   input")
dr.find_element_by_css_selector("span.soutu-btn  input#kw")
dr.find_element_by_css_selector("form#form   span   input")
```

假如页面上有如下一组文本链接

```javascript
<a href="http://news.baidu.com" rel="external nofollow" name="tj_trnews" 新闻</a 
<a href="http://www.hao123.com" rel="external nofollow" name="tj_trhao123" hao123</a 
```

通过link text定位：

```
dr.find_element_by_link_text("新闻")
dr.find_element_by_link_text("hao123")
```

通过partial link text定位：

```
dr.find_element_by_partial_link_text("新")
dr.find_element_by_partial_link_text("hao")
dr.find_element_by_partial_link_text("123")
```

**控制浏览器**

常用的控制浏览器操作的一些方法

| 方法                | 说明                   |
| ------------------- | ---------------------- |
| set_window_size()   | 设置浏览器的大小       |
| back()              | 控制浏览器后退         |
| forward()           | 控制浏览器前进         |
| refresh()           | 刷新当前页面           |
| clear()             | 清除文本               |
| send_keys (value)   | 模拟按键输入           |
| click()             | 单击元素               |
| submit()            | 用于提交表单           |
| get_attribute(name) | 获取元素属性值         |
| is_displayed()      | 设置该元素是否用户可见 |
| size                | 返回元素的尺寸         |
| text                | 获取元素的文本         |

? 示例

```javascript
from selenium import webdriver

from time import sleep
#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口

browser = webdriver.Chrome(executable_path= "chromedriver.exe")

#2.通过浏览器向服务器发送URL请求
browser.get("https://www.baidu.com/")

sleep(3)

#3.刷新浏览器
browser.refresh()

#4.设置浏览器的大小
browser.set_window_size(1400,800)

#5.设置链接内容
element=browser.find_element_by_link_text("新闻")
element.click()
```

**调用JavaScript代码**

虽然WebDriver提供了操作浏览器的前进和后退方法，但对于浏览器滚动条并没有提供相应的操作方法。在这种情况下，就可以借助JavaScript来控制浏览器的滚动条。WebDriver提供了execute_script()方法来执行JavaScript代码。

用于调整浏览器滚动条位置的JavaScript代码如下：

```javascript
<!-- window.scrollTo(左边距,上边距); -- 
window.scrollTo(0,450);
```

```javascript
from selenium import webdriver
from time import sleep

# 1.访问百度
drive = webdriver.Chrome(executable_path='chromedriver.exe')
drive.get('https://www.baidu.com')

# 2.搜索
drive.find_element_by_id('kw').send_keys('python')
drive.find_element_by_id('su').click()

# 3.休眠2s,获取服务器的响应内容
sleep(2)

# 4.通过javascript设置浏览器窗口的滚动条位置
drive.execute_script('window.scrollTo(0, 500)')
# drive.execute_script('window.scrollTo(0, document.body.scrollHeight)') #滑到最底部

sleep(2)
drive.close()
```

**获取页面源码数据**

通过 `page_source`属性可以获取网页的源代码，接着就可以使用解析库（如正则表达式、Beautiful Soup、pyquery等）来提取信息了。

? 示例

```javascript
from selenium import webdriver
from time import sleep

# 1.访问百度
drive = webdriver.Chrome(executable_path='chromedriver.exe')
drive.get('https://www.baidu.com')

# 2.搜索
drive.find_element_by_id('kw').send_keys('python')
drive.find_element_by_id('su').click()

# 3.休眠2s,获取服务器的响应内容
sleep(2)

# 4.获取页面源码数据
text = drive.page_source
print(text)

drive.close()
```

**cookie操作**

有时候我们需要验证浏览器中cookie是否正确，因为基于真实cookie的测试是无法通过白盒和集成测试进行的。WebDriver提供了操作Cookie的相关方法，可以读取、添加和删除cookie信息。

WebDriver操作cookie的方法：

| 方法                              | 说明                                                                                                                  |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| get_cookies()                     | 获得所有cookie信息                                                                                                    |
| get_cookie(name)                  | 返回字典的key为“name”的cookie信息                                                                                   |
| add_cookie(cookie_dict)           | 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值                                                          |
| delete_cookie(name,optionsString) | 删除cookie信息。“name”是要删除的cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域” |
| delete_all_cookies()              | 删除所有cookie信息                                                                                                    |

? 示例

```javascript
from selenium import webdriver
drive = webdriver.Chrome(executable_path='chromedriver.exe')
drive.get('https://www.cnblogs.com/')

# 1.打印cookie信息
print(drive.get_cookies())

# 2.添加cookie信息
dic = {'name':'name', 'value':'python'}
drive.add_cookie(dic)
print(drive.get_cookies())

# 3.遍历打印cookie信息
for cookie in drive.get_cookies():
 print(f"{cookie['name']}---f{cookie['value']}\n")

drive.close()
```

**谷歌无头浏览器**

PhantomJs已停止维护更新，这里使用谷歌的无头浏览器，是一款无界面的谷歌浏览器。很多时候我们爬取数据，并不想打开一个浏览器窗口进行操作，我们只需要获取数据或者拿到cookie然后进行操作。

? 示例

```javascript
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 1.创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 2.创建浏览器对象
drive = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)

# 3.发起请求获取数据
drive.get('https://www.cnblogs.com/')

page_text = drive.page_source
print(page_text)

drive.close()
```

**selenium规避被检测识别**

现在不少大网站有对selenium采取了监测机制。比如正常情况下我们用浏览器访问淘宝等网站的 window.navigator.webdriver的值为 undefined。而使用selenium访问则该值为true。那么如何解决这个问题呢？

只需要设置Chromedriver的启动参数即可解决问题。在启动Chromedriver之前，为Chrome开启实验性功能参数 `excludeSwitches`，它的值为 `['enable-automation']`，完整代码如下：

? 示例

```javascript
from selenium import webdriver
from selenium.webdriver import ChromeOptions

# 1.实例化一个ChromeOptions对象
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 2.将ChromeOptions实例化的对象option作为参数传给Crhome对象
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=option)

# 3.发起请求
driver.get('https://www.taobao.com/')
```
