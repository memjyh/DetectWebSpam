# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapytest.UrlRead import Urlread
from scrapytest.items import ScrapytestItem
from scrapy.spidermiddlewares import httperror
import csv
import chardet
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.downloadermiddlewares.redirect import RedirectMiddleware
import scrapy.downloadermiddlewares

#url_ex = open("url_exception.csv", "w", newline='', encoding='utf-8')
#url_exception = csv.writer(url_ex)

#global i
#i = 0
class SpamtestSpider(scrapy.Spider):
    name = 'spamtest1'
    #allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']
    #302:请求的资源现在临时从不同的 URI 响应请求
    handle_httpstatus_list = [ 404, 403, 401, 405, 400, 500, 503]

    def __init__(self):
        self.urlread = Urlread()
        self.url_dict = self.urlread.queryTable()#urllist
        self.url_list = list(self.url_dict.keys())
        self.urlnames={}
        for i in range(0,int(len(self.url_list)/3)):
            self.urlnames[self.url_list[i]]=self.url_dict[self.url_list[i]]

    def start_requests(self):
        for key in self.urlnames.keys():
            yield scrapy.Request(url=key,callback=self.parse)


    def parse(self, response):
        #try:
        if response.url=='':
            del response
        elif response.url=='exception':
            del response
        else:
            #global i
            try:
                #获取网页代码
                url = response.url
                body = response.body
                code_list = chardet.detect(body)
                sel = Selector(response)

                content_list = sel.xpath('/html').extract()
                content = content_list[0]

                #print("="*20+code_list['encoding']+"="*20)
                if code_list['encoding'] is not None:
                    #urlname = self.urlnames[i-1]
                    item = ScrapytestItem()
                    item['urlcode'] = code_list['encoding']
                    item['urlname'] = url
                    item['html_content'] = content
                    item['host'] = self.urlnames[url]

                    yield item
            except Exception as e:
                pass







