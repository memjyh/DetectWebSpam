# -*- coding: UTF-8 -*-

import os,sys
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr  
reload(sys)  
sys.setdefaultencoding( "utf-8" ) 
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir)
sys.path.insert(0,parentdir+"/Common")

from bs4 import BeautifulSoup
import re


def SeparateWithHtml(html):
        tagList = []
        elemList = []
        attrList = []
        soup = BeautifulSoup(html,"html5lib")
        txt = re.compile("[^-~]")
        for elem in soup.body(text = txt):
            dname=""
            for parent in elem.parents:
                dname = dname + "-" + str(parent.name)
            if elem !=u'\n' and str(elem.parent.name) != "script":
                #print "dname:",dname
                #print "elem:",elem
                #print elem.parent.attrs
                tagList.append(dname)
                elemList.append(elem)
                attrList.append(elem.parent.attrs)
        for elem in soup.body(text =""):
            dname=elem.name
            for parent in elem.parents:
                dname = dname + "-" + str(parent.name)
            if str(elem.parent.name) != "script" and str(elem.name) != "script":
                #print "dname:",dname
                #print "elem:",""
                #print elem.attrs
                tagList.append(dname)
                elemList.append("")
                attrList.append(elem.attrs)
        return tagList,elemList,attrList
