from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Utils import Color
from PyQt5.QtGui import *


class SendWidget(QWidget):
    singal_send = pyqtSignal(str)

    def __init__(self, name):
        super().__init__()
        self.setWindowTitle(name)
        self.resize(200, 200)
        self.move(200, 200)
        self.btn = QPushButton("AA", self)
        self.btn.clicked.connect(self.clicked)
        Color.setWidgetBackgroundColor(self, Qt.gray)
        self.show()

    def clicked(self):
        self.singal_send.emit("bruce")


class RecWidget(QWidget):
    cnt = 0

    def __init__(self, name):
        super().__init__()
        self.setWindowTitle(name)
        self.resize(200, 200)
        self.move(500, 200)
        self.line_edit = QLineEdit(self)
        self.line_edit.setAlignment(Qt.AlignLeft)
        self.line_edit.setPlaceholderText("等待接收...")
        self.show()

    def recived_msg(self, msg):
        self.cnt += 1
        str = "hello[{}]:{}".format(self.cnt, msg)
        print(str)
        self.line_edit.setText(str)


app = QApplication([])
win2 = RecWidget("接收")
win1 = SendWidget("发射")
win1.singal_send.connect(win2.recived_msg)
exit(app.exec())