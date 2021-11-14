# selenium各种翻页【下一页】例子

## 学习翻页代码1：获取进入下一页的标签[text()='下一页']

```python3
from selenium import webdriver
import time
import re

class Douyu(object):

    def __init__(self):
        # 开始时的url
        self.start_url = "https://www.douyu.com/directory/all"
        # 实例化一个Chrome对象
        self.driver = webdriver.Chrome()
        # 用来写csv文件的标题
        self.start_csv = True

    def __del__(self):
        self.driver.quit()

    def get_content(self):
        # 先让程序两秒,保证页面所有内容都可以加载出来
        time.sleep(2)
        item = {}
        # 获取进入下一页的标签
        next_page = self.driver.find_element_by_xpath("//span[text()='下一页']/..")
        # 获取用于判断是否是最后一页的属性
        is_next_url = next_page.get_attribute("aria-disabled")
        # 获取存储信息的所有li标签的列表
        li_list = self.driver.find_elements_by_xpath("//ul[@class='layout-Cover-list']//li")
      
        # 提取需要的数据
        for li in li_list:
          
            item["user-id"] = li.find_element_by_xpath(".//div[@class='DyListCover-userName']").text
            item["img"] = li.find_element_by_xpath(".//div[@class='DyListCover-imgWrap']//img").get_attribute("src")
            item['class-name'] = li.find_element_by_xpath(".//span[@class='DyListCover-zone']").text
            item["click-hot"] = li.find_element_by_xpath(".//span[@class='DyListCover-hot']").text
            item["click-hot"] = re.sub(r'\n','',item['click-hot'])
          
            # 保存数据
            self.save_csv(item)
      
        # 返回是否有下一页和下一页的点击事件的标签,
        return next_page,is_next_url

    def save_csv(self,item):
        # 将提取存放到csv文件中的内容连接为csv格式文件
        str = ','.join([i for i in item.values()])

        with open('./douyu.csv','a',encoding='utf-8') as f:
            if self.start_csv:
                f.write("用户id,image,所属类,点击热度\n")
                self.start_csv = False
            # 将字符串写入csv文件
            f.write(str)
            f.write('\n')
        print("save success")

    def run(self):
        # 启动chrome并定位到相应页面
        self.driver.get(self.start_url)

        while True:
            # 开始提取数据,并获取下一页的元素
            next_page,is_next = self.get_content()
            if is_next!='false':
                break
            # 点击下一页
            next_page.click()

if __name__=='__main__':
    douyu_spider = Douyu()
    douyu_spider.run()
```

## 学习翻页代码2: *获取滚轮，分页向下滑动直至最底部，加载出图片*

```text
def pulldown(driver):
    """
    获取滚轮，分页向下滑动直至最底部，加载出图片
    """
    t = True
    while t:
        check_height = driver.execute_script("return document.body.scrollHeight;")
        for r in range(20):
            # t = random.uniform(1, 2)
            time.sleep(0.8)
            driver.execute_script("window.scrollBy(0,1500)")
        check_height1 = driver.execute_script("return document.body.scrollHeight;")
        if check_height == check_height1:
            t = False
```

## 学习翻页代码3: while 查找下一页，不见则退出。

```python3
import time
import urllib.parse
from selenium import webdriver

# option=webdriver.ChromeOptions()
# option.add_argument("headless")
# driver = webdriver.Chrome(options=option)
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
kw="衣服"
url="https://s.taobao.com/search?q={kw}".format(kw=urllib.parse.quote(kw))
driver.get(url)
js="window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)

main_driver=driver.current_window_handle

while True:
    time.sleep(2)
    goods=driver.find_elements_by_xpath('//div[contains(@class,"J_MouserOnverReq")]')
    for good in goods:
        price=good.find_element_by_xpath('.//div[2]/div[1]/div/strong').text
        title=good.find_element_by_xpath('.//div[2]/div[2]/a').text
        shop_name=good.find_element_by_xpath('.//div[2]/div[3]/div[1]/a/span[2]').text
        origin=good.find_element_by_xpath('.//div[2]/div[3]/div[2]').text
        good.click()
        driver.switch_to.window(driver.window_handles[-1])
        js="window.scrollTo(0,1000)"
        driver.execute_script(js)
        time.sleep(1)
        try:
            tag_standard = WebDriverWait(driver, 5, 0.2).until(lambda x:x.find_element_by_xpath('//*[@id="J_TabBar"]/li[2]/a'))
        except:
            tag_standard=None
        if tag_standard:
            tag_standard.click()
            try:
                tag_table = driver.find_element_by_xpath('//table[@class="tm-tableAttr"]')
                good_info = tag_table.text
            except:
                good_info=None
            print(good_info)
            driver.close()
            driver.switch_to.window(main_driver)

    try:
        next_page = WebDriverWait(driver, 3, 0.2).until(lambda x: x.find_element_by_xpath('//span[contains(text(),"下一页")]/..'))
    except Exception as e:
        print(e)
        break
    else:
        next_page.click()
driver.quit()
```

