# -*- coding: UTF-8 -*-


import pymongo


myclient = pymongo.MongoClient('localhost',27017)
db=myclient.mydb
my_set=db.test_set

allData=[]

#删除数据
my_set.remove({'name': 'zhangsan'})
my_set.remove({'name': 'lisi'})

#插入数据
users=[{"name":"zhangsan","age":18},{"name":"lisi","age":20}]
my_set.insert(users)

#查询全部
for i in my_set.find():
    data = []
    print(i)
    data.append(i["name"])
    data.append(i["age"])
    print data
    allData.append(data)
print allData


#查询name=zhangsan的
# for i in my_set.find({"name":"zhangsan"}):
#     print(i)
# print(my_set.find_one({"name":"zhangsan"}))