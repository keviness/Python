最近开发自动化测试工具，遇到了3种情况，selenium在操作页面元素，进行点击的时候，元素可以找到，但是点击没有反应的情况。

在开始前一定要确认元素可以找到!

第一种：元素里有href属性，属性为JavaScript。这类元素需要用js点击。

操作代码：

```
          driver= new InternetExplorerDriver();

          Element el = driver.findElement(By.xpath(“.//*[@id='menu']/div/ul/li[1]/a”))

          JavascriptExecutor js = (JavascriptExecutor) driver;

          js.executeScript("arguments[0].click();",el);
```

第二种：元素里有href属性，属性为超链接。这类元素无法点击时，需要获得元素连接，执行打开这个连接地址。


操作代码：

```
             driver= new InternetExplorerDriver();

             Element el = driver.findElement(By.xpath(“.//*[@id='contentul']/li[1]/div/div[1]/a”))

             String url = el.getAttribute("href");

             driver.get(url);
```

第三种：元素属性正常，没有特殊标签，但是click()就是无法点击，这时需要给元素进行Enter操作。


操作代码：

```
          driver= new InternetExplorerDriver();

             Element el = driver.findElement(By.xpath(“.//*[@id='payMobileConfirm']”))

          el.sendKeys(Keys.ENTER);
```
