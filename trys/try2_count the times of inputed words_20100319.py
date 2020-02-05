#try_count the times of words which input_20190319
def deal_inputtxt(txt):
    for ch in '!;"$@;:?><。，':
        txt = txt.replace(ch, " ")
    words = txt.split()
    return words
def count_times(txt):
    new_words = deal_inputtxt(txt)
    dct = {}
    for word in new_words:
        if word == 1:
            continue
        else:
            dct[word] = dct.get(word, 0) + 1
    item = list(dct.items())
    item.sort(key = lambda x: x[1], reverse = True)
    for i in range(5):
        ite, count = item[i]
        print("{0: <3} {1: >3}".format(ite, count))
def main():
    txt = input("Enter something you want to say:")
    deal_inputtxt(txt)
    count_times(txt)
main()
        

    
    
    
