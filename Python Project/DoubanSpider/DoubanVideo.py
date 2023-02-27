# -*- coding = utf-8 -*-

# 解析网页
from bs4 import BeautifulSoup as bf
# 正则表达式
import re
# Excel表格操作
import xlwt
# 获取URL得到html文件
import urllib.request as req

# 设置单独全局变量，如需更加规范，也可以将电影信息封装成一个class类 比如 class Movie: ...
# 电影名称
find_name = re.compile(r'<span class="title">(.*?)</span>')
# 电影播放地址链接
find_link = re.compile(r'<a href="(.*?)">')
# 电影封面的地址链接，re.S让换行符包含在字符中
find_imgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
# 电影评分
find_score = re.compile(r'<span class="rating_num".*>(.*?)</span>')
# 评分人数
find_num = re.compile(r'<span>(\d*人)评价</span>')
# 名句
find_inq = re.compile(r'<span class="inq">(.*?)</span>')


# 有些电影没有某些项，所以查找长度为0的时候，设置该项为空
def set_film(file, content):
    # 检查查找内容的长度，如果不为0，说明查找到内容，则将内容转换成字符串类型
    if len(re.findall(file, content)) != 0:
        film = str(re.findall(file, content)[0])
    else:
        film = ""

    return film


# 保存获取的html，避免出现ip异常的情况
def write_html(path, html):
    file = open(path, 'w', encoding='utf-8')
    file.write(str(html))
    file.close()


