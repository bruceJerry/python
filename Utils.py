from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Color(QObject):
    def __init__(self):
        super().__init__()

    @staticmethod
    def setWidgetBackgroundColor(widget, color):
        pal = widget.palette()
        pal.setColor(QPalette.Window, color)  # 设置背景颜色
        widget.setPalette(pal)
