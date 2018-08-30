from PyQt5.QtWidgets import QTableView, QWidget, QApplication, QVBoxLayout, QHeaderView, QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyWindow(QWidget):
    selectRow = 0

    def __init__(self, title):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle(title)
        self.ui_init()
        print(self.selectRow)
        self.show()

    def ui_init(self):
        self.tableView = QTableView()

        self.model = QStandardItemModel(4, 4) # 添加到tableview的数据结构

        self.model.setHorizontalHeaderLabels(["标题1", "标题2", "标题3", "标题4"])
        self.model.setVerticalHeaderLabels(["标题1", "标题2", "标题3", "标题4"])

        for row in range(4):
            for column in range(4):
                item = QStandardItem("row %s, col %s" % (row, column))
                self.model.setItem(row, column, item)

        self.tableView = QTableView()
        self.tableView.setModel(self.model)  # 给tableView绑定数据
        self.tableView.clicked.connect(self.btn_clicked)
        self.tableView.tag = 3
        # 下面方法只能拉伸最后一列
        # self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout = QVBoxLayout()
        layout.addWidget(self.tableView)

        self.btn1 = QPushButton("增加数据")
        self.btn1.clicked.connect(self.btn_clicked)
        self.btn1.tag = 1

        self.btn2 = QPushButton("减少数据")
        self.btn2.clicked.connect(self.btn_clicked)
        self.btn2.tag = 2

        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        self.setLayout(layout)

    def btn_clicked(self):
        sender = self.sender()
        if sender.tag == 1:  # 增加
            self.model.appendRow([QStandardItem("1"), QStandardItem("1"), QStandardItem("1"), QStandardItem("1")])

        elif sender.tag == 2:  # 减少
            self.model.removeRow(self.selectRow)

        elif sender.tag == 3:  # 选中
            index = sender.currentIndex()
            self.selectRow = index.row()
            print(index.row(), index.column())


app = QApplication([])
win = MyWindow("TableView")
exit(app.exec())