# 循环获取所有的html页面并提取所需信息保存到 data_list 列表
def get_data():
    # 获得多有页面有价值的信息，然后集中存放与data_list列表中
    data_list = []
    # 循环遍历，修改?start=起始排行序号，获取不同分页的豆瓣top信息，url分页格式去豆瓣换页内容试试
    # 例如第一页第 top 0-24，第二页是top 25-49条 ?start=25 这个参数，会让服务器响应第二页的25条信息
    for i in range(0, 250, 25):

        # 使用二进制读取，这点很重要，报错无数次
        html = open('Data/html/html' + str(i//25) + '.html', 'rb')

        # 接下来是逐一解析数据
        bs = bf(html, 'html.parser')

        # 使用标签 + 属性组合查找，查找<div class="item"></div>的标签块
        # 注意：class是关键字，所以这里需要使用 class_ 代替
        f_list = bs.find_all('div', class_="item")

        # 使用re.findall(x, s) 或者 x.findall(s)效果一样
        for f in f_list:
            data = []
            # 将正则表达式提取的内容赋值给自定义变量
            file_name = set_film(find_name, str(f))
            file_num = set_film(find_num, str(f))
            file_link = set_film(find_link, str(f))
            file_img_src = set_film(find_imgSrc, str(f))
            file_score = set_film(find_score, str(f))
            file_inq = set_film(find_inq, str(f))

            # 将所有需要的数据保存到data列表
            data.append(file_name)
            data.append(file_score)
            data.append(file_num)
            data.append(file_link)
            data.append(file_img_src)
            data.append(file_inq)

            # 写入data（单条电影信息）列表，到总的 data_list（所有电影信息）列表
            data_list.append(data)

        html.close()

    return data_list


# 保存豆瓣的各页html文件
def save_douban_html(base_url):
    for i in range(0, 250, 25):
        # 使用基础地址 'https://movie.douban.com/top250?start='  +  偏移地址如 '25'
        url = base_url + str(i)

        # 获取html保存在本地，方便之后爬虫操作，因为频繁爬取可能被豆瓣发现异常
        html = ask_url(url)

        # 将文件批量保存在 Data/html/ 目录下 i//25 是整除，命名格式如   html0.html  html1.html ...
        write_html('Data/html/html' + str(i//25) + '.html', html)


# 获取html信息，并返回html信息
def ask_url(url):
    # 设置传给服务器的header头部信息，伪装自己是正规浏览器访问
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0"
    }

    # 用于保存获取的html文件
    html = ""
    # 最好用 try-except 捕捉异常
    try:
        # 封装一个Request对象，将自定义的头部信息加入进去
        res = req.Request(url, headers=headers)
        # 向指定的url获取响应信息，设置超时，防止长时间耗在一个页面
        response = req.urlopen(res, timeout=10)
        # 读取html信息，使用decode('utf-8')解码
        html = response.read().decode('utf-8')
    # 如果出错，就捕捉报错信息并打印出，这里使用Exception 泛泛的意思一下
    except Exception as error:
        # 出现异常时候，打印报错信息
        print("Ask_url is Error : " + error)

    # 将获得的html页面信息返回
    return html


# 以下split、main两个函数和 if __name__ 程序主入口是我个人编程习惯，与上述内容无本质关联
# 定义分隔线长度，并返回分割线字符串
def split(num):
    str1 = ""
    for i in range(1, num):
        # print("------------", end='')
        str1 += "------------"

    return str1


# 读取文件文本
def read_file(file_name):
    # 打开文本选择读模式
    file = open(file_name, 'r', encoding='utf-8')
    print(file.read())
    file.close()


# 保存数据到txt文本中
def save_data_txt(datas, save_file):
    # 打开文本选择写模式，并指定编码格式
    file = open(save_file, 'w', encoding='utf-8')
    # 不能直接写入list，所以通过遍历一条条写入
    for data in datas:
        for dat in data:
            file.write(dat + '\n')
        file.write(split(10) + '\n')
    file.close()


# 设置excel的单元格字体样式
def set_font(bold, size, horz):
    # 创建xlwt格式对象
    style_font = xlwt.XFStyle()
    # 设置字体是否为粗体
    style_font.font.bold = bold
    # 设置字体尺寸大小
    style_font.font.height = size
    # 字体是否居中
    if horz:
        # 设置字体水平居中
        style_font.alignment.horz = 0x02
        # 设置字体垂直居中
        style_font.alignment.vert = 0x01
    # 设置单元格自动换行
    style_font.alignment.wrap = False

    # 返回设置的字体样式
    return style_font


# 保存数据到excel文件中
def save_data_excel(datas, save_path):
    # 创建一个xlwt对象，使用utf-8编码格式
    excel = xlwt.Workbook(encoding='utf-8')
    # 创建一个工作表，命名为top250
    sheet = excel.add_sheet('top250')

    # 设置前六列的列宽
    width_c = [256*20, 256*6, 256*12, 256*42, 256*72, 256*68]
    for i in range(0, 6):
        sheet.col(i).width = width_c[i]

    # 设置三种单元格样式 set_font(粗体，尺寸，居中)
    style_font_title = set_font(True, 240, True)
    style_font_content = set_font(False, 220, True)
    style_font_content1 = set_font(False, 220, False)

    # 表格各列的列名
    titles = ['电影名称', '评分', '评论数', '电影链接', '图片链接', '电影名言']
    index = 0
    # 将标题写入excel
    for title in titles:
        # (单元格行序号，单元格列序号，单元格的内容，单元格样式)
        sheet.write(0, index, title, style_font_title)
        index += 1

    # 将数据写入excel
    index_r = 1
    # 从多条电影中每次取出一条
    for data in datas:
        index_c = 0
        # 从一条电影中每次取出一个属性
        for item in data:
            # 前三列设置居中对齐
            if index_c <= 2:
                sheet.write(index_r, index_c, item, style_font_content)
            # 后三列设置默认对齐，即左对齐
            else:
                sheet.write(index_r, index_c, item, style_font_content1)
            index_c += 1
        index_r += 1

    # 保存excel文件到指定路径
    excel.save(save_path)


# 主程序
def main():
    base_url = "https://movie.douban.com/top250?start="

    # 1.爬取网页
    # 从豆瓣上获取html文件并保存到本地目录下，该方法成功执行一次即可，保存html，接下来本地操作
    # save_douban_html(base_url)

    # 2.解析数据
    # 逐个解析保存在本地的html文件
    datas = get_data()

    # 3.保存数据
    # 保存爬取数据到本地txt文件
    # save_txt_path = 'Data/Text/top250.txt'
    # save_data_txt(datas, save_txt_path)
    # 将读取的txt文本打印到控制台
    # read_file('Data/Text/top250.txt')

    # 保存爬取数据到本地excel文件
    save_excel_path = 'Data/excel/top250.xls'
    save_data_excel(datas, save_excel_path)

    # 打印自定义分界线
    print(split(10))


# 主程序入口
if __name__ == '__main__':
    main()