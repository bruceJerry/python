from pymongo import MongoClient

settings = {
    "ip": "localhost",          # ip
    "port": 27017,               # 端口
    "db_name": "db_test",    # 数据库名字
    "set_name": "students"   # 集合名字
}


class MyMongoDB(object):
    def __init__(self):
        try:
            self.conn = MongoClient(settings["ip"], settings["port"])
        except Exception as e:
            print(e)
        self.db = self.conn[settings["db_name"]]
        self.my_set = self.db[settings["set_name"]]

    def display_db(self, dic={}):
        res = self.my_set.find(dic, {"_id": 0})
        for doc in res:
            print(doc)


def main():
    dics = [{"name": "bruce", "age": 38}, {"name": "linda", "age": 28}, {"name": "jerry", "age": 18}]
    mongo = MyMongoDB()
    #mongo.my_set.insert_many(dics)
    mongo.display_db()

    mongo.my_set.update_one({"name": "jerry"}, {"$set": {"age": 19}})

    mongo.display_db()
    #mongo.my_set.delete_many({"name":"bruce"})
    #mongo.delete({"name":"zhangsan"})


if __name__ == "__main__":
    main()