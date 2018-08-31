from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Utils import Color


class Work(QThread):
    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.is_work = True
        self.num = 0

    def run(self):
        while self.is_work:
            file_str = "file index {}{} OK".format(self.num, self.num)
            self.num += 1
            self.signal.emit(file_str)
            self.sleep(1)

    def __del__(self):
        self.is_work = False
        print("self.is_work = False")
        self.wait()


class MyThread(QThread):
    started = pyqtSignal(str)
    finished = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.is_work = True

    def run(self):  # 只运行一次
        while self.is_work:
            self.sleep(1)
            print("thread run-------------------------------------------")

    def __del__(self):
        self.is_work = False
        print("self.is_work = False")
        self.wait()


class MyTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("定时器")
        self.setGeometry(200, 200, 400, 100)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_out)
        self.timer.setTimerType(Qt.PreciseTimer)
        self.ui_init()
        self.work = Work()
        self.work.signal.connect(self.work_signal)
        self.mythread = MyThread()
        self.mythread.start()
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

        self.list_info = QListWidget()
        layout.addWidget(self.list_info)

        self.btn_sure = QPushButton("确认")
        self.btn_sure.tag = 3
        self.btn_sure.clicked.connect(self.clicked)
        layout.addWidget(self.btn_sure, 2, 1, 1, 1)
        self.setLayout(layout)

    def show_time(self):
        time = QDateTime.currentDateTime()  # 获取系统时间
        time_display = time.toString("yyyy-MM-dd hh:mm:ss dddd")  # 设置时间格式
        self.label.setText(time_display)

    def timer_out(self):
        self.show_time()

    def work_signal(self, info):
        self.list_info.addItem(info)

    def clicked(self):
        tag = self.sender().tag
        if tag == 1:
            self.timer.start(1000)
            self.btn_start.setEnabled(False)
            self.btn_end.setEnabled(True)
            self.timer.singleShot(10000, self.single_shot)   # 后面的参数为定时器超时的回调函数
        elif tag == 2:
            self.timer.stop()
            self.btn_start.setEnabled(True)
            self.btn_end.setEnabled(False)
        elif tag == 3:
            self.work.start()

    def single_shot(self):
        dialog = QDialog()
        dialog.setWindowTitle("提示")
        dialog.setAutoFillBackground(True)
        Color.setWidgetBackgroundColor(dialog, Qt.yellow)
        dialog.resize(200, 100)
        QLabel("定时器运行10秒", dialog)
        dialog.setWindowModality(Qt.ApplicationModal)  # 只有关闭子窗口才能关闭后面的窗口
        dialog.exec()


app = QApplication(["hello"])
timer = MyTimer()
exit(app.exec())