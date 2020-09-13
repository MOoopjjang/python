#!python3
# -*- coding:utf-8 -*-



import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MySignal(QObject):
    signal1 = pyqtSignal()

    def run(self):
        self.signal1.emit()



class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mysignal = MySignal()
        mysignal.signal1.connect(self.signal1_emmit)

    @pyqtSlot()
    def signal1_emmit(self):
        print('signal1_emmit')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MyWindow()
    m.show()


    sys.exit(app.exec_())
