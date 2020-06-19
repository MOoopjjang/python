#!python3.7.3
# -*- coding:utf-8 -*-

from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class CustomQLabel(QLabel):
    clicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super(CustomQLabel, self).__init__(parent)

    def mousePressEvent(self, event):
        self.ultimo = "Clic"

    def mouseReleaseEvent(self, event):
        self.clicked.emit(self.ultimo)
