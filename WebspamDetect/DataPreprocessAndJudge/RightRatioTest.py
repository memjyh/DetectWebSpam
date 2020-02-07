# -*- coding: UTF-8 -*-

import os,sys
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr  
reload(sys)  
sys.setdefaultencoding( "utf-8" ) 
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir)
sys.path.insert(0,parentdir+"/Common")

if __name__ == '__main__':
    RightSpamClassicationPath = "/Volumes/E/ExperimentSample/RightClassification/spam"
    RightNonSpamClassicationPath = "/Volumes/E/ExperimentSample/RightClassification/nonspam"
    ResultSpamClassicationPath = "/Volumes/E/ExperimentSample/Classification20/spam"
    ResultNonSpamClassicationPath = "/Volumes/E/ExperimentSample/Classification20/nonspam"
    rightspam = os.listdir(RightSpamClassicationPath)
    rightnonspam =os.listdir(RightNonSpamClassicationPath)
    resultspam=os.listdir(ResultSpamClassicationPath)
    resultnonspam=os.listdir(ResultNonSpamClassicationPath)

    spamwrong=[]
    spamright =[]
    nonspamwrong =[]
    nonspamright=[]
    for f in resultspam:
       if f in rightspam:
           spamright.append(f)
       else:

           nonspamwrong.append(f)
    for f in resultnonspam:
        if f in rightnonspam:
            nonspamright.append(f)
        else:
            spamwrong.append(f)

    print "Lb:",len(spamwrong)
    print "Wb:",len(nonspamwrong)
    print "Sr:",len(spamright)
    print "Nr:",len(nonspamright)
    # print 'wb:'
    # for wrong in nonspamwrong:
    #     print wrong
    # print 'lb'
    # for wrong in spamwrong:
    #     print wrong
    # print 'sr'
    # for right in spamright:
    #     print right
    
    
