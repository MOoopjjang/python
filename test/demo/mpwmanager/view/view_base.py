#!python3.7.3
# -*- coding:utf-8 -*-

class BaseView:

    def _setLayout_(self):pass

    '''
     - view에 style sheet를 셋팅한다
    '''
    def _setStyle_(self , _es , * , _style = None):
        for e in _es:e.setStyleSheet(_style)