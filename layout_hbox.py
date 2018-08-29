from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import *
import sys


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("水平布局")
        self.move(400, 300)
        pal = QPalette()
        pal.setColor(QPalette.ButtonText, Qt.red) #设置按键字体为红色

        layout = QHBoxLayout()
        self.setLayout(layout)
        bt1 = QPushButton(str(1))
        bt2 = QPushButton(str(2))
        bt3 = QPushButton(str(3))
        bt4 = QPushButton(str(4))
        bt5 = QPushButton(str(5))
        layout.addWidget(bt1, 0, Qt.AlignTop)
        layout.addWidget(bt2, 0, Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(bt3, 0, Qt.AlignLeft | Qt.AlignBottom)
        layout.addWidget(bt4)
        layout.addWidget(bt5)
        bt1.setPalette(pal)


app = QApplication(sys.argv)
form = MyWindow()
form.show()
sys.exit(app.exec())