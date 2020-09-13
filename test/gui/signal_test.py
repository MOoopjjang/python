#!python3
# -*- coding:utf-8 -*-


import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

'''
 Reference:
  
'''

def test1():
    class Form(QDialog):
        def __init__(self , parent = None):
            QDialog.__init__(self , parent)
            self.ui = uic.loadUi('signal_test.ui' , self)
            self.ui.show()


        @pyqtSlot()
        def slot_1st(self):
            self.ui.label.setText('첫번째')

        @pyqtSlot()
        def slot_2nd(self):
            self.ui.label.setText('두번째')

        @pyqtSlot()
        def slot_3rd(self):
            self.ui.label.setText('세번째')

    app = QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec_())




def test2():
    class Form2(QWidget):
        '''
       https://github.com/RavenKyu/OpenTutorials_PyQt/blob/master/QtFramework/QtWidgets/Signal_Slot/signal_slot_00_basic.py
        '''
        def __init__(self):
            QWidget.__init__( self , flags=Qt.Widget)
            self.dl = QDial()
            self.sd = QSlider(Qt.Horizontal)
            self.init_widget()

        def init_widget(self):
            self.setWindowTitle("test")
            form_lbx = QBoxLayout(QBoxLayout.TopToBottom , parent = self)
            self.setLayout(form_lbx)

            # 시그널 슬롯 연결
            # 다이얼의 값이 변하면 슬라이더의 값을 변경하는 슬롯과 연결
            # 슬라이더의 값이 변화하면 다이얼의 값을 변경하는 슬롯과 연결
            # 두 위젯의 valueChange 시그은 현재값을 int형으로 반환
            # 두 위젯의 setValue 슬롯은 int형만을 받는다.
            self.dl.valueChanged.connect(self.sd.setValue)
            self.sd.valueChanged.connect(self.dl.setValue)

            form_lbx.addWidget(self.dl)
            form_lbx.addWidget(self.sd)

    app = QApplication(sys.argv)
    f = Form2()
    f.show()
    sys.exit(app.exec_())



def test3():
    '''
    https://github.com/RavenKyu/OpenTutorials_PyQt/blob/master/QtFramework/QtWidgets/Signal_Slot/signal_slot_02_custom_signal.py
    '''
    class TicGenerator(QThread):
        '''
        5초마다 tick 신호전달
        '''
        # 사용자 정의 시그널 선언
        # 외부에서 사용할때 tic대신 Tic을 이용하여 호출할 수 있다.
        # Qt의 시그널 및 슬롯 이름은 Camel을 사용하기 때문에 파이썬의 PEP8을 지키면서 작성한다면 name을 반드시 사용
        tic = pyqtSignal( name = 'Tic')

        def __init__(self):
            QThread.__init__( self )

        def __del__(self):
            self.wait()

        def run( self ):
            while True:
                t = int(time.time())
                if not t%5 == 0:
                    self.usleep(1)
                    continue
                self.Tic.emit()
                self.msleep(1000)


    class Form( QWidget ):
        def __init__(self):
            QWidget.__init__(self , flags = Qt.Widget)
            self.te = QTextEdit()
            self.tic_gen = TicGenerator()
            self.init_widget()
            self.tic_gen.start()


        def init_widget(self):
            self.setWindowTitle('Custom Signal')
            form_lbx = QBoxLayout(QBoxLayout.TopToBottom , parent = self)
            self.setLayout(form_lbx)

            # 시그널 슬롯 연결
            self.tic_gen.Tic.connect( lambda: self.te.insertPlainText(time.strftime('[%H:%M:%S] Tic!\n')))

            form_lbx.addWidget(self.te)


    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    test1()
    # test2()
    # test3()