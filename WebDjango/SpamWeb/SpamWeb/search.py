
# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response,render
from django.http import HttpResponse

def search_form(request):
    context = {}
    request.encoding = 'utf-8'
    if request.POST:
        context['crl'] = request.POST['q']

    #return render_to_response('search_form.html')
    return render(request,'search_form.html',context)

def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = "你搜索的内容为："+request.GET['q']
    else:
        message = "你提交了空表单"
    return HttpResponse(message)