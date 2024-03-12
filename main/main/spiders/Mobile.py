import scrapy
from time import sleep


class MobileSpider(scrapy.Spider):
    name = "Mobile"
    allowed_domains = ["www.flipkart.com"]
    #start_urls = ["https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io"]
    #ru = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&param=1112&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlJlYWxtZSBzbWFydHBob25lcyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&wid=17.productCard.PMU_V2_15&page=2"
    
    def start_requests(self):
        yield scrapy.Request(url="https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io",callback=self.parse,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})

    def parse(self, response):
        for urls in response.xpath("//a[@class='_1fQZEK']"):
            links=urls.xpath("@href").get()
            ab_url = response.urljoin(links)
            yield response.follow(url=ab_url,callback=self.page_parser)
        
        for page in range(2,50):
            ur = response.xpath("(//a[@class='_1LKTO3']/@href)[2]").get()
            #ur='https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&param=1112&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlJlYWxtZSBzbWFydHBob25lcyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&wid=18.productCard.PMU_V2_14&page='+str(page)
            yield response.follow(url=ur,callback=self.parse)
           
    def page_parser(self,response):
        image=response.xpath("//img[@class='_396cs4 _2amPTt _3qGmMb']/@src").get()
        product=response.xpath("(//span[@class='B_NuCI']/text())[1]").get()
        selling=response.xpath("//div[@class='_30jeq3 _16Jk6d']/text()").get()
        mrp=response.xpath("(//div[@class='_3I9_wc _2p6lqe']/text())[2]").get()
    
    

        yield{
            'Images':image,
            'Product Name':product,
            'Selling Price':selling,
            'MRP':mrp
        }
        
