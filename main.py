import sys
from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication, QDesktopWidget, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *
from SubSystem import Person


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.statusBar().showMessage("状态栏", 5000)
        self.setWindowTitle("窗口")

        self.button = QPushButton("按钮", self)
        self.button.move(200, 200)

        self.label = QLabel("标签", self)
        self.label.move(200, 300)
        self.label.setText("改后的标签")
        self.label.setFont(QFont("宋体", 10, QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.size()
        print(screen, size)
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)


app = QApplication(sys.argv)
app.setWindowIcon(QIcon("123.png"))
form = MyWindow()
form.center()
form.show()
p = Person("bruce", 100)
p.eat()
p.test()
sys.exit(app.exec_())