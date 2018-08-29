import sys
from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication, QDesktopWidget, QHBoxLayout, QWidget, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *


class MyWindow(QMainWindow):

    name = "bruce"

    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.statusBar().showMessage("状态栏", 5000)
        self.setWindowTitle("关闭窗口")
        self.setWindowIcon(QIcon("123.png"))

        self.button = QPushButton("关闭窗口")
        self.button.move(200, 200)
        self.button.clicked.connect(self.button_clicked)
        print(dir(QPushButton))

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        frame = QWidget()
        frame.setLayout(layout)
        self.setCentralWidget(frame)

    def button_clicked(self):
        print("button clicked")
        sender = self.sender() # 获取发送信号的对象
        QApplication.instance().quit()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.size()
        print(screen, size)
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)


app = QApplication(sys.argv)
# app.setWindowIcon(QIcon("123.png"))
form = MyWindow()
print(form.name)
form.center()
form.show()
sys.exit(app.exec())