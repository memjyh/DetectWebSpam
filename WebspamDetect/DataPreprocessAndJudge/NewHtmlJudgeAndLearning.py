# -*- coding: UTF-8 -*-

import os,sys,shutil
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr  
reload(sys)  
sys.setdefaultencoding( "utf-8" ) 
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir)
sys.path.insert(0,parentdir+"/Common")

import HtmlBlockSeparator as HBS
import HeadArrayGenerator as HAG
import AttributeArrayGenerator as AAG
import TagArrayGenerator as TAG
import TextArrayGenerator as TAG1
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
import numpy as np

from bs4 import BeautifulSoup
import re

import csv

import DataAcquire.FileNameGenerator as fng

def Judge(addr,worddict,html,ORValueFilePath,nb_clf,KeyList,AllkeyValueDict):
    # definitethreshold = float(40)
    # possiblethreshold = float(36)
    definitethreshold = float(60)
    possiblethreshold = float(16)
    soup = BeautifulSoup(html,"html5lib")
    headtext = HAG.GenerateHeadText(html)
    headorvalue = float(0)
    flag =0
    # print headtext
    if headtext!="" and re.match("[^\s]",headtext,re.I):
        # print 'headtext:',headtext
        headorvalue,unexist,exist = TAG1.ComputeORValue(worddict,headtext)

        # print 'headorvalue:',headorvalue
    if headorvalue > possiblethreshold:
        print addr," head is spam"
        # unexistorvalue = float(36.8848708487)
        unexistorvalue = float(60.9042806566)

        for word in unexist:
            worddict[word.decode("utf8")] = (1,0,unexistorvalue)
        for word in exist:
            #print word
            A = float(worddict[word.decode("utf8")][0])+1
            ORValue = (float(1)+float(1)/float(A))*float(worddict[word.decode("utf8")][2])
            newA= A+1
            worddict[word.decode("utf8")] = (newA,worddict[word.decode("utf8")][1],ORValue)
        flag = 1
    elif headorvalue>float(0) and headorvalue <=possiblethreshold:
        print addr," head is not spam"
        # unexistorvalue = float(9.21942446043)
        unexistorvalue = float(15.22505793)
        for word in unexist:
            #print word
            worddict[word.decode("utf8")] = (0,1,unexistorvalue)
        for word in exist:
            #print word
            B = float(worddict[word.decode("utf8")][1])+1
            ORValue = (1/(float(1)+float(1)/float(B)))*float(worddict[word.decode("utf8")][2])
            newB= B+1
            worddict[word.decode("utf8")] = (worddict[word.decode("utf8")][0],newB,ORValue)
    else:
        pass
    tagList,elemList,attrList = HBS.SeparateWithHtml(html);
    # print tagList
    # print elemList
    # print attrList
    i=0
    for tag in tagList:
        blockarray =[]
        tagarray = TAG.Generate(tag)
        text = elemList[i]
        attrsarray,text = AAG.Generate(str(attrList[i]),text,worddict,KeyList,AllkeyValueDict)
        i=i+1
        if text!="":
            #print text
            # print len(tagarray)
            # print len(attrsarray)
            blockarray.extend(tagarray)
            blockarray.extend(attrsarray)
        else:
            continue


        if len(blockarray) != 4071:
        # if len(blockarray) != 217:
            print "the lenth of the array is not correct:",addr
            print "len:",len(blockarray)

        #print 'text:',text
        orvalue,unexist,exist = TAG1.ComputeORValue(worddict,text)
        #print orvalue
        #blockarray.reshape(1, -1)
        blockarray1=np.array(blockarray)
        blockarray2=blockarray1.reshape(1,-1)
        possibility = nb_clf.predict(blockarray2)
        #possibility = nb_clf.predict(blockarray)
        #print orvalue
        if orvalue>=definitethreshold:           
            flag = flag + 1
            # print 'text:'+text
            # print 'orvalue>=definitethreshold: orvalue:'+str(orvalue)
            print addr," block is spam"
            # unexistorvalue = float(36.8848708487)
            unexistorvalue = float(60.9042806566)
            for word in unexist:
                #print word
                worddict[word.decode("utf8")] = (1,0,unexistorvalue)
            for word in exist:
                #print word
                A = float(worddict[word.decode("utf8")][0])+1
                ORValue = (float(1)+float(1)/float(A))*float(worddict[word.decode("utf8")][2])
                newA= A+1
                worddict[word.decode("utf8")] = (newA,worddict[word.decode("utf8")][1],ORValue)
            if possibility!=[1]:
                blockarray1 = np.array(blockarray)
                blockarray2 = blockarray1.reshape(1, -1)
                nb_clf.partial_fit(blockarray2, [1], classes=np.array([0, 1]))
        elif orvalue<definitethreshold and orvalue>possiblethreshold and possibility==[1]:
            flag = flag + 1
            # print "possiblility:",possibility
            # print 'text:' + text
            # print 'orvalue:' + str(orvalue)
            print addr," block is spam"
            # unexistorvalue = float(36.8848708487)
            unexistorvalue = float(60.9042806566)
            for word in unexist:
                #print word
                worddict[word.decode("utf8")] = (0,1,unexistorvalue)
            for word in exist:
                #print word
                A = float(worddict[word.decode("utf8")][0])+1
                ORValue = (float(1)+float(1)/float(A))*float(worddict[word.decode("utf8")][2])
                newA= A+1
                worddict[word.decode("utf8")] = (newA,worddict[word.decode("utf8")][1],ORValue)
            #nb_clf.partial_fit(blockarray, [0], classes=np.array([0, 1]))
        elif orvalue<definitethreshold and orvalue>possiblethreshold and possibility==[0]:
            #print "possiblility:",possibility
            #print addr," block is not spam"
            # unexistorvalue = float(36.8848708487)
            unexistorvalue = float(60.9042806566)
            for word in unexist:
                #print word
                worddict[word.decode("utf8")] = (1,0,unexistorvalue)
            for word in exist:
                #print word
                B = float(worddict[word.decode("utf8")][1])+1
                ORValue = (1/(float(1)+float(1)/float(B)))*float(worddict[word.decode("utf8")][2])
                newB= B+1
                worddict[word.decode("utf8")] = (worddict[word.decode("utf8")][0],newB,ORValue)
            #nb_clf.partial_fit(blockarray, [0], classes=np.array([0, 1]))
        elif orvalue<=possiblethreshold:
            #print "possiblility:",possibility
            #print addr," block is not spam"
            # unexistorvalue = float(9.21942446043)
            unexistorvalue=float(15.22505793)
            for word in unexist:
                #print word
                worddict[word.decode("utf8")] = (0,1,unexistorvalue)
            for word in exist:
                #print word
                B = float(worddict[word.decode("utf8")][1])+1
                ORValue = (1/(float(1)+float(1)/float(B)))*float(worddict[word.decode("utf8")][2])
                newB= B+1
                worddict[word.decode("utf8")] = (worddict[word.decode("utf8")][0],newB,ORValue)
            if possibility!=[0]:
                blockarray1 = np.array(blockarray)
                blockarray2 = blockarray1.reshape(1,-1)
                nb_clf.partial_fit(blockarray2, [0], classes=np.array([0, 1]))
    if flag>0:
        return True,nb_clf,worddict
    else:
        return False,nb_clf,worddict