翻页方法4：输入页码点确定进行翻页

```text
import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq

'''
wait.until()语句是selenum里面的显示等待，wait是一个WebDriverWait对象，它设置了等待时间，如果页面在等待时间内
没有在 DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常,也可以说程序每隔xx秒看一眼，如果条件
成立了，则执行下一步，否则继续等待，直到超过设置的最长时间，然后抛出TimeoutException
1.presence_of_element_located 元素加载出，传入定位元组，如(By.ID, 'p')
2.element_to_be_clickable 元素可点击
3.text_to_be_present_in_element 某个元素文本包含某文字
'''
# 定义一个无界面的浏览器
browser = webdriver.PhantomJS(
    service_args=[
        '--load-images=false',
        '--disk-cache=true'])
# 10s无响应就down掉
wait = WebDriverWait(browser, 10)
#虽然无界面但是必须要定义窗口
browser.set_window_size(1400, 900)


def search():
    '''
    此函数的作用为完成首页点击搜索的功能，替换标签可用于其他网页使用
    :return:
    '''
    print('正在搜索')
    try:
        #访问页面
        browser.get('https://www.taobao.com')
        # 选择到淘宝首页的输入框
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        #搜索的那个按钮
        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        #send_key作为写到input的内容
        input.send_keys('面条')
        #执行点击搜索的操作
        submit.click()
        #查看到当前的页码一共是多少页
        total = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        #获取所有的商品
        get_products()
        #返回总页数
        return total.text
    except TimeoutException:
        return search()


def next_page(page_number):
    '''
    翻页函数，
    :param page_number:
    :return:
    '''
    print('正在翻页', page_number)
    try:
        #这个是我们跳转页的输入框
        input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
        #跳转时的确定按钮
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '#mainsrp-pager > div > div > div > div.form > span.J_Submit')))
        #清除里面的数字
        input.clear()
        #重新输入数字
        input.send_keys(page_number)
        #选择并点击
        submit.click()
        #判断当前页是不是我们要现实的页
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR,
                 '#mainsrp-pager > div > div > div > ul > li.item.active > span'),
                str(page_number)))
        #调用函数获取商品信息
        get_products()
    #捕捉超时，重新进入翻页的函数
    except TimeoutException:
        next_page(page_number)


def get_products():
    '''
    搜到页面信息在此函数在爬取我们需要的信息
    :return:
    '''
    #每一个商品标签，这里是加载出来以后才会拿网页源代码
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    #这里拿到的是整个网页源代码
    html = browser.page_source
    #pq解析网页源代码
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        # print(item)
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)


def main():
    try:
        #第一步搜索
        total = search()
        #int类型刚才找到的总页数标签，作为跳出循环的条件
        total = int(re.compile('(\d+)').search(total).group(1))
        #只要后面还有就继续爬，继续翻页
        for i in range(2, total + 1):
            next_page(i)
    except Exception:
        print('出错啦')
    finally:
        #关闭浏览器
        browser.close()


if __name__ == '__main__':
    main()
```

翻页方法五：先获取最大页码，然后用for page in range(max_page)进行

```python3
    # coding=utf-8
    import os
    import time
    from selenium import webdriver
   
    #打开火狐浏览器 需要V47版本以上的
    driver = webdriver.Firefox()#打开火狐浏览器
    url = "http://codelife.ecit-it.com"#这里打开我的博客网站
    driver.get(url)#设置火狐浏览器打开的网址
    time.sleep(2)
   
    #使用xpath进行多路径或多元素定位,用法看官网http://selenium-python.readthedocs.io/locating-elements.html
    elem_dh = driver.find_elements_by_xpath("//div[@class='pagination pagination-large']/ul/li/a")
    print ("我是刚获取的翻页按钮的路径数组:",elem_dh)
    print ("下一页按钮元素："，elem_dh[2])
    time.sleep(5)
   
    #获取当前窗口句柄
    now_handle = driver.current_window_handle #获取当前窗口句柄
    print ("我是当前窗口的句柄:",now_handle)#打印窗口句柄 是一串数字
    time.sleep(10)
   
    #循环获取界面
    for elem in elem_dh:
      print ("我是翻页按钮上的文本信息:",elem.text)          #获取元素的文本值
      print ("我是翻页按钮的地址",elem.get_attribute('href'))  #获取元素的href属性值
      elem.click()#点击进入新的界面 _blank弹出
      print ("刚翻页完成了！")
   
    time.sleep(20)
```
