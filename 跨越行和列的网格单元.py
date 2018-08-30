import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self):
        self.setWindowTitle("网格布局")
        layout = QGridLayout()
        self.setLayout(layout)

        label_title = QLabel("标题")
        lineEdit_title = QLineEdit()
        label_name = QLabel("提交人")
        lineEdit_name = QLineEdit()
        label_content = QLabel("内容")
        lineEdit_content = QTextEdit()

        layout.addWidget(label_title, 0, 0)
        layout.addWidget(lineEdit_title, 0, 1)
        layout.addWidget(label_name, 1, 0)
        layout.addWidget(lineEdit_name, 1, 1)
        layout.addWidget(label_content, 2, 0, Qt.AlignTop)
        layout.addWidget(lineEdit_content, 2, 1, 5, 1)


app = QApplication(sys.argv)
win = MyWindow()
win.show()
exit(app.exec())
