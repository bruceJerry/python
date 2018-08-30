from PyQt5.QtWidgets import QTableView, QWidget, QApplication, QVBoxLayout, QHeaderView, QTableWidgetItem, QListView, QTableWidget, QListWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyWindow(QWidget):
    selectRow = 0

    def __init__(self, title):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle(title)
        self.ui_init()
        self.show()

    def ui_init(self):
        self.listView = QListView()
        model = QStringListModel()
        self.qList = ["Item1", "Item2", "Item3", "Item4"]
        model.setStringList(self.qList)
        self.listView.setModel(model)
        self.listView.clicked.connect(self.clicked)
        layout = QVBoxLayout()
        layout.addWidget(self.listView)

        self.listWidget = QListWidget()
        self.listWidget.addItems(self.qList)
        self.listWidget.clicked.connect(self.clicked)
        layout.addWidget(self.listWidget)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        layout.addWidget(self.tableWidget)
        item00 = QTableWidgetItem("bruce")
        item00.setTextAlignment(Qt.AlignCenter)  # 设置单元格字体对齐方式
        item01 = QTableWidgetItem("80kg")
        item02 = QTableWidgetItem("180cm")
        self.tableWidget.setItem(0, 0, item00)
        self.tableWidget.setItem(0, 1, item01)
        self.tableWidget.setItem(0, 2, item02)
        self.tableWidget.clicked.connect(self.clicked)

        self.setLayout(layout)

    def clicked(self, index):  # 获取选中的item的数据
        print(index.row(), index.column(), self.tableWidget.model().data(index))


app = QApplication([])
win = MyWindow("ListView")
exit(app.exec())
