from PyQt5.QtCore import QThread,Qt,pyqtSignal, QTime, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLCDNumber, QHBoxLayout
import sys
import time
from PyQt5 import QtNetwork


class MyWindow(QWidget):

    count1 = 0
    count2 = 0
    count3 = 0
    timer = QTimer()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("demo")
        self.resize(400,100)
        self.show()

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.lcd1 = QLCDNumber()
        layout.addWidget(self.lcd1)
        self.lcd2 = QLCDNumber()
        layout.addWidget(self.lcd2)
        self.lcd3 = QLCDNumber()
        layout.addWidget(self.lcd3)

        self.timer.timeout.connect(self.timer_out)
        self.timer.start(1000)

    def timer_out(self):
        print("time out")
        self.count1 += 1
        self.count2 += 2
        self.count3 += 3

        self.lcd1.display(str(self.count1))
        self.lcd2.display(str(self.count2))
        self.lcd3.display(str(self.count3))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec())
