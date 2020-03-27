import scrapy

class FangjiaItem(scrapy.Item):
    onSale=scrapy.Field()
    name=scrapy.Field()
    location=scrapy.Field()
    address=scrapy.Field()
    price=scrapy.Field()
    resBlockType=scrapy.Field()
    remarks=scrapy.Field()
    rooms=scrapy.Field()
    area=scrapy.Field()
    url=scrapy.Field()
    pass

