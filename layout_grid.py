from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import *
import sys


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("网状布局")
        self.move(400, 300)
        self.setSizeIncrement(200, 200)
        pal = QPalette()
        pal.setColor(QPalette.ButtonText, Qt.red) #设置按键字体为红色

        names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        # values = range(0, 9)
        positions = [(i, j) for i in range(3) for j in range(4)]

        layout = QGridLayout()
        self.setLayout(layout)
        for item, name in zip(positions, names):
            btn = QPushButton(name, self)
            btn.clicked.connect(lambda: self.btn_clicked(int(name)))
            layout.addWidget(btn, *item)


    def btn_clicked(self, n):
        print(n)


app = QApplication(sys.argv)
form = MyWindow()
form.show()
sys.exit(app.exec())