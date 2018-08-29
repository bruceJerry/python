from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import serial.utilities
import serial.tools.list_ports


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("串口")
        self.setGeometry(200, 200, 400, 400)

    def ui_init(self):
        self.serial = serial()


app = QApplication([])
win = MyWindow()
win.show()
exit(app.exec())
