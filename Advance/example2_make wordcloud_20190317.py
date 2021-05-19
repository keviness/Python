#example2_make worldcloud_20190317
from wordcloud import WordCloud
import jieba
txt = "i am a Chinese,我是一个中国人，我自小生长在中国，中国是一个伟大的母亲，她哺育了我。啊！母亲。啊！中国。中国加油！"
words = jieba.lcut(txt)
new_words = "".join(words)
wordcloud = WordCloud(font_path = "simsun", background_color = "red",max_font_size = 80).generate(new_words)
wordcloud.to_file("make woldcloud.png")
