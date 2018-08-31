from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyTableWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("tableWidget")
        self.setGeometry(300, 300, 600, 300)
        self.ui_init()
        self.show()

    def ui_init(self):
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tab1_init()
        self.tab2_init()
        self.tab3_init()

        self.addTab(self.tab1, "tab1")
        self.setTabText(0, "联系方式")
        self.addTab(self.tab2, "tab2")
        self.setTabText(1, "个人信息")
        self.addTab(self.tab3, "tab3")
        self.setTabText(2, "教育程度")

    def tab1_init(self):
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.tab1.setLayout(layout)

    def tab2_init(self):
        layout = QFormLayout()
        sublayout = QHBoxLayout()
        sublayout.addWidget(QRadioButton("男"))
        sublayout.addWidget(QRadioButton("女"))
        layout.addRow("性别", sublayout)
        layout.addRow("生日",QLineEdit())
        self.tab2.setLayout(layout)

    def tab3_init(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("化学"))
        self.tab3.setLayout(layout)


app = QApplication([])
win = MyTableWidget()
exit(app.exec())
