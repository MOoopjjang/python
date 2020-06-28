#!python3.7.3
# -*- coding:utf-8 -*-


class BaseView:

    def _setLayout_(self):pass

    def _setListener_(self):pass

    '''
     - view에 style sheet를 셋팅한다
    '''
    def _setStyle_(self , _es , * , _style = None):
        for e in _es:e.setStyleSheet(_style)

    '''
     - 경고팝업 출력
    '''
    def _showAlertDialog_(self , _iconType , _text , _infoText , _wtitle):
        from PyQt5.QtWidgets import QMessageBox

        msg = QMessageBox()
        msg.setIcon(_iconType)
        msg.setText(_text)
        msg.setInformativeText(_infoText)
        msg.setWindowTitle(_wtitle)
        msg.exec_()