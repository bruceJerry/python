from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Utils import Color
import time


class MyWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProcessEvent")
        self.setGeometry(200, 200, 400, 400)
        self.show()
        self.ui_init()

    def ui_init(self):
        self.listWidget = QListWidget()
        self.btn_start = QPushButton("开始")
        layout = QGridLayout()
        layout.addWidget(self.listWidget)
        layout.addWidget(self.btn_start)
        self.btn_start.clicked.connect(self.clicked)
        self.setLayout(layout)

    def clicked(self):
        for n in range(10):
            str_n = "file {}".format(n)
            self.listWidget.addItem(str_n)
            QApplication.processEvents()
            time.sleep(1)


app = QApplication(["hello"])
timer = MyWindows()
exit(app.exec())

