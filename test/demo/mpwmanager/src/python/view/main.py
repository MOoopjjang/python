#!python3.7.3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

from src.python.view.view_base import BaseView

def getInstance():
    form_class = uic.loadUiType('')[0]
    class MPWMain(QDialog , form_class , BaseView):
        def __init__(self):pass



    return MPWMain()




if __name__ == '__main__':
    pass