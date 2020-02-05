#try2_make wordcloud3_20190318
import jieba
from wordcloud import WordCloud
f = open("字体安装方法.txt", "r")
words = f.read()
f.close()
new_words = jieba.lcut(words)
count = {}
for word in new_words:
    if len(word):
        continue
    else:
        count[word] = count.get(word, 0) +1
dct = list(count.items())
dct.sort(key = lambda x : x[1], reverse = True)
for i in range(15):
    word, count = dct[i]
    print("{0:<10} {1:>5}".format(word, count))
    
