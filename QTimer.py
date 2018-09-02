from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Utils import Color


class CountThread(QThread):
    signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(5000):
            print(i)
            self.usleep(1000)
        self.signal.emit(i)


class MyTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("定时器")
        self.setGeometry(200, 200, 400, 100)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_out)

        self.count_thead = CountThread()
        self.count_thead.signal.connect(self.count_finshed)
        self.show()

        self.ui_init()

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
        self.btn_mea = QPushButton("计时")
        self.btn_mea.clicked.connect(self.clicked)
        self.btn_mea.tag = 3
        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0, 1, 3)
        layout.addWidget(self.btn_start, 1, 0)
        layout.addWidget(self.btn_end, 1, 1)
        layout.addWidget(self.btn_mea, 1, 2)
        self.setLayout(layout)

    def timer_out(self):
        time = QDateTime.currentDateTime()  # 获取系统时间
        time_display = time.toString("yyyy-MM-dd hh:mm:ss dddd")  # 设置时间格式
        self.label.setText(time_display)

    def count_finshed(self, i):
        self.timer.stop()
        dialog = QDialog()
        dialog.setWindowTitle("count运行时间")
        dialog.setAutoFillBackground(True)
        Color.setWidgetBackgroundColor(dialog, Qt.yellow)
        dialog.resize(200, 100)
        QLabel("最大计数值{}".format(i), dialog)
        dialog.setWindowModality(Qt.ApplicationModal)  # 只有关闭子窗口才能关闭后面的窗口
        dialog.exec()

    def clicked(self):
        tag = self.sender().tag
        if tag == 1:
            self.timer.start(1000)
        elif tag == 2:
            self.timer.stop()
        elif tag == 3:
            self.count_thead.start()  #  cheout


app = QApplication(["hello"])
timer = MyTimer()
exit(app.exec())