# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import csv
from scrapytest.filenamegenerator import Generate
import os

class MysqlPipeline():
    # def __init__(self):
    #     self.conn = pymysql.connect(host='localhost', user='root', password='123456', db='test', port=3306)
    #     self.cursor = self.conn.cursor()
    #     self.file = open("content.csv", "w", newline="", encoding="utf-8")
    #     self.write = csv.writer(self.file)
    #     self.filename = "haha.txt"

    def process_item(self, item, spider):
        current_path = os.path.abspath('...')
        if not os.path.isdir(current_path+"/data/" +item['host']):
            os.mkdir(current_path+"/data/" +item['host'])
        if len(Generate(item['urlname'])) > 200:
            filename = current_path+"/data/"+ item['host']+"/"+ Generate(item['urlname'])[0:200]
        else:
            filename = current_path+"/data/"+ item['host']+"/"+ Generate(item['urlname'])
        str = item['urlname'] + "\r\n" + item['html_content']
        urlcode = item['urlcode']
        with open(filename, "w", encoding=urlcode) as f:
            f.write(str)

        return item