if __name__ == '__main__':

    HtmlDataPath ="../WebspamDetect/Result/data"  #检测的网页在的路径
    SpamPath = "../WebspamDetect/Result/spam"  #spam被分到的路径
    NonSpamPath ="../WebspamDetect/Result/nonspam"  #nonspam被分到的路径
    HtmlFiles = os.listdir(HtmlDataPath)
    KeyEnumFilePath = "../WebspamDetect/DetectModel/Key.txt"  # html标签文件
    ORValueFilePath = "../WebspamDetect/DetectModel/AssetValuemy/TextAB+1ORValueWithoutLog.txt"  # 优势模型
    NewORValueFilePath = "../WebspamDetect/DetectModel/AssetValuemy/TextAB+1ORValueWithoutLogV10.txt"  # 新优势模型
    ModelFilePath = "../WebspamDetect/DetectModel/modelmy/nb_train_model_without_text_with_text.m"  # nb模型
    NewModelFilePath = "../WebspamDetect/DetectModel/modelmy/nb_train_model_without_text_with_text_v10.m"  # 新nb模型
    AttributesDirectoryPath = "../WebspamDetect/DetectModel/Attributes"  # 属性文件
    #errordatapath = "/Volumes/E/ExperimentSample/errordata" #错误文件
    KeyList, AllkeyValueDict = AAG.init(KeyEnumFilePath, AttributesDirectoryPath)
    worddict = {}
    fo = open(ORValueFilePath, "r")
    while 1:
        line = fo.readline()
        if not line:
            break

        word = line.split(" ")[0]
        # print word
        A = float(line.split(" ")[1])
        B = float(line.split(" ")[2])
        C = float(line.split(" ")[3])
        worddict[word.decode("utf8")] = (A, B, C)
    nb_clf = joblib.load(ModelFilePath)
    HtmlFiles = os.listdir(HtmlDataPath)
    k = 0
    judge=True
    for f in HtmlFiles:
        if ".DS_Store" in f:
            continue
        # print HtmlDataPath + "/" + f
        htmls = os.listdir(HtmlDataPath + "/" + f)
        for hhtml in htmls:
            if ".DS_Store" in f:
                continue
            k = k + 1
            # print k
            fo = open(HtmlDataPath + "/" + f + "/"+hhtml, "r")
            html = fo.read()
            fo.close()
            try:
                html = html.decode('utf8')
            except:
                try:
                    html = html.decode('gbk')
                except:
                    html = html
            # html=html.decode('utf8')
            judge, nb_clf, wordict = Judge(str(f), worddict, html, ORValueFilePath, nb_clf, KeyList, AllkeyValueDict)
            if judge:
                print str(hhtml) + "is spam"
                folder = os.path.exists(SpamPath + "/" + f)
                if not folder:
                    os.makedirs(SpamPath + "/" + f)
                # fo = open(SpamPath + "/" + f, "w")
                fo = open(SpamPath + "/" + f + "/" + hhtml, "w")
                fo.write(html)
                fo.close()
            else:
                print str(hhtml) + "is not spam"
                folder = os.path.exists(NonSpamPath + "/" + f)
                if not folder:
                    os.makedirs(NonSpamPath + "/" + f)
                fo = open(NonSpamPath + "/" + f + "/" + hhtml, "w")
                # fo = open(NonSpamPath + "/" + f, "w")
                fo.write(html)
                fo.close()

    for word in worddict:
        fo = open(NewORValueFilePath, "ab+")
        fo.write(word.decode("utf8") + " " + str(int(worddict[word.decode("utf8")][0])) + " " + str(
            int(worddict[word.decode("utf8")][1])) + " " + str(worddict[word.decode("utf8")][2]) + "\n")
        fo.close()
    joblib.dump(nb_clf, NewModelFilePath)

    spams=os.listdir(SpamPath)

    csvFile = open('../WebspamDetect/Result/spams.csv', 'w') #存储结果的csv文件
    writer = csv.writer(csvFile)
    writer.writerow(["host","url"])
    for host in spams:
        if ".DS_Store" in host:
            continue
        for url in os.listdir(SpamPath+"/"+host):
            if ".DS_Store" in host:
                continue
            writer.writerow([host,fng.DeGenerate(url)])

    csvFile.close()


