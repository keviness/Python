# Requests库详解

由于最近工作中，与同事对接模拟手机浏览器进行广告模拟跳转。又一次接触用到爬虫的知识，以前用过urllib + bs4 + selenium定向爬取网易一元夺宝的商品信息保存在数据库中，当时，还是太年轻，对爬虫不是很了解，对爬虫的robots协议也不知道。现在重新梳理一下爬虫的知识。争取写一个系列，大致内容顺序是requests, bs4,re, scrapy, selenium等。
在介绍requests库之前，先介绍以下基本的http概念,
下面内容是在上 `嵩天教授`课程笔记整理。在这里感谢他。

![](https://upload-images.jianshu.io/upload_images/1293367-2dcea888c99170c8.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

追寻

#### HTTP协议

HTTP,超文本传输协议（HTTP，HyperText Transfer Protocol)是互联网上应用最为广泛的一种网络协议。所有的WWW文件都必须遵守这个标准。设计HTTP最初的目的是为了提供一种发布和接收HTML页面的方法,HTTP是一种基于"请求与响应"模式的、无状态的应用层协议。HTTP协议采用URL作为定位网络资源的的标识符。
`http://host[:post][path]`
`host`:合法的Internet主机域名或ip地址
`port`:端口号，缺省为80
`path`:请求资源的路径

HTTP URl的理解:
url是通过HTTP协议存取资源的的Internet路径，一个URL对应一个数据资源

HTTP协议对资源的操作

| 方法   | 说明                                                    |
| ------ | ------------------------------------------------------- |
| GET    | 请求获取URL位置的资源                                   |
| HEAD   | 请求获取URL位置资源的响应消息报告，即获得资源的头部信息 |
| POST   | 请求向URL位置的资源后附加新的消息                       |
| PUT    | 请求向URL位置存储一个资源，覆盖原URL位置的资源          |
| PATCH  | 请求局部更新URL位置的资源,即改变该处资源的部分内容      |
| DELETE | 请求删除URL位置存储的资源                               |

