#!python3.7.3
# -*- coding:utf-8 -*-


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from source.view.view_base import BaseView


def createDialog(*args):
    if len(args) != 2:
        raise Exception('parameter error!!!')

    _template_path = args[0]
    _image_path = args[1]

    form_class = uic.loadUiType(_template_path)[0]

    class Registry(QDialog, form_class,BaseView):
        LEStyle = 'color:white;padding-left:10px;border-radius: 5px;'

        def __init__(self):
            QDialog.__init__(self)
            self.setupUi(self)

            self._setLayout_()

        def _setLayout_(self):
            self.le_email.setPlaceholderText('이메일')
            self.le_pwd.setPlaceholderText('암호')
            self.le_pwd_confirm.setPlaceholderText('확인')

            self._setStyle_((self.le_email, self.le_pwd, self.le_pwd_confirm,), _style=Registry.LEStyle)

            self._loadImage_()

        def _loadImage_(self):
            self.qmapImagVar = QPixmap()
            self.qmapImagVar.load(_image_path)
            self.qmapImagVar = self.qmapImagVar.scaledToWidth(200)
            self.qmapImagVar = self.qmapImagVar.scaledToHeight(190)
            self.lbl_registry_icon.setPixmap(self.qmapImagVar)


    return Registry()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qd = createDialog('../resources/template/registry.ui', '../resources/image/registry_icon.png')
    qd.show()
    sys.exit(app.exec_())
