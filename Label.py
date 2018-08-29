import sys
from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication, QDesktopWidget, QHBoxLayout, QWidget, QToolTip, \
    QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont, QPalette
from PyQt5.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("关闭窗口")
        self.setWindowIcon(QIcon("123.png"))

        pal = QPalette()
        pal.setColor(QPalette.Window, Qt.gray)
        self.resize(600, 600)
        self.move(400, 200)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setAutoFillBackground(True)
        self.label.setPalette(pal)
        self.label.setOpenExternalLinks(False)
        self.label.setText("<a href='#'>欢迎使用</a>")  # html
        self.label.linkActivated.connect(lambda: self.link_clicked(1))  # 只能使用一种actived
        # self.label.linkHovered.connect(self.link_hovered) # 鼠标划过控件

        self.label2 = QLabel()
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setAutoFillBackground(True)
        self.label2.setPalette(pal)
        self.label2.setOpenExternalLinks(False)
        self.label2.setText("<a href='#'>欢迎使用</a>")  # html
        self.label2.linkActivated.connect(lambda: self.link_clicked(2))  # 只能使用一种actived

        self.label1 = QLabel()
        self.label1.setAlignment(Qt.AlignVCenter)
        self.label1.setAutoFillBackground(True)
        self.label1.setPalette(pal)
        self.label1.setText("<A href = 'http://www.baidu.com'>欢迎使用baidu</a>")  # html
        self.label1.setOpenExternalLinks(True)

        frame = QWidget()
        self.setCentralWidget(frame)
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        frame.setLayout(layout)

    def link_clicked(self, n):
        print("link_clicked %d" %n)
        print(self.sender().text())
        d = "abc"
        e = "cba"
        if d == e:
            print("####################")

    def link_hovered(self):
        sender = self.sender()
        print("link_hovered")


app = QApplication(sys.argv)
form = MyWindow()
form.show()
sys.exit(app.exec())