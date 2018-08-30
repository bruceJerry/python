import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpinBox, QApplication, QSlider, QComboBox, QLabel, QHBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self):
        self.setWindowTitle("SpinBox计数器")
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("当前值:")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.spin_box = QSpinBox()
        self.spin_box.valueChanged.connect(self.value_changed)
        layout.addWidget(self.spin_box)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.valueChanged.connect(self.value_changed)
        layout.addWidget(self.slider)



    def value_changed(self):
        sender = self.sender()
        print(sender.value())
        self.label.setText("当前值:%s" % str(sender.value()))



app = QApplication(sys.argv)
win = MyWindow()
win.show()
exit(app.exec())
