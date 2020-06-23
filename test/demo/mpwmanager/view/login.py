#!python3.7.3
# -*- coding:utf-8 -*-


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from view.custom_qlabel import CustomQLabel
import view.registry as reg
from view.registry import *
from view.view_base import BaseView


def createLogin(*args):
    if len(args) != 2:
        raise Exception('parameter 오류')

    _template_path = args[0]
    _image_path = args[1]

    form_class = uic.loadUiType(_template_path)[0]

    class Login(QDialog, form_class, BaseView):
        LEStyle = 'color:white;padding-left:10px;border-radius: 5px;'
        PBStyle = 'border: 1px solid white;border-radius:5px;'
        LBStyle = 'color:white;text-align:right;border-bottom-width:2px;border-bottom-color:white;border-bottom-style:solid;border-radius:0px;'
        TRANSPARENT_BG = 'opacity:0;border:0;'

        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.setFixedSize(400, 540)

            self._setLayout_()

        def _setLayout_(self):
            self.lb_registry = CustomQLabel()
            self.lb_registry.setText("가입하기")
            self.lb_registry.setGeometry(70, 460, 280, 20)
            self.lb_registry.clicked.connect(self._registry_)

            self.btn_login.clicked.connect(self._login_)
            self.line_username.setPlaceholderText('이메일')
            self.line_pwd.setPlaceholderText('패스워드')

            # StyleSheet 적용
            self._setStyle_((self.line_username, self.line_pwd), _style=Login.LEStyle)
            self._setStyle_((self.btn_login,), _style=Login.PBStyle)
            self._setStyle_((self.lb_registry,), _style=Login.LBStyle)

            self._loadImage_()

            # 회원가입 UI
            hbox = QHBoxLayout()
            hbox.setAlignment(Qt.AlignRight)
            hbox.addWidget(self.lb_registry)
            self.gb_registry.setLayout(hbox)
            self._setStyle_((self.gb_registry,), _style=Login.TRANSPARENT_BG)

        def _registry_(self, action):
            registry = reg.createDialog('./resources/template/registry.ui', './resources/image/registry_icon.png')
            registry.show()
            registry.exec()

        # def _setStyle_(self, args, *, _style=None):
        #    for e in args: e.setStyleSheet(_style)

        def _loadImage_(self):
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load(_image_path)
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(210)
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToHeight(170)
            self.lbl_icon.setPixmap(self.qPixmapFileVar)

        def _login_(self):
            registry = reg.createDialog('./resources/template/registry.ui', './resources/image/registry_icon.png')
            registry.show()
            registry.exec()

    return Login()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    winlogin = createLogin('../resources/template/login.ui', '../resources/image/login_icon.png')
    winlogin.show()
    app.exec_()
