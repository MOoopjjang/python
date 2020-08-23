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

from src.python.view.t_registry import *


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
            self.setFixedSize(826 , 486 )
            self._setLayout_()

        def _setLayout_(self):
            self.tb_invalid_notify.hide()
            self.btn_login.clicked.connect(self._login_)

            # 회원가입 UI
            # hbox = QHBoxLayout()
            # hbox.setAlignment(Qt.AlignRight)
            # hbox.addWidget(self.lb_registry)
            # self.gb_registry.setLayout(hbox)
            # self._setStyle_((self.gb_registry,), _style=Login.TRANSPARENT_BG)

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
            if authenticationManager.certification(self.le_email.text() , self.le_password.text()) == False:
                self.tb_invalid_notify.show()
            else:
                import src.python.manager.security_context_holder as sch
                securityContextHolder = context.getComponent(sch.__file__)
                securityContextHolder.setAuthentication(authenticationManager.getMember(self.le_email.text()))
                print('login Success ---> {}'.format(securityContextHolder))

                self.gb_login.deleteLater()

                registryLayout = getLayout()
                dir(self.gb_login)


                # self.gb_login.deleteLater()



    return Login()


if __name__ == '__main__':
    import src.python.defines.defines as df

    df.initRepositoryPath(__file__)
    app = QApplication(sys.argv)

    winlogin = createLogin(ctx.getInstance().getTemplatePath('main_dialog.ui'), ctx.getInstance().getImagePath('login_icon.png'))
    winlogin.show()
    app.exec_()
