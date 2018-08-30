from PyQt5.QtWidgets import QTableView, QWidget, QApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyWindow(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle(title)
        self.ui_init()
        self.show()

    def ui_init(self):
        self.tableView = QTableView()
        self.model = QStandardItemModel(4, 4)
        print(self.model)


app = QApplication([])
win = MyWindow("TableView")
exit(app.exec())
