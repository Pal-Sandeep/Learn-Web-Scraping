import scrapy

class ScrapUrls(scrapy.Spider):
    name = "scrap"    # name must be unique 


    def start_requests(self):

        urls = ['https://your.url.com/']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

        # return super().start_requests()
    
    def parse(self,response):
        title = response.css('title::text').extract_first()

        links = response.css('a::attr(href)').extract()

        for link in links:
            yield{
                'title':title,
                'links':link
                }
            
            if 'github' in link:
                yield scrapy.Request(url=link,callback=self.parse)