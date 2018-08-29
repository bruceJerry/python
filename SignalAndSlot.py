from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class MyWidget(QWidget):

    signal1 = pyqtSignal()  # 无参数
    signal2 = pyqtSignal(int)  # 一个参数
    signal3 = pyqtSignal(int, str)  # 两个参数
    signal4 = pyqtSignal(list)  # 列表参数
    signal5 = pyqtSignal(dict)  # 字典参数

    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号与槽")
        self.resize(400, 400)
        self.btn = QPushButton("A", self)

        self.btn.clicked.connect(self.signal1.emit)
        self.btn.clicked.connect(lambda: self.signal2.emit(5))
        self.btn.clicked.connect(lambda: self.signal3.emit(6, "bruce"))
        self.btn.clicked.connect(lambda: self.signal4.emit([1, 2, 3]))
        self.btn.clicked.connect(lambda: self.signal5.emit({"name":"bruce", "age":"33"}))

        self.signal1.connect(self.cb1)
        self.signal2.connect(self.cb2)
        self.signal3.connect(self.cb3)
        self.signal4.connect(self.cb4)
        self.signal5.connect(self.cb5)
        self.show()

    def cb1(self):
        print("signal1 emit")

    def cb2(self, val):
        print("signal2 emit, value:", val)

    def cb3(self, val, text):
        print("signal3 emit,value:", val, text)

    def cb4(self, val):
        print("signal4 emit,value:", val)

    def cb5(self, val):
        print("signal5 emit,value:", val)


app = QApplication([])
win = MyWidget()
exit(app.exec())