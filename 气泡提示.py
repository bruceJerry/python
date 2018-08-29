import sys
from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication, QDesktopWidget, QHBoxLayout, QWidget, QToolTip, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont, QPalette
from PyQt5.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("关闭窗口")
        self.setWindowIcon(QIcon("123.png"))

        pal = QPalette()
        pal.setColor(QPalette.Window, Qt.gray)

        # 气泡提示控件
        QToolTip.setFont(QFont("SansSerif", 10))
        self.setToolTip("这是一个<b>气泡提示<b>")
        self.resize(600, 600)
        self.move(400, 200)


        self.label = QLabel("这是第一个标签")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setAutoFillBackground(True)
        self.label.setPalette(pal)
        

        self.label1 = QLabel()
        self.label1.setAlignment(Qt.AlignVCenter)
        self.label1.setAutoFillBackground(True)
        self.label1.setPalette(pal)
        self.label1.setText("<A href = 'http://www.baidu.com'>欢迎使用</a>")  # html
        self.label1.setOpenExternalLinks(True)

        frame = QWidget()
        self.setCentralWidget(frame)
        layout = QHBoxLayout()
        layout.addStretch()
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(self.label1)
        layout.addStretch()
        frame.setLayout(layout)


app = QApplication(sys.argv)
form = MyWindow()
form.show()
sys.exit(app.exec())