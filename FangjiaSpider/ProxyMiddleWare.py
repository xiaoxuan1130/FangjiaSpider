import random

from FangjiaSpider import settings


class ProxyMiddleWare(object):

    def process_request(self,request,spider):
        proxy=self.get_random_proxy()
        request.meta['proxy']=proxy

    def process_response(self,request,response,spider):
        if response.status!=200:
            proxy=self.get_random_proxy()
            request.meta['proxy']=proxy
            return request
        return response

    def get_random_proxy(self):
        proxies=settings.OPPOOL
        proxy=random.choice(proxies).strip()
        return proxy