from pymongo import MongoClient
import gridfs

#获取数据库对象
conn = MongoClient('localhost',27017)
db = conn.grid

#获取文佳集合对象
fs = gridfs.GridFS(db)

#获取文件集
files = fs.find()

for file in files:
    #通过filename属性获取文件名称
    print(file.filename)
    if file.filename == './database/1.jpg':
        # with open(file.filename,'wb') as f:
        with open('./1.jpg','wb') as f:
            #从数据库读取
            data = file.read()
            #写入本地
            f.write(data)
conn.close()