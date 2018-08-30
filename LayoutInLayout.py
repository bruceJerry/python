import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, QVBoxLayout, QLineEdit, QHBoxLayout, QFormLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self):
        self.setWindowTitle("网格布局")
        layout = QHBoxLayout()
        self.setLayout(layout)

        layout1 = QHBoxLayout()
        btn1 = QPushButton("1")
        btn2 = QPushButton("2")
        layout1.addWidget(btn1)
        layout1.addWidget(btn2)
        layout.addLayout(layout1)

        layout2 = QVBoxLayout()
        btn3 = QPushButton("3")
        btn4= QPushButton("4")
        layout2.addWidget(btn3)
        layout2.addWidget(btn4)
        layout.addLayout(layout2)


        layout3 = QGridLayout()
        btn5 = QPushButton("5")
        btn6= QPushButton("6")
        btn7 = QPushButton("7")
        btn8= QPushButton("8")
        layout3.addWidget(btn5, 0, 0)
        layout3.addWidget(btn6, 0, 1)
        layout3.addWidget(btn7, 1, 0)
        layout3.addWidget(btn8)
        layout.addLayout(layout3)



app = QApplication(sys.argv)
win = MyWindow()
win.show()
exit(app.exec())
