import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, QLabel, QLineEdit, QTextEdit, QFormLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self):
        self.setWindowTitle("网格布局")
        layout = QFormLayout()
        self.setLayout(layout)

        label_title = QLabel("标题")
        lineEdit_title = QLineEdit()
        label_name = QLabel("提交人")
        lineEdit_name = QLineEdit()
        label_content = QLabel("内容")
        lineEdit_content = QTextEdit()

        # 可以直接写字符串
        layout.addRow("标题", lineEdit_title)
        layout.addRow(label_name, lineEdit_name)
        layout.addRow(label_content, lineEdit_content)




app = QApplication(sys.argv)
win = MyWindow()
win.show()
exit(app.exec())
