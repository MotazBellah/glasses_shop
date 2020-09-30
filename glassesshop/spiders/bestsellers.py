import scrapy


class BestsellersSpider(scrapy.Spider):
    name = 'bestsellers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        products_list = response.xpath("//div[@id='product-lists']/div")

        for i in products_list:
            link = i.xpath(".//div[2]/a/@href").get()
            glass_image = i.xpath(".//div[2]/a/img[1]/@src").get()
            tryon_image = i.xpath(".//div[2]/a/img[2]/@src").get()
            name = i.xpath(".//div[3]/div[2]/div[1]/div[1]/div[1]/a/@title").get()
            price = i.xpath(".//div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/span/text()").get()

            yield {
                'name': name,
                'price': price,
                'link': link,
                'glass_image': glass_image,
                'try_on_image': tryon_image,
            }
