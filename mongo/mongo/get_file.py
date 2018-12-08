from pymongo import MongoClient
import bson.binary
 
conn = MongoClient('localhost',27017)
db = conn.image
myset = db.person

#文件提取
img = myset.find_one({'filename':'mm.jpg'},{'_id':0})

# print(img)

#将data域内容写入文件
with open ('mm.jpg','wb') as f:
    f.write(img['data'])


conn.close()
