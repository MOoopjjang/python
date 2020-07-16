#!python3.7.3
# -*- coding:utf-8 -*-


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

from src.python.view.custom_qlabel import CustomQLabel
import src.python.common.application_context as ctx
import src.python.manager.mauthenticationmanager as mam
from src.python.view.view_base import BaseView
import src.python.view.registry as reg
import src.python.view.custom_alert_popup as cdp


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
            self.line_pwd.setEchoMode(QLineEdit.Password)
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
            registry = reg.createDialog(ctx.getInstance().getTemplatePath('registry.ui'), ctx.getInstance().getImagePath('registry_icon.png'))
            registry.show()
            registry.setModal(True)
            registry.exec()


        def _loadImage_(self):
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load(_image_path)
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(210)
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToHeight(170)
            self.lbl_icon.setPixmap(self.qPixmapFileVar)

        '''
         - 로그인 인증 진행
        '''
        def _login_(self):
            context = ctx.getInstance()
            authenticationManager = context.getComponent(mam.__file__)
            if authenticationManager.certification(self.line_username.text() , self.line_pwd.text()) == False:
                popup = cdp.createDialog()
                popup.setText('등록된 사용자가 아닙니다.') \
                    .setIConImage({'path': ctx.getInstance().getImagePath("alert_icon.png"), "w": 62, "h": 52}) \
                    .setButtons([
                    {'text': 'OK', 'listener': lambda p:print('{}'.format(p))}
                ]).show()
                popup.exec()
            else:
                import src.python.manager.security_context_holder as sch
                securityContextHolder = context.getComponent(sch.__file__)
                securityContextHolder.setAuthentication(authenticationManager.getMember(self.line_username.text()))
                print('login Success ---> {}'.format(securityContextHolder))



    return Login()


if __name__ == '__main__':
    import src.python.defines.defines as df

    df.initRepositoryPath(__file__)
    app = QApplication(sys.argv)

    winlogin = createLogin(ctx.getInstance().getTemplatePath('login.ui'), ctx.getInstance().getImagePath('login_icon.png'))
    winlogin.show()
    app.exec_()
