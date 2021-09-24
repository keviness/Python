python的强大之处就在于有许多已经写好的功能库提供，这些库强大且易用，对于写一些有特定功能的小程序十分方便。

现在就用pyhton的selenium+谷歌游览器写一个可以自动刷课的程序，以智慧树上的网课为例。

原理说明：selenium 是一套完整的web应用程序测试系统，可以模拟真实游览器，支持多种游览器。简单来说就是可以定位到html元素，比如按钮，输入框之类的，然后模拟点击，模拟输入等从而实现自动化效果。selenium难点在于定位元素。

selenium的一些基本用法：

[https://blog.csdn.net/weixin_36279318/article/details/79475388](https://blog.csdn.net/weixin_36279318/article/details/79475388)

一 .开始之前准备

1.安装selenium：在cmd窗口输入：pip isntaller selenium

2.下载谷歌游览器的驱动chromedriver：[https://pan.baidu.com/s/1_wopkNwvmKvqLlNxY_EagQ](https://pan.baidu.com/s/1_wopkNwvmKvqLlNxY_EagQ)  (7yxk)

3.安装一个谷歌游览器，最好是最新版的

二.分析网站

要定位元素就要分析网站的一些元素的源代码是如何写的。

1.智慧树的登陆页面

![](https://img2018.cnblogs.com/blog/1330717/201906/1330717-20190623084251179-1656334932.jpg)![](https://img2018.cnblogs.com/blog/1330717/201906/1330717-20190623084344387-884618867.jpg)

2.用谷歌游览器的审查元素功能查看元素的源代码

按右键选择审查或按F12,得到如下的页面

![](https://img2018.cnblogs.com/blog/1330717/201906/1330717-20190623084702284-616816285.jpg)

可以看到输入手机号那一个输入框有一个id选择器，这样就可以根据id选择器的名字定位到这个元素。

其它元素也可以用同样的方法定位元素，然后根据具体情况选择不同的定位方式。

![](https://img2018.cnblogs.com/blog/1330717/201906/1330717-20190623090545485-1287948221.gif)

3.写代码


```
  1 from selenium import webdriver
  2 
  3 import time
  4 import threading
  5 
  6 browser=webdriver.Chrome()
  7 #请求登陆页面
  8 browser.get('https://passport.zhihuishu.com/login?service=http://online.zhihuishu.com/onlineSchool/')
  9 
 10 #登陆
 11 def login(number,password):
 12     phone_number=browser.find_element_by_id('lUsername')#通过id定位，手机号码
 13     pwd=browser.find_element_by_id('lPassword')#密码
 14     login_btn=browser.find_element_by_class_name('wall-sub-btn')#登陆按钮
 15 
 16     phone_number.send_keys(number)#输入手机号码
 17     pwd.send_keys(password)#输入密码
 18     login_btn.click()#点击登陆按钮
 19 
 20 #转到播放视频页面
 21 def to_course(key):
 22 
 23     time.sleep(5)
 24     current=browser.current_window_handle#当前页面的句柄
 25     key=browser.find_element_by_partial_link_text(key)#找到课程
 26     key.click()#跳转到播放视频页面
 27     time.sleep(1)#等待页面加载
 28     #因为跳转到新的页面，所以browser要切换到新的页面操作
 29     handles=browser.window_handles
 30     for handle in handles:
 31         if handle!=current:
 32             browser.switch_to.window(handle)
 33   
 34     time.sleep(10)
 35     try:
 36         video=browser.find_element_by_id('mediaplayer')#定位视频窗口
 37         video.click()#点击播放
 38     except:
 39         pass
 40   
 41 
 42 
 43 #判断是否有答题窗口弹出
 44 def is_exist():
 45     while True:
 46         try:
 47             browser.switch_to.default_content()
 48             browser.switch_to.frame('tmDialog_iframe')#答题窗口在另一个frame里面，要切换
 49             box=browser.find_elements_by_class_name('answerOption')#答题列表
 50             radio=box[0].find_element_by_tag_name('input')#找到第一个选项
 51             radio.click()#选择
 52             browser.switch_to.default_content()
 53             browser.find_element_by_link_text('关闭').click()#关闭答题窗口
 54         except:
 55             browser.switch_to.parent_frame()#没有弹出，切换回本来的frame
 56         time.sleep(5)
 57 
 58 #判断当前视频是否结束
 59 def is_end():
 60     while True:
 61         try:
 62             video=browser.find_element_by_id('mediaplayer')#定位视频窗口
 63             #获取当前播放的进度
 64             current_time=video.find_element_by_class_name('currentTime').get_attribute('textContent')
 65             #该视频的总时间
 66             total_time=video.find_element_by_class_name('duration').get_attribute('textContent')
 67             print(current_time,total_time)
 68             if current_time==total_time:
 69                 #当前视频播放结束，点击下一节
 70                 js="document.ElementById('nextBtn').click()"#js脚本
 71                 browser.execute_script(js)
 72               
 73             time.sleep(10)#10秒检测一次
 74         except:
 75             current_time='00:00'
 76             total_time='00:01'
 77     
 78           
 79       
 80 if __name__=='__main__':
 81   
 82     '''
 83     number=''#手机号码
 84     password=''#密码
 85     key=''#课程名称，可以部分名字
 86         
 87     '''
 88     login(number,password)
 89     to_course(key)
 90     #开两个线程
 91     t1=threading.Thread(target=is_exist)
 92     t2=threading.Thread(target=is_end)
 93     t2.start()
 94     time.sleep(3)
 95     t1.start()
 96     t2.join()
 97     t1.join()
 98 
 99 
100 
101   
```

登陆过程:

![](https://img2018.cnblogs.com/blog/1330717/201906/1330717-20190623115653724-395338092.gif)

---

这个程序只是做一个简单的演示，并没有做到很全面，但也可以用的。

selenium定位不到元素时会报错，要处理好，否则程序就没用了。元素定位最好使用WebDriverWait的方式，加上异常控制。

网站是会变化的，分析好网站操作基本的过程，基本没有问题了。

selenium定位不到元素有以下几种情况

1.通过class定位时，有时定位不到

2.页面没有加载出来，元素无法定位

3.元素不可见，无法定位

4.元素被其它元素遮挡了

5.方法用错了
