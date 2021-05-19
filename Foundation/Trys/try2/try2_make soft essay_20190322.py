#try2_make soft essary_20190322
def deal_file(txt):
    for chr in '！。，”“':
        txt = txt.replace(chr, " ")
    new_words = txt.split(" ")
    return new_words
def print_file(txt):
    lst_file = deal_file(txt)
    linewidth = 30
    for line in lst_file:
        print(line.center(linewidth, chr(12288)))
def main():
    f = open("一醉枫林（三）.txt", "r")
    txt = f.read()
    deal_file(txt)
    print_file(txt)
main()
    

    
