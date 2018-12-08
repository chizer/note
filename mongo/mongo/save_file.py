from mongo import MongoClient
import bson.binary

conn = MongoClient('localhost',27017)
db = conn.image
myset = db.person

#存取图片
f = open('t.jpg','rb')
data = f.read()

#将data转为mongodb存储格式
content = bson.binary.Binary(data)

#插入集合
myset.insert({'filename':'mm.jpg','data':content})

conn.close()
