import scrapy
from ..items import NewsExtractItem

class NewsSpider(scrapy.Spider):
    name = 'news'
    page_number = 1
    start_urls=['https://www.indiatoday.in/top-stories']

    def parse(self, response):

        items = NewsExtractItem()
        all_responses= response.css('.catagory-listing')

        for text in all_responses:
            title = text.css("h2::attr(title)").extract_first()
            temp_content = text.css("p::text").extract_first()
            content = ' '.join(temp_content.split())
            url = "https://www.indiatoday.in"+text.css("h2 a::attr(href)").extract_first()

            #Item assign
            items['title']= title
            items['content'] = content
            items['url'] = url

            #Output per textec
            yield items

        #Increment and go to next page
        next_page = 'https://www.indiatoday.in/top-stories?page='+str(NewsSpider.page_number)
        if NewsSpider.page_number <=11:
            NewsSpider.page_number +=1
            yield response.follow(next_page, callback=self.parse)
