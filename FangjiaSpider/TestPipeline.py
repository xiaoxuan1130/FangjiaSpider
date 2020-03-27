# -*- coding: utf-8 -*-
import datetime
import uuid

import pymysql

from FangjiaSpider import settings


class TestPipeline(object):

    def __init__(self):
        dbargs = dict(
            host=settings.MYSQL_HOST,
            port=settings.MYSQL_PORT,
            db=settings.MYSQL_DB,
            user=settings.MYSQL_USER,
            password=settings.MYSQL_PASS,
            charset='utf8',
            use_unicode=True,
        )
        self.conn= pymysql.connect(**dbargs)
        self.cursor=self.conn.cursor()
        self._sql=None

    def process_item(self, item, spider):
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        id=uuid.uuid1()
        self.cursor.execute(self.sql,(str(id),item['name'], item['address'], item['onSale'], item['price'], item['location'], item['remarks'],
                     item['resBlockType'],item['area'],item['rooms'],dt,item['url']))
        self.conn.commit()

    @property
    def sql(self):
        self._sql="insert into fangjia (id,name,address,on_sale,price,location,remarks,type,area,rooms,create_date,url) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        return self._sql


