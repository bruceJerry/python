from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Utils import Color
import time


class MyWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProcessEvent")
        self.setGeometry(200, 200, 400, 100)
        self.show()
        self.ui_init()

    def ui_init(self):
        pass


app = QApplication(["hello"])
timer = MyWindows()
exit(app.exec())

