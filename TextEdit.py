import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self):
        self.setWindowTitle("TextEdit")
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.text_edit = QTextEdit()
        text_btn = QPushButton("显示文本")
        text_btn.tag = 1
        text_btn.clicked.connect(self.btn_clicked)
        html_btn = QPushButton("显示html")
        html_btn.tag = 2
        html_btn.clicked.connect(self.btn_clicked)
        layout.addWidget(self.text_edit)
        layout.addWidget(text_btn)
        layout.addWidget(html_btn)

    def btn_clicked(self):
        tag = self.sender().tag
        if tag == 1:
            self.text_edit.setPlainText("Hello PyQt!")
        else:
            self.text_edit.setHtml("<font color='red' size='6'><red>Hello bruce</font>")


app = QApplication(sys.argv)
win = MyWindow()
win.show()
exit(app.exec())
