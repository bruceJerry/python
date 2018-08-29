import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QCheckBox, QComboBox, QGroupBox, QHBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self):
        self.setWindowTitle("各种按钮")
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.combox = QComboBox()
        self.combox.addItem("C")
        self.combox.addItem("C++")
        self.combox.addItem("Python")
        self.combox.addItems(["JAVA", "PHP", "ObjectC"])
        self.combox.currentIndexChanged.connect(self.combox_changed)
        layout.addWidget(self.combox)

    def combox_changed(self):
        sender = self.sender()
        print(sender.currentText(), sender.currentIndex())

app = QApplication(sys.argv)
win = MyWindow()
win.show()
exit(app.exec())
