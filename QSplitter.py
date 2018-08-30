import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget): # 可以动态拖拽的一种布局，少用  先不看

    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)
        self.ui_init()

    def ui_init(self):
        self.setWindowTitle("Splitter")
        layout = QGridLayout()
        self.setLayout(layout)




app = QApplication(sys.argv)
win = MyWindow()
win.show()
exit(app.exec())
