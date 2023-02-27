import requests
import re
import xlwt
from lxml import etree

outputPath = '/Users/kevin/Desktop/program files/python/Python Project/DoubanSpider/'

def get_html(url):
    url = 'https://www.baidu.com'
    r = requests.get(url)
    
    r.encoding = r.apparent_encoding
    print(r.text[-200:])
    #html=requests.get(url)
    #return html

#数据解析
def parse_html(html):
    parse=etree.HTMLParser
    tree=etree.HTML(html)
    all_books=[]
    # count=0
    tables_list=tree.xpath('// *[ @ id = "content"] / div / div[1] / div/ table')
    for table in tables_list:

        book_info = {}
        url=table.xpath('.//td[@valign="top"]/div[1]/a/@href')[0]
        # print(url)
        name=table.xpath('.//td[@valign="top"]/div[1]/a/@title')[0]
        # print(table.xpath('./td[2]/p[1]/text()')[0])
        author=table.xpath('.//td[@valign="top"]/p[1]/text()')[0].split('/')[0]
        price=re.search(r'\d+\.\d+',table.xpath('.//td[@valign="top"]/p[@class="pl"]')[0].text,re.S)
        if price:
            # count+=1
            book_info['book_price'] = price.group()
        else:
            # count+=1
            if re.search(r'\d+元',table.xpath('.//td[@valign="top"]/p[@class="pl"]')[0].text,re.S):
                book_info['book_price'] = re.search(r'\d+元',table.xpath('.//td[@valign="top"]/p[@class="pl"]')[0].text,re.S).group()
            else:
                book_info['book_price'] = '未标价'
        score=table.xpath('.//span[@class="rating_nums"]/text()')[0]
        # print(table.xpath('.//span[@class="pl"]')[0].text)
        people_nums=re.search(r'\d+',table.xpath('.//span[@class="pl"]')[0].text,re.S).group()
        # print(people_nums)
        book_info['book_name']=name
        book_info['book_url'] = url
        book_info['book_author'] = author
        book_info['book_score'] = score
        book_info['people_nums'] = people_nums
        all_books.append(book_info)
    # print(count)
    return all_books

#数据持久化存储,可以存储到excle中
def save_data(all_books, outputPath):
    #创建workbook对象
    workbook=xlwt.Workbook(encoding='utf-8')
    sheet1=workbook.add_sheet('豆瓣top250图书')
    mulv=['书名','链接','作者','价格','评分','评分人数']
    en_mulv=['book_name','book_url','book_author','book_price','book_score','people_nums']
    for j in range(len(all_books[0])):
        sheet1.write(0,j,mulv[j])
    for i in range(1,len(all_books)+1):
        for j in range(len(all_books[0])):
            sheet1.write(i,j,all_books[i-1][en_mulv[j]])

    workbook.save(outputPath+'豆瓣top250图书.xlsx')

if __name__=='__main__':
    start_url='https://book.douban.com/top250?start='#起始的url
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    headers=headers
    all_books=[]
    
    for i in range(10):#爬取十页数据,也就是top250的榜单
        url=start_url+str(i*25)
        html=get_html(url)
        onepage_all_books=parse_html(html)
        # print(all_books)
        all_books+=onepage_all_books

    save_data(all_books)