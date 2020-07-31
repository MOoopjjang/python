#!python3.7.3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

from src.python.view.view_base import BaseView
import src.python.common.application_context as ctx

def getInstance():
    form_class = uic.loadUiType(ctx.getInstance().getTemplatePath('main.ui'))[0]
    class MPWMain(QDialog , form_class , BaseView):
        TEXT_STYLE_1= 'font-size:14px;font-weight:bold;'
        def __init__(self):
            QDialog.__init__(self)
            self.setupUi( self )

            self._setLayout_()

        def _setLayout_(self):
            self._setStyle_((self.lbl_userinfo,) , _style=MPWMain.TEXT_STYLE_1)
#            self._setStyle_((self.btn_logout,) , _style=MPWMain.BUTTON_STYLE_1)


    return MPWMain()




if __name__ == '__main__':
    import src.python.defines.defines as df

    df.initRepositoryPath(__file__)

    app = QApplication(sys.argv)
    mpmwmain = getInstance()
    mpmwmain.show()
    sys.exit(app.exec_())
