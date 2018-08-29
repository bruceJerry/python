from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyLineEdit(QLineEdit):
    clicked = pyqtSignal()

    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event):   # 重写了mouseReleaseEvent事件
        if event.button() == Qt.LeftButton:
            self.clicked.emit()


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("对话框")
        self.resize(300, 400)
        self.ui_init()
        self.show()

    def ui_init(self):
        btn = QPushButton("弹出对话框")
        btn.clicked.connect(self.btn_clicked)
        btn.tag = 1

        btn1 = QPushButton("弹出消息窗口")
        btn1.clicked.connect(self.btn_clicked)
        btn1.tag = 2

        btn2 = QPushButton("弹出字体选择框")
        btn2.clicked.connect(self.btn_clicked)
        btn2.tag = 3

        btn3 = QPushButton("选择文本文件")
        btn3.clicked.connect(self.btn_clicked)
        btn3.tag = 4

        self.textfield = QTextEdit()
        self.label = QLabel()

        btn4 = QPushButton("选择图片")
        btn4.clicked.connect(self.btn_clicked)
        btn4.tag = 5

        self.label.setText("image")

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(btn)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(self.textfield)
        layout.addWidget(btn4)
        layout.addWidget(self.label)

        layout1 = QFormLayout()
        layout.addLayout(layout1)

        self.lineEdit_list = MyLineEdit()
        self.lineEdit_list.setPlaceholderText("点击后选择")
        self.lineEdit_list.clicked.connect(self.input)
        self.lineEdit_list.tag = 1
        layout1.addRow("获得列表的选项", self.lineEdit_list)

        self.lineEdit_str = MyLineEdit()
        self.lineEdit_str.setPlaceholderText("点击后选择")
        self.lineEdit_str.clicked.connect(self.input)
        self.lineEdit_str.tag = 2
        layout1.addRow("获得字符串", self.lineEdit_str)

        self.lineEdit_int = MyLineEdit()
        self.lineEdit_int.setPlaceholderText("点击后选择")
        self.lineEdit_int.clicked.connect(self.input)
        self.lineEdit_int.tag = 3
        layout1.addRow("获得整数", self.lineEdit_int)

    def input(self):
        tag = self.sender().tag
        if tag == 1:
            lists = ["C", "C++", "JAVA", "PYTHON"]
            strs = self.sender().text()
            if strs:
                index = lists.index(strs)
            else:
                index = 0
            item, btn = QInputDialog.getItem(self, "输入对话框", "语言列表", lists, index, False)
            if item and btn:
                self.sender().setText(item)
        elif tag == 2:
            text, btn = QInputDialog.getText(self, "输入对话框", "请输入姓名")
            if text and btn:
                self.sender().setText(text)
        elif tag == 3:
            num, btn = QInputDialog.getInt(self, "输入对话框", "请输入学号", 1, -1, 9) #无法选择0
            if num and btn:
                self.sender().setText(str(num))

    def btn_clicked(self):
        sender = self.sender()
        if sender.tag is 1:
            dialog = QDialog()
            dialog.setWindowTitle("对话框")
            dialog.resize(200, 100)
            dialog.setWindowModality(Qt.ApplicationModal) # 只有关闭子窗口才能关闭后面的窗口
            dialog.exec()
        elif sender.tag is 2:
            btn = QMessageBox.information(self, "标题", "消息正文", QMessageBox.Yes | QMessageBox.No)
            if btn == QMessageBox.Yes:
                print("Yes")
            elif btn == QMessageBox.No:
                print("No")
        elif sender.tag is 3:
            font, ok = QFontDialog.getFont()
            if font and ok:
                sender.sender().setFont(font)
        elif sender.tag is 4:
            name, ok = QFileDialog.getOpenFileName(self, "打开文件", ".")
            if name and ok:
                print(name)
                with open(name, "r") as f:
                    content = f.read()
                    self.textfield.setText(content)
        elif sender.tag is 5:
            name, ok = QFileDialog.getOpenFileName(self, "打开文件", ".", "(*.png *.jpg)")
            if name and ok:
                print(name)
                self.label.setAlignment(Qt.AlignCenter)
                self.label.setPixmap(QPixmap(name))


app = QApplication([])
win = MyWindow()
exit(app.exec())

