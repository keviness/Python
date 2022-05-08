# 使用Selenium Webdriver下载时命名文件

我看到你可以通过Webdriver设置下载文件的位置，如下所示：

```python
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir",getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
browser = webdriver.Firefox(firefox_profile=fp)
```

但是，我想知道是否有类似的方式来给文件下载时的名称？最好是，可能不是与配置文件相关的东西，因为我将通过一个浏览器实例下载约6000个文件，并且不希望为每次下载重新启动驱动程序。---

编辑：所选答案建议的代码解决方案。每次下载后重命名文件。

```python
import os
os.chdir(SAVE_TO_DIRECTORY)
files = filter(os.path.isfile, os.listdir(SAVE_TO_DIRECTORY))
files = [os.path.join(SAVE_TO_DIRECTORY, f) for f in files] # add path to each file
files.sort(key=lambda x: os.path.getmtime(x))
newest_file = files[-1]
os.rename(newest_file, docName+".pdf")
```
