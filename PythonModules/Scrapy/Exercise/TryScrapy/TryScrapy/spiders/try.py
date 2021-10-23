import scrapy
from TryScrapy.items import TryscrapyItem
from scrapy import Request
from scrapy.spiders import Spider
from TryScrapy.items import ScrapydoubanItem

class DoubanMovieTop250Spider(scrapy.Spider):
    name = 'douban_movie_top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = ScrapydoubanItem()
        movies = response.xpath('/html/head/title/text()')
        print('movie:\n', movies)

        yield item

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["movie.douban.com"]
    start_urls = (
        'https://movie.douban.com/top250',
    )

    def parse(self, response):
        # 获取网站标题
        context = response.xpath('/html/head/title/text()')   
       
        # 提取网站标题
        title = context.extract_first()  
        print(title) 
        items = []

        for each in response.xpath("/html/body/div[2]/div[3]/div[1]/div[2]/div[1]/ul[1]/li"):
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = TryscrapyItem()
            #extract()方法返回的都是unicode字符串
            name = each.xpath("./a/text()").extract()
            print('name:', name)
            #xpath返回的是包含一个元素的列表
            item['name'] = name[0]

            items.append(item)

        # 直接返回最后数据
        return items