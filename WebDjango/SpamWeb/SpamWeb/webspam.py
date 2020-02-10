# -*- coding: UTF-8 -*-
from django.shortcuts import render
# from webspam_app.models import WebSpamModel
# import requests
from .UrlRead import Urlread
import os
import csv
import io

def webspam_main(request):
    result_dict = {'url_list': [], 'host_list': [],'flag':0}
    if request.POST:
        if 'result_show' in request.POST.keys():
            os.system("/usr/bin/python ../WebspamDetect/DataPreprocessAndJudge/NewHtmlJudgeAndLearning.py")

            result_file = io.open("../WebspamDetect/Result/spams.csv","r",encoding='utf-8')
            result_rows = csv.reader(result_file)
            result_dict['flag']=1
            #results=WebSpamModel.objects
            # print(result)
            for result_row in result_rows:
                if result_row!=[]:
                    result_dict['url_list'].append(result_row[1])
                    result_dict['host_list'].append(result_row[0])
            return render(request, 'webspam.html', result_dict)
        if 'crawl_start' in request.POST.keys():
            urlread = Urlread()
            crawl_num = urlread.queryTable()
            os.system("cd ../scrapytest&&python debug.py")
            return render(request, 'webspam.html',{'crawl_num':crawl_num,'flag':0,'crawl_status':'条爬取成功'})
    return render(request,'webspam.html',result_dict)

if __name__=='__main__':
    '''
    url = 'http://localhost:6800/schedule.json'
    data = {'project': 'scrapytest', 'spider': 'spamtest0','url_dict':"{'http://www.baidu.com':'baidu.com'}"}
    requests.post(url=url,data=data)
    
    requrl = "http://localhost:6800/listjobs.json?project=scrapytest"
    print(str(requests.get(requrl)))
    '''
    result_dict={}
    result_file = io.open("../WebspamDetect/Result/spams.csv", "r", encoding='utf-8')
    result_rows = csv.reader(result_file)
    result_dict['flag'] = 1
    # results=WebSpamModel.objects
    # print(result)
    for result_row in result_rows:
        if result_row!=[]:
            print(result_row)