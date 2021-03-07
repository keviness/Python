#t2
string = input("string:")
d = {}
for w in string:
    d[w] = d.get(w, 0)+1
item = list(d.items())
item.sort(key=lambda x:x[1], reverse=True)
for i in range(4):
    word, count = item[i]
    print("{0}  {1}".format(word, count))