if __name__ != '__main__':
    HtmlDataPath = "../Result/data"  # 检测的网页在的路径
    SpamPath = "../Result/spam"  # spam被分到的路径
    NonSpamPath = "../Result/nonspam"  # nonspam被分到的路径
    HtmlFiles = os.listdir(HtmlDataPath)
    print HtmlFiles

    KeyEnumFilePath = "../DetectModel/Key.txt"  # html标签文件
    ORValueFilePath = "../DetectModel/AssetValuemy/TextAB+1ORValueWithoutLog.txt"  # 优势模型
    NewORValueFilePath = "../DetectModel/AssetValuemy/TextAB+1ORValueWithoutLogV10.txt"  # 新优势模型
    ModelFilePath = "../DetectModel/modelmy/nb_train_model_without_text_with_text.m"  # nb模型
    NewModelFilePath = "../DetectModel/Tag.txt"  # 新nb模型
    AttributesDirectoryPath = "../DetectModel/Attributes"  # 属性文件

    HtmlFiles = os.listdir(AttributesDirectoryPath)
    print HtmlFiles

    fo = open(ORValueFilePath, "r")
    fo.close()
    fo = open(NewORValueFilePath, "r")
    fo.close()
    fo = open(ModelFilePath, "r")
    fo.close()
    fo = open(NewModelFilePath, "r")
    fo.close()