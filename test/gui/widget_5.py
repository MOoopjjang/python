#!python4
# coding:utf-8

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QListView
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import QModelIndex

from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic


form_class = uic.loadUiType('widget_5.ui')[0]

class Widget_5(QWidget , form_class):
    def __init__(self):
        QWidget.__init__( self )
        self.setupUi(self)
