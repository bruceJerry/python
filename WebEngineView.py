from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


class MyWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WebView")
        self.setGeometry(200, 200, 1400, 800)
        self.ui_init()
        self.show()

    def ui_init(self):
        self.web_view = QWebEngineView()
        # url = "http://www.baidu.com"  # 加载远端网络
        url ="F:/VR001"  # 加载本地文件夹
        self.web_view.load(QUrl(url))
        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        self.setLayout(layout)

app = QApplication(["hello"])
timer = MyWindows()
exit(app.exec())

