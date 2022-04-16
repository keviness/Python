import re
import os, base64
result = re.search("data:image/(?P<ext>.*?);base64,(?P<data>.*)", src, re.DOTALL)
if result:
    ext = result.groupdict().get("ext")
    data = result.groupdict().get("data")

img_str = 'abcdefgh12345oK'
img_data = base64.b64decode(img_str)
# 注意：如果是"data:image/jpg:base64,"，那你保存的就要以png格式，如果是"data:image/png:base64,"那你保存的时候就以jpg格式。
with open('001.png', 'wb') as f:
      f.write(img_data)