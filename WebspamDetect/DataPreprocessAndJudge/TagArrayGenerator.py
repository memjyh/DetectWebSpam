# -*- coding: UTF-8 -*-

import os,sys
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr  
reload(sys)  
sys.setdefaultencoding( "utf-8" ) 
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir)
sys.path.insert(0,parentdir+"/Common")

def Generate(tagtree):
    TagEnumFilePath = "../WebspamDetect/DetectModel/Tag.txt"
    TagList = []
    fo = open(TagEnumFilePath, "r")
    while 1:
        line  = fo.readline()
        if not line:
            break        
        TagList.append(line.split("\n")[0].strip())
    fo.close()
    TagList.remove("")
    TagList.remove("")
    # TagList.remove("\r")
    # TagList.remove("\r")
    for t in TagList:
        #print t
        t=t[:-1]
        #print t
    #print TagList

    TagNumber = len(TagList)
    # print TagNumber
    TagArray = [0 for n in range(TagNumber)]
    tags = tagtree.split("-")
    if "" in tags:
        tags.remove("")
    #print tags
    for tag in tags:
        if tag not in TagList:
            continue
        TagArray[TagList.index(tag)]=1
    #print len(TagArray)
    return TagArray

if __name__ == '__main__':
    print len(Generate('a-article-b'))
