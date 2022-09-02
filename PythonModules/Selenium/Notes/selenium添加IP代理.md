# 1.设置user-agent

```Python
    option = ChromeOptions()
    #设置无头模式
    option.add_argument("--headless")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    #设置user-agent
    option.add_argument('user-agent=ywy')
    driver = webdriver.Chrome(options=option)
```

# 2.通过user-agent池替换user-agent

```Python
pip install fake_useragent
 
from fake_useragent import UserAgent
 
headers = {
‘User-Agent’: UserAgent().random,
}
```

# 3.设置代理ip

## 3.1 连接无用户名密码认证的代理

```Python
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--proxy-server=http://ip:port')  
driver = webdriver.Chrome(chrome_options=chromeOptions)
```

## 3.2有用户名和密码的连接

```Python
from selenium import webdriver
def create_proxyauth_extension(proxy_host, proxy_port,
                               proxy_username, proxy_password,
                               scheme='http', plugin_path=None):
    """Proxy Auth Extension

    args:
        proxy_host (str): domain or ip address, ie proxy.domain.com
        proxy_port (int): port
        proxy_username (str): auth username
        proxy_password (str): auth password
    kwargs:
        scheme (str): proxy scheme, default http
        plugin_path (str): absolute path of the extension     

    return str -> plugin_path
    """
    import string
    import zipfile
 
    if plugin_path is None:
        plugin_path = 'd:/webdriver/vimm_chrome_proxyauth_plugin.zip'
 
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """
 
    background_js = string.Template(
    """
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "${scheme}",
                host: "${host}",
                port: parseInt(${port})
              },
              bypassList: ["foobar.com"]
            }
          };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "${username}",
                password: "${password}"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """
    ).substitute(
        host=proxy_host,
        port=proxy_port,
        username=proxy_username,
        password=proxy_password,
        scheme=scheme,
    )
    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
 
    return plugin_path
 
proxyauth_plugin_path = create_proxyauth_extension(
    proxy_host="proxy.crawlera.com",
    proxy_port=8010,
    proxy_username="username",
    proxy_password="password"
)
 
 
co = webdriver.ChromeOptions()
co.add_argument("--start-maximized")
co.add_extension(proxyauth_plugin_path)
 
 
driver = webdriver.Chrome(chrome_options=co)
driver.get("http://www.amazon.com/")
```

# 4. [Selenium chrome配置不加载图片](https://www.cnblogs.com/roystime/p/6935585.html)

```Python
prefs = {"profile.managed_default_content_settings.images":2}
chrome_options.add_experimental_option("prefs",prefs)
```
