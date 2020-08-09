#!python3.7.3
# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class CustomBlinkTextBrowser(QTextBrowser):
    def __init__(self):
        QTextBrowser.__init__(self)

    def __getattr__(self, item):
        def method(*argv):
            return getattr(self , item)
        return method

