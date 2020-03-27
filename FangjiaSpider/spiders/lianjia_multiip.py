import math
import random

import scrapy
from logbook import log
from scrapy.http import Request

from FangjiaSpider import settings
from FangjiaSpider.data.FangjiaItem import FangjiaItem


class liangjiaMultiSpider(scrapy.Spider):
    name="lianjia_multi"
    start_urls=['https://cs.fang.lianjia.com/loupan/pg']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url,self.parse)

    def parse(self,response):
        url = response.url
        if url in self.start_urls:
            totalCount=response.css(".page-box")
            totalCount=response.xpath("//div[@class='page-box']/@data-total-count").get()
            totalPage=math.ceil(float(totalCount)/10)
            for i in range(1,totalPage):
                url1 = self.start_urls + list(str(i))
                url2=''
                for j in url1:
                    url2 +=j+''
                yield Request(url2, callback=self.parse)
        else:
            ul=response.css(".resblock-list-wrapper li")
            ul=response.xpath("//ul[@class='resblock-list-wrapper']/li")
            for info in ul:
                onSale=info.css(".sale-status::text").extract_first()
                name=info.css(".resblock-name a::text").extract_first()
                location=info.css(".resblock-location span::text").extract_first()
                address=info.css(".resblock-location a::text").extract_first()
                price =info.css(".main-price .number::text").extract_first()
                if price=='价格待定':
                    price='0'
                resBlockType=info.css(".resblock-name .resblock-type::text").extract_first()
                #以下方式不知道为什么会把所有li下面的数据都查询出来
                #info.xpath("//span[@class='resblock-type']/text()").get()
                remarks=info.css(".resblock-tag span::text")
                area=info.css(".resblock-area span::text").get()
                rooms=info.css(".resblock-room span::text")
                rooms_str=""
                for i in rooms:
                    room=i.extract()
                    rooms_str+=room+" "
                remarks_str=""
                for r in remarks:
                    remark=r.extract()
                    remarks_str+=remark+" "
                item=FangjiaItem()
                item['onSale']=onSale
                item['name']=name
                item['location']=location
                item['address']=address
                item['price']=price
                item['remarks']=remarks_str
                item['resBlockType']=resBlockType
                item['rooms']=rooms_str
                item['area']=area
                item['url']=url
                yield item
