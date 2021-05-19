import jieba
fi = open("射雕英雄传-网络版.txt", "r", encoding='utf-8')
txt = fi.read()
fi.close()
ls = jieba.lcut(txt)
d = {}
for w in ls:
    d[w] = d.get(w, 0) + 1
for x in " \n，。！“”：":
    del d[x]
rst = []
for i in range(8):
    mx = 0
    mxj = 0
    for j in d:
        if d[j] > mx:
            mx = d[j]
            mxj = j
    rst.append(mxj)
    del d[mxj]
print("，".join(rst))
