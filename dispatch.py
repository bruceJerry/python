from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Utils import Color


global sec
sec = 0


class WorkThread(QThread):
    signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(10000000):
            print(i)
            # self.usleep(1000)
        self.signal.emit(i)

def countTime():
    global sec
    sec += 1
    lcdNumber.display(sec)

def work():
    timer.start(1000)

def measure():
    workThread.start()

def timeStop():
    timer.stop()
    global sec
    sec = 0


app = QApplication(["hello"])
top = QWidget()
top.resize(300, 200)
layout = QVBoxLayout(top)
lcdNumber = QLCDNumber()
layout.addWidget(lcdNumber)
btn = QPushButton("测试")
btn1 = QPushButton("计时")
layout.addWidget(btn)
layout.addWidget(btn1)

timer = QTimer()
workThread = WorkThread()
workThread.signal.connect(timeStop)
btn.clicked.connect(work)
btn1.clicked.connect(measure)
timer.timeout.connect(countTime)
top.show()
exit(app.exec())