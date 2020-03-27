# -*- coding: utf-8 -*-
import datetime

import pymysql


class SqlPipeline(object):

    def process_item(self, item, spider):
        self.query = "insert IGNORE into `fangjia` (name,address,on_sale,price,location,remarks,type) values(%s,%s,%s,%s,%s,%s,%s) "
        self.data = (item['name'], item['address'], item['onSale'], item['price'], item['location'], item['remarks'],
                     item['resBlockType'])
        d = self.dbpool.runInteraction(self._do_upsert, item, spider)
        d.addBoth(lambda _: item)
        return d

    def __init__(self,dbpool):
        self.dbpool=dbpool

    @classmethod
    def from_settings(cls,settings):
        dbargs=dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DB'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASS'],
            charset='utf8',
            use_unicode=True,
        )
        dbpool=pymysql.connect(**dbargs)
        return dbpool

