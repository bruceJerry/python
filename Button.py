import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QCheckBox, QRadioButton, QGroupBox, QHBoxLayout
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

        btn1 = QPushButton("&PUSH")
        # btn1.setDefault(True)
        layout.addWidget(btn1)

        btn2 = QRadioButton("回家")
        btn2.setChecked(True)
        btn2.toggled.connect(self.btn_toggled)
        btn2.tag = 1
        btn3 = QRadioButton("离家")
        btn3.toggled.connect(self.btn_toggled)
        btn3.tag = 2
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        group_box = QGroupBox("CHECKBOX")
        layout.addWidget(group_box)

        check_box1 = QCheckBox("CHECKBOX1")
        check_box1.stateChanged.connect(self.btn_toggled)
        check_box1.tag = 3
        check_box2 = QCheckBox("CHECKBOX2")
        check_box2.stateChanged.connect(self.btn_toggled)
        check_box2.tag = 4
        check_box3 = QCheckBox("CHECKBOX3")
        check_box3.stateChanged.connect(self.btn_toggled)
        check_box3.tag = 5
        layout_group_box = QHBoxLayout()
        group_box.setLayout(layout_group_box)

        layout_group_box.addWidget(check_box1)
        layout_group_box.addWidget(check_box2)
        layout_group_box.addWidget(check_box3)




    def btn_toggled(self):
        sender = self.sender()
        tag = sender.tag
        if sender.isChecked():
            if tag == 1:
                print("回家")
            elif tag == 2:
                print("离家")
            elif tag == 3:
                print("卧室")
            elif tag == 4:
                print("客厅")
            elif tag == 5:
                print("厨房")


app = QApplication(sys.argv)
win = MyWindow()
win.show()
exit(app.exec())
