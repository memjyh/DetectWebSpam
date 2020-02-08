# -*- coding: UTF-8 -*-

def Generate(url):
    url=str(url)
    url = url.replace('?',"#1")
    url = url.replace('/',"#2")
    url = url.replace('\\',"#3")
    url = url.replace('*',"#4")
    url = url.replace('|',"#5")
    url = url.replace('<',"#6")
    url = url.replace('\"',"#7")
    url = url.replace('>',"#8")
    url = url.replace(':',"#9")
    return url

def DeGenerate(url):
    url=str(url)
    url = url.replace('#1',"?")
    url = url.replace('#2',"/")
    url = url.replace('#3',"\\")
    url = url.replace('#4',"*")
    url = url.replace('#5',"|")
    url = url.replace('#6',"<")
    url = url.replace('#7',"\"")
    url = url.replace('#8',">")
    url = url.replace('#9',":")
    return url