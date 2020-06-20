#!python3.7.3
# -*- coding:utf-8 -*-


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType('./template/test.ui')[0]

class Test(QDialog , form_class):
    def __init__(self):
        super().__init__()
        self.setupUi( self )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Test()
    t.show()
    app.exec_()