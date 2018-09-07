from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Utils import Color
from PyQt5.QtGui import *
from pymongo import MongoClient
from cv2 import imshow

class MyWidget(QWidget):

    def __init__(self, name):
        super().__init__()
        self.setWindowTitle(name)
        self.resize(400, 200)
        self.move(200, 200)
        self.btn = QPushButton("OK", self)
        Color.setWidgetBackgroundColor(self, Qt.gray)
        self.btn.setObjectName("okButton")
        QMetaObject.connectSlotsByName(self)  # 查找类的方法名
        self.show()

    @pyqtSlot()  #声明一个槽函数
    def on_okButton_clicked(self):
        print("ok---")

    @pyqtSlot()  # 声明一个槽函数
    def on_okButton_released(self):
        print("released")

    @pyqtSlot()  # 声明一个槽函数
    def on_okButton_pressed(self):
        print("pressed")


app = QApplication([])
win2 = MyWidget("装饰器信号")
# 常见一个mongo客户端
mongo_client = MongoClient("localhost", 27017)
db = mongo_client.db_tset  # db_test为创建的数据库
collection = db.students  # students为数据库的一个集合

db1 = mongo_client.db_tset1
set1 = db1.people
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
set1.insert_many([student1, student2])
# res = collection.insert_many([student1, student2])

# mycol = mydb["sites"]
# x = mycol.find_one()

my_collection = db["students"]
# for i in my_collection.find({}, ["name", "age"]):  # 条件查询,查询指定的列
#     print(i)
for i in my_collection.find():  # 条件查询,查询指定的列
    print(i)
# for i in my_collection.find({"name": "Mike"}):  # 条件查询, 根据指定的字段的值查询
#    print(i)
my_collection.insert_one({"weight": 90})
my_collection.update_one({'name': "bruce"}, {"$set": {'weight': 68}})
# my_collection.delete_one({"name": "linda"})
print("---------------------------")
for i in my_collection.find():  # 条件查询,查询指定的列
    print(i)
exit(app.exec())
