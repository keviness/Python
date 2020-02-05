#try2_make wordcloud2_20190318
import jieba
from wordcloud import WordCloud
f = open("字体安装方法.txt")
txt = f.read()
f.close()
words = jieba.lcut(txt)
new_words = "".join(words)
wordcloud = WordCloud(background_color = "blue", font_path = "MSYH.ttc").generate(new_words)
wordcloud.to_file("字体安装方法wordcloud.png")
