# encoding='utf-8'
import pandas as pd

def main():
    with open("zichan.html", "r") as f:    ###读入文件
        htmll = f.read()
    html_data = pd.read_html(htmll)
    for i in html_data:
        table_date = pd.DataFrame(i)
        table_date.to_csv('table.csv',encoding='utf-8-sig')
        #print table_date

if __name__ == '__main__':
    main()