以上方法中，`GET`,`HEAD`是从服务器获取信息到本地，`PUT`,`POST`,`PATCH`,`DELETE`是从本地向服务器提交信息。通过URL和命令管理资源，操作独立无状态，网络通道及服务器成了黑盒子。
[文档](https://link.jianshu.com/?t=http://cn.python-requests.org/zh_CN/latest/)

### 安装

```powershell
pip install requests
```

#### requests库安装小测

```python
import request
url = 'https://www.baidu.com'
r = requests.get(url)
r.encoding = r.apparent_encoding
print(r.text[-200:])

Out[13]: 'w.baidu.com/duty/>使用百度前必读</ a>  < a href= >意见反馈</ a> 京ICP证030173号  < img src=//www.baidu.com/img/gs.gif> </p > </div> </div> </div> </body> </html>\r\n'
```

### requests库7个主要方法

| 方法             | 说明                                                      |
| ---------------- | --------------------------------------------------------- |
| requsts.requst() | 构造一个请求，最基本的方法，是下面方法的支撑              |
| requsts.get()    | 获取网页，对应HTTP中的GET方法                             |
| requsts.post()   | 向网页提交信息，对应HTTP中的POST方法                      |
| requsts.head()   | 获取html网页的头信息，对应HTTP中的HEAD方法                |
| requsts.put()    | 向html提交put方法，对应HTTP中的PUT方法                    |
| requsts.patch()  | 向html网页提交局部请求修改的的请求，对应HTTP中的PATCH方法 |
| requsts.delete() | 向html提交删除请求，对应HTTP中的DELETE方法                |

#### requests.get()

`r = requests.get(url)`
`r`:是一个 `Response`对象，一个包含服务器资源的对象
`.get(url)`:是一个 `Request`对象，构造一个向服务器请求资源的Request。

```powershell
In [4]: type(requests.get(url))
Out[4]: requests.models.Response
```

下面看一下源码:

```python
def get(url, params=None, **kwargs):
    kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, **kwargs) #返回一个request对象

＃　request对象，另外,method参数就是修改http方法
def request(method, url, **kwargs):
    with sessions.Session() as session:
        return session.request(method=method, url=url, **kwargs)
    
class Session(SessionRedirectMixin):
....
    # session的reqeust方法
    def request(self, method, url,
        params=None,
        data=None,
        headers=None,
        cookies=None,
        files=None,
        auth=None,
        timeout=None,
        allow_redirects=True,
        proxies=None,
        hooks=None,
        stream=None,
        verify=None,
        cert=None,
        json=None):
        #　构造一个Request对象.
        req = Request(
            method = method.upper(),
            url = url,
            headers = headers,
            files = files,
            data = data or {},
            json = json,
            params = params or {},
            auth = auth,
            cookies = cookies,
            hooks = hooks,
        )
        prep = self.prepare_request(req)

        proxies = proxies or {}

        settings = self.merge_environment_settings(
            prep.url, proxies, stream, verify, cert
        )

        # Send the request.
        send_kwargs = {
            'timeout': timeout,
            'allow_redirects': allow_redirects,
        }
        send_kwargs.update(settings)
        resp = self.send(prep, **send_kwargs)

        return resp
```

#### get方法参数

`request.get(url,params=None,**kwargs)`
从上面的源码也可以知道，解释一下参数含义
`url`: 获取html的网页的url
`params`:url中的额外的参数，字典或字节流格式，可选
`**kwargs`:　12个控制访问的参数

#### Requests中两个重要的对象

`r = requests.get(url)`
`r`:是一个 `Response`对象，一个包含服务器资源的对象,Request对象包含爬虫返回的内容。
`.get(url)`:是一个 `Request`对象，构造一个向服务器请求资源的Request。
x下面用例子看一下，返回的对象包含的内容

```powershell
In [5]: type(r)  ＃打印类型
Out[5]: requests.models.Response

In [6]: dir(r)　＃显示具有的属性和方法
Out[6]: 
['__attrs__',
 '__bool__',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__init__',
 '__iter__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__nonzero__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__setstate__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_content',
 '_content_consumed',
 'apparent_encoding',
 'close',
 'connection',
 'content',
 'cookies',
 'elapsed',
 'encoding',
 'headers',
 'history',
 'is_permanent_redirect',
 'is_redirect',
 'iter_content',
 'iter_lines',
 'json',
 'links',
 'ok',
 'raise_for_status',
 'raw',
 'reason',
 'request',
 'status_code',
 'text',
 'url']
```

列出几个重要的属性：

| 属性                | 说明                                         |
| ------------------- | -------------------------------------------- |
| r.status_code       | HTTP请求返回状态码，200表示成功              |
| r.text              | HTTP响应的字符串形式，即，url对应的页面内容  |
| r.encoding          | 从HTTP　header中猜测的响应内容的编码方式     |
| r.apparent_encoding | 从内容中分析响应内容的编码方式(备选编码方式) |
| r.content           | HTTP响应内容的二进制形式                     |

`理解Response编码`
`r.encoding`:如果header中不存在charset,则认为编码是ISO-8859-1,`r.text`根据 `r.encoding`显示网页内容
`r.apparent_encoding`:根据网页内容分析处的编码方式可以看做是 `r.encoding`的备选

```python
response = requests.get('http://www.jianshu.com/')
# 获取响应状态码
print(type(response.status_code),response.status_code)
# 获取响应头信息
print(type(response.headers),response.headers)
# 获取响应头中的cookies
print(type(response.cookies),response.cookies)
# 获取访问的url
print(type(response.url),response.url)
# 获取访问的历史记录
print(type(response.history),response.history)
```

#### 理解requests库的异常

网络链接有风险，异常处理很重要

| 异常                      | 说明                                    |
| ------------------------- | --------------------------------------- |
| requests.ConnectionError  | 网络连接异常，如DNS查询失败，拒绝连接等 |
| requests.HTTPError        | HTTP错误异常                            |
| requests.URLRequired      | URL缺失异常                             |
| requests.TooManyRedirects | 超过最大重定向次数，产生重定向异常      |
| requests.ConnectTimeout   | 连接远程服务器超时异常                  |
| requests.Timeout          | 请求URL超时，产生超时异常               |

```python
import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException

try:
  response = requests.get("http://httpbin.org/get", timeout = 0.5)
          print(response.status_code)
except ReadTimeout:
  # 超时异常
  print('Timeout')
except ConnectionError:
  # 连接异常
  print('Connection error')
except RequestException:
  # 请求异常
  print('Error')
```

#### 理解Response的异常

`r.raise_for_status()`
如果 `status_code`不是200,产生异常requests.HTTPError

r.raise_for_status()方法内部判断r.status_code是否等于200不需要增加额外的if语句，该语句便于利用try-except进行异常处理。
`raise_for_status`源码

```python
   def raise_for_status(self):
       """Raises stored :class:`HTTPError`, if one occurred."""

       http_error_msg = ''
       if isinstance(self.reason, bytes):
           # We attempt to decode utf-8 first because some servers
           # choose to localize their reason strings. If the string
           # isn't utf-8, we fall back to iso-8859-1 for all other
           # encodings. (See PR #3538)
           try:
               reason = self.reason.decode('utf-8')
           except UnicodeDecodeError:
               reason = self.reason.decode('iso-8859-1')
       else:
           reason = self.reason

       if 400 <= self.status_code < 500:
           http_error_msg = u'%s Client Error: %s for url: %s' % (self.status_code, reason, self.url)

       elif 500 <= self.status_code < 600:
           http_error_msg = u'%s Server Error: %s for url: %s' % (self.status_code, reason, self.url)

       if http_error_msg:
           raise HTTPError(http_error_msg, response=self)

```

#### requests内置的状态字符

```python
# -*- coding: utf-8 -*-

from .structures import LookupDict

_codes = {

    # Informational.
    100: ('continue',),
    101: ('switching_protocols',),
    102: ('processing',),
    103: ('checkpoint',),
    122: ('uri_too_long', 'request_uri_too_long'),
    200: ('ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\\o/', '✓'),
    201: ('created',),
    202: ('accepted',),
    203: ('non_authoritative_info', 'non_authoritative_information'),
    204: ('no_content',),
    205: ('reset_content', 'reset'),
    206: ('partial_content', 'partial'),
    207: ('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'),
    208: ('already_reported',),
    226: ('im_used',),

    # Redirection.
    300: ('multiple_choices',),
    301: ('moved_permanently', 'moved', '\\o-'),
    302: ('found',),
    303: ('see_other', 'other'),
    304: ('not_modified',),
    305: ('use_proxy',),
    306: ('switch_proxy',),
    307: ('temporary_redirect', 'temporary_moved', 'temporary'),
    308: ('permanent_redirect',
          'resume_incomplete', 'resume',),  # These 2 to be removed in 3.0

    # Client Error.
    400: ('bad_request', 'bad'),
    401: ('unauthorized',),
    402: ('payment_required', 'payment'),
    403: ('forbidden',),
    404: ('not_found', '-o-'),
    405: ('method_not_allowed', 'not_allowed'),
    406: ('not_acceptable',),
    407: ('proxy_authentication_required', 'proxy_auth', 'proxy_authentication'),
    408: ('request_timeout', 'timeout'),
    409: ('conflict',),
    410: ('gone',),
    411: ('length_required',),
    412: ('precondition_failed', 'precondition'),
    413: ('request_entity_too_large',),
    414: ('request_uri_too_large',),
    415: ('unsupported_media_type', 'unsupported_media', 'media_type'),
    416: ('requested_range_not_satisfiable', 'requested_range', 'range_not_satisfiable'),
    417: ('expectation_failed',),
    418: ('im_a_teapot', 'teapot', 'i_am_a_teapot'),
    421: ('misdirected_request',),
    422: ('unprocessable_entity', 'unprocessable'),
    423: ('locked',),
    424: ('failed_dependency', 'dependency'),
    425: ('unordered_collection', 'unordered'),
    426: ('upgrade_required', 'upgrade'),
    428: ('precondition_required', 'precondition'),
    429: ('too_many_requests', 'too_many'),
    431: ('header_fields_too_large', 'fields_too_large'),
    444: ('no_response', 'none'),
    449: ('retry_with', 'retry'),
    450: ('blocked_by_windows_parental_controls', 'parental_controls'),
    451: ('unavailable_for_legal_reasons', 'legal_reasons'),
    499: ('client_closed_request',),

    # Server Error.
    500: ('internal_server_error', 'server_error', '/o\\', '✗'),
    501: ('not_implemented',),
    502: ('bad_gateway',),
    503: ('service_unavailable', 'unavailable'),
    504: ('gateway_timeout',),
    505: ('http_version_not_supported', 'http_version'),
    506: ('variant_also_negotiates',),
    507: ('insufficient_storage',),
    509: ('bandwidth_limit_exceeded', 'bandwidth'),
    510: ('not_extended',),
    511: ('network_authentication_required', 'network_auth', 'network_authentication'),
}

codes = LookupDict(name='status_codes')

for code, titles in _codes.items():
    for title in titles:
        setattr(codes, title, code)
        if not title.startswith('\\'):
            setattr(codes, title.upper(), code)
```

以上的方法特别好，可以借鉴使用在自己项目中进行数据映射转换。
`reqeust.codes`可以使用属性方式去访问。如：

```python
print(requests.codes.ok)
200
print(requests.codes.unordered_collection)
425
type(requests.codes.not_extended)
Out[15]: int
print(requests.codes.not_extended)
510
```

##### 爬取网页的通用代码框架

```python
# coding: utf8

import requests


def get_html(url, params):
    try:
        r = requests.get(url, params)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "raise exception"


if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(get_html(url))
```

#### Requests库中的head()方法

![](https://upload-images.jianshu.io/upload_images/1293367-471cc45a78f5c1d0.gif?imageMogr2/auto-orient/strip|imageView2/2/w/850/format/webp)

head

#### Requests库中的post()方法

![](https://upload-images.jianshu.io/upload_images/1293367-9af1352d32a21888.gif?imageMogr2/auto-orient/strip|imageView2/2/w/850/format/webp)

post

```python
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {     #post提交的data是一个字典的
    "key1": "youdi", # 就会格式化成一个form
    "king": "youdi", 
    "value": "the one"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "35", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.13.0"
  }, 
  "json": null, 
  "origin": "183.240.20.24", 
  "url": "http://httpbin.org/post"
}


{
  "args": {}, 
  "data": "ABCDEFG",  # post提交的data是字符串 ，编码为data
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "7", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.13.0"
  }, 
  "json": null, 
  "origin": "183.240.20.24", 
  "url": "http://httpbin.org/post"
}
```

#### Requests库中的put()方法

![](https://upload-images.jianshu.io/upload_images/1293367-aa2a57fb5e965042.gif?imageMogr2/auto-orient/strip|imageView2/2/w/850/format/webp)

put

#### requests库主要方法解析

`requests.request(method, url, **kwagrs)`

* method:　请求方式，对应get/put/post等7种方法
* url: 获取页面的url链接
* **kwargs:　控制访问的参数，共有13个

`method`:请求方式

```python
r = requests.request(method='GET', url=url, **kwargs)
r = requests.get(url, **kwargs)
r = requests.request(method='HEAD', url=url, **kwargs)
r = requests.head(url, **kwargs)
r = requests.request(method='POST', url=url, **kwargs)
r = requests.post(url, **kwargs)
r = requests.request(method='PUT', url=url, **kwargs)
r = requests.put(url, **kwargs)
r = requests.request(method='PATCH', url=url, **kwargs)
r = requests.patch(url, **kwargs)
r = requests.request(method='DELETE', url=url, **kwargs)
r = requests.delete(url, **kwargs)
r = requests.request(method='OPTIONS', url=url, **kwargs)
r = requests.options(url, **kwargs)
```

`说明`：上面的方法和下面的方法达到的效果是一样的，就是做了一层封装，把比较常用的方法都抽出来，python中很多库都是这样做的。典型的就是matplotlib中模仿matlab使用最简单的method绘制目标图。这个内容后面会更新给大家。

`**kwargs`:控制访问的参数，均为可选项

> * params: 字典或字节序列，作为参数增加到url中
> * data:字典，字节序列或文件对象,作为Request的内容
> * json: JSON格式的数据，作为Request的内容
> * headers: 字典, HTTP定制头
> * cookie: 字典或CooKiJar, Request中的cookie
> * auth: 元祖，支持HTTP认证功能
> * files: 字典类型，传输文件
> * timeout: 设定超时时间，秒为单位
> * proxies: 字典类型，设定访问代理服务器，可以增加登录认证
> * allow_redirects: True/False,默认为True,重定向开关
>   stream: True/False，默认为True,获取内容立即下载开关
>   verity: True/False默认Ture,认证ssl证书开关
>   cert: 本地ssl证书路径

![](https://upload-images.jianshu.io/upload_images/1293367-562cba8bd9839c1a.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

远方 背影

下面逐一介绍

`params`
字典或字节序列，作为参数增加到url中

```powershell
In [36]: payload
Out[36]: {'key1': 'one', 'key2': 'two'}

In [37]: r = requests.request('GET', 'http://python123.io/ws', params=payload)

In [38]: print(r.url)
http://python123.io/ws?key1=one&key2=two
```

`data`
字典，字节序列或文件对象,作为Request的内容

```python
import requests
payload = {'key1':'one', 'key2':'two'}
url = 'http://httpbin.org/put'
r = requests.put(url=url, data=payload)
# or 
r = requests.put(url=url, data='ABCDEFG') #字符串
```

`json`
JSON格式的数据，作为Request的内容

```python
In [48]: kv = {'name': 'youdi', 'role': 'king', 'rank': 'the one'}

In [49]: url = 'http://httpbin.org/post'

In [50]: r = requests.request(method='POST', url=url, json=kv)

In [51]: print(r.text)
{
  "args": {}, 
  "data": "{\"role\": \"king\", \"rank\": \"the one\", \"name\": \"youdi\"}",  #json格式，其实就是字符串
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "52", 
    "Content-Type": "application/json", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.13.0"
  }, 
  "json": {
    "name": "youdi", 
    "rank": "the one", 
    "role": "king"
  }, 
  "origin": "183.60.175.16", 
  "url": "http://httpbin.org/post"
}
```

`headers`
字典, HTTP定制头部信息，隐藏爬虫信息，模拟浏览器的头部信息

```python
In [58]: url = 'http://httpbin.org/post'

In [59]: r = requests.request('POST', url)

# 头部信息
In [69]: r.request.headers
# 观察User-Agent
Out[69]: {'Accept': '*/*', 'User-Agent': 'python-requests/2.13.0', 'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '0'}


#加入headers后
In [62]: headers = { # 浏览器代理
    ...:      "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Ch
    ...: rome/57.0.2987.133 Safari/537.36"
    ...: }
In [63]: r = requests.request('POST', url, headers=headers)

In [71]: r.request.headers
Out[71]: {'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36', 'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '0'}
```

`cookie`
字典或CooKiJar, Request中的cookie

```python

#先获取百度的cookie
In [74]: r = requests.request('GET', 'https://www.baidu.com')

In [75]: r
Out[75]: <Response [200]>
# 保存在变量中
In [76]: cookie = r.cookies

# cookie类型
In [86]: type(cookie)
Out[86]: requests.cookies.RequestsCookieJar


In [77]: r_baidu = requests.request('POST', 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=old&rsv_pq=981edbe6000308e9&rsv_t=76c1VG%2B1PcKzCGSEjcf3W2zDn5ZcBnhR1TAe%2FcJ32OW62aKsa5DWo7YYsms&rqlang=cn&rsv_enter=1&rsv_sug3=2', cookie=cookie)
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=test&rsv_pq=981edbe6000308e9&rsv_t=76c1VG%2B1PcKzCGSEjcf3W2zDn5ZcBnhR1TAe%2FcJ32OW62aKsa5DWo7YYsms&rqlang=cn&rsv_enter=1&rsv_sug3=2 中 wd修改关键词 就是提交给百度进行搜索的内容
```

`auth`
元祖，支持HTTP认证功能

```python
import requests
# 最简单的http验证
from requests.auth import HTTPBasicAuth

r = requests.get('http://httpbin.org/auth', auth=HTTPBasicAuth('user', 'user'))
# r = requests.get('http://httpbin.org/auth', auth=('user', 'user'))
print(r.status_code)
```

`files`
字典类型，传输文件

```python
fs = {file: open('data.xls', 'rb')}
# 使用files参数就可以了
r = requests.request('POST','http://httpbin.org/post',files=fs)
```

`timesout`
设定超时时间，秒为单位

```python
import requests
from requests.exceptions import ReadTimeout

try:
  # 设置必须在500ms内收到响应，不然或抛出ReadTimeout异常
  response = requests.get("http://httpbin.org/get", timeout=0.5)
           print(response.status_code)
except ReadTimeout:
  print('Timeout')
```

`proxies`
字典类型，设定访问代理服务器，可以增加登录认证

```python
import requests

#普通代理
proxies = {
   "http": "http://127.0.0.1:1080",
   "https": "https://127.0.0.1:1080",
}
# 往请求中设置代理(proxies)
r = requests.get("https://www.taobao.com", proxies=proxies)
print(r.status_code)

# 带有用户名和密码的代理
proxies = {
   "http": "http://user:password@127.0.0.1:9743/",
}
r = requests.get("https://www.taobao.com", proxies=proxies)
print(r.status_code)

# 设置socks代理,翻墙必备
proxies = {
   'http': 'socks5://127.0.0.1:1080',
   'https': 'socks5://127.0.0.1:1080'
}
r = requests.get("https://www.google.com", proxies=proxies)
print(r.status_code)
```

`allow_redirects`
True/False,默认为True,重定向开关

```python
r = requests.request('GET','http://httpbin.org/get',allow_redirects=False)
```

`stream`
True/False，默认为True,获取内容立即下载开关

```python
r = requests.request('GET','http://httpbin.org/get/**.txt',stream=False)
```

`verity`
True/False默认Ture,认证ssl证书开关

```python
# 无证书访问
r = requests.get('https://www.12306.cn')
# 在请求https时，request会进行证书的验证，如果验证失败则会抛出异常
print(r.status_code)


# 关闭验证，但是仍然会报出证书警告
r = requests.get('https://www.12306.cn',verify=False)
print(r.status_code)

# 消除关闭证书验证的警告
from requests.packages import urllib3

# 关闭警告
urllib3.disable_warnings()
r = requests.get('https://www.12306.cn',verify=False)
print(r.status_code)
```

`cert`
本地ssl证书路径

```python
# 设置本地证书
r = requests.get('https://www.12306.cn', cert=('/home/youdi/Download/**.crt', '/hone/youdi/.ssh/**.key'))
print(r.status_code)
```
