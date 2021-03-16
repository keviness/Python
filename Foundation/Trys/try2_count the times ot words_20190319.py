#try_count the times of the words_20190319
import jieba
f = open("字体安装方法.txt", "r")
txt = f.read()
f.close()
for ch in '!"#$%*+-<>=?/:().':
    txt = txt.replace(ch, " ")
words = jieba.lcut(txt)
dct = {}
for word in words:
    if word == 1:
        continue
    else:
        dct[word] = dct.get(word, 0) + 1
item = list(dct.items())
item.sort(key = lambda x : x[1], reverse = True)
for i in range(13):
    word, count = item[i]
    print("{0:<10} {1:>5}".format(word, count))
