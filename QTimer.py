from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Utils import Color


class MyTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("定时器")
        self.setGeometry(200, 200, 400, 400)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_out)
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.start(1000)
        self.ui_init()
        self.show()

    def ui_init(self):
        self.label = QLabel("当前时间")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setAutoFillBackground(True)  # 设置背景充满，为设置背景颜色的必要条件
        Color.setWidgetBackgroundColor(self.label, Qt.lightGray)
        self.btn_start = QPushButton("开始")
        self.btn_start.clicked.connect(self.clicked)
        self.btn_start.tag = 1
        self.btn_end = QPushButton("结束")
        self.btn_end.clicked.connect(self.clicked)
        self.btn_end.tag = 2
        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.btn_start, 1, 0)
        layout.addWidget(self.btn_end, 1, 1)
        self.setLayout(layout)

    def timer_out(self):
        print("11")

    def clicked(self):
        tag = self.sender().tag
        if tag == 1:
            pass
        elif tag == 2:
            pass


app = QApplication(["hello"])
timer = MyTimer()
exit(app.exec())