#!python3.7.3
# -*- coding:utf-8 -*-

import os
from src import python as m


def tst1():
    print('{}'.format(os.path.dirname(m.__file__)))
    os.chdir(os.path.dirname(m.__file__))
    os.chdir('..')
    p = os.getcwd()
    print('p : {}'.format(p))


def tst2():
    import sys
    from PyQt5.QtWidgets import QApplication , QDialog , QPushButton
    # from PyQt5.QtCore import QPropertyAnimation
    # from PyQt5.QtGui import *
    from src.python.view.custom_blink_textbrowser import CustomBlinkTextBrowser

    app = QApplication(sys.argv)
    dlg = QDialog()
    dlg.setFixedSize(300 , 300)
    dlg.setModal(True)

    qbutton = QPushButton()
    qbutton.setText('OK')
    dlg.setW
    dlg.show()


    sys.exit(app.exec_())


    # cbtb = CustomBlinkTextBrowser()
    # cbtb.setFixedSize(300,60)






if __name__ == '__main__':
    # tst1()
    tst2()
