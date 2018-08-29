import sys
from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication, QDialog, QHBoxLayout, QWidget, QFormLayout, \
    QLabel, QVBoxLayout, QLineEdit, QGridLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()


    def ui_init(self):
        self.setWindowTitle("QLabel例子")
        self.setGeometry(200, 200, 400, 200)

        nameLabel = QLabel("&Y用户名")
        nameLineEdit = QLineEdit()  # 文本输入框
        nameLabel.setBuddy(nameLineEdit)

        pwLabel = QLabel("&M密码") # &后面的字符为快捷键
        pwLineEdit = QLineEdit()
        pwLabel.setBuddy(pwLineEdit)
        pwLineEdit.setEchoMode(QLineEdit.Password)

        okButton = QPushButton("确认")
        okButton.clicked.connect(lambda: self.button_clicked(1))
        escButton = QPushButton("取消")
        escButton.clicked.connect(lambda: self.button_clicked(2))

        layout = QGridLayout()
        layout.addWidget(nameLabel, 0, 0) # 多个参数   控件   起始行  起始列   占用的行数  占用的列数   对齐方式
        layout.addWidget(nameLineEdit, 0, 1, 1, 2)
        layout.addWidget(pwLabel, 1, 0)
        layout.addWidget(pwLineEdit, 1, 1, 1, 2)
        layout.addWidget(okButton, 2, 1)
        layout.addWidget(escButton, 2, 2)

        self.setLayout(layout)

    @staticmethod
    def button_clicked(sel):
        print("sel = %d" %sel)



app = QApplication(sys.argv)
form = MyWindow()
form.show()
sys.exit(app.exec())