from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("菜单栏")
        self.move(300, 300)
        self.resize(400, 300)
        menu_bar = self.menuBar()
        print(menu_bar)
        file = menu_bar.addMenu("文件")
        file.addAction("新建")
        save = QAction("保存", self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)
        file.triggered[QAction].connect(self.processor_menu)
        self.init_tool_bar()
        self.show()

    def init_tool_bar(self):
        tb = self.addToolBar("文件")
        open = QAction(QIcon("open.png"), "打开文件", self)
        tb.addAction(open)
        save = QAction(QIcon("save.png"), "保存文件", self)
        tb.addAction(save)

        tb.actionTriggered[QAction].connect(self.processor_tool) # 发射信号

    def processor_menu(self, q):
        print(q.text())

    def processor_tool(self, q):
        print(q.text())


app = QApplication([])
win = MyWindow()
exit(app.exec())