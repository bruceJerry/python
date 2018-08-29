import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui_init()

    def ui_init(self):
        self.setWindowTitle("网格布局")
        layout = QGridLayout()
        self.setLayout(layout)

        names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        positions = [(i, j) for i in range(4) for j in range(4)]

        for name, position, value in zip(names, positions, values):
            btn = QPushButton(name)
            btn.clicked.connect(self.btn_clicked)
            btn.tag = value  # 可以随便给一个对象添加属性
            btn.bruce = "bruce"
            layout.addWidget(btn, *position)

    def  btn_clicked(self):
        sender = self.sender()
        print(sender.tag, sender.bruce)


app = QApplication(sys.argv)
win = MyWindow()
win.show()
exit(app.exec())
