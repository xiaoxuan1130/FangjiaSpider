import os
print(os.getcwd())

class CsvPipeline(object):
    def process_item(self,item,spider):
        with open('E:\python-workspace\csv\house.txt','a+',encoding='utf-8') as fp:
            name=str(item['name'])
            onSale=str(item['onSale'])
            location=str(item['location'])
            address=str(item['address'])
            price=str(item['price'])
            remarks=str(item['remarks'])
            resBlockType=str(item['resBlockType'])
            fp.write(name+" "+onSale+" "+address+" "+price+" "+remarks+" "+resBlockType+'\n')
            fp.flush()
            fp.close()
        return item
    print("写入文件成功")