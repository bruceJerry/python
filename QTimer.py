from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QVBoxLayout, QPushButton


class MyTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("定时器")
        self.setGeometry(200, 200, 400, 400)
        self.ui_init()

    def ui_init(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_out)
        self.timer.start(1000)
        self.timer.setTimerType(Qt.PreciseTimer)

    def timer_out(self):
        sender = self.sender()
        print("hello")


app = QApplication(["hello"])
timer = MyTimer()
timer.show()
exit(app.exec())