from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("绘图")
        self.resize(300, 400)
        self.ui_init()
        self.show()

    def ui_init(self):
        self.text = "欢迎QT"

    def paintEvent(self, event):  # 重写
        painter = QPainter(self)
        painter.begin(self)
        self.draw(event, painter)
        painter.end()

    def draw(self, event, painter):
        painter.setPen(QColor(168, 35, 50))
        painter.setFont(QFont("SimSun", 20))
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)


app = QApplication([])
win = MyWindow()
exit(app.exec())

