#!python3
# -*- coding:utf-8 -*-


'''
- 인증기능 + 계정별 목록관리 기능 + 파일로 저장기능
- 클립보드 복사기능
- 관리자 기능
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import view.login as lg
from view.login import *


def main():
    app = QApplication(sys.argv)
    wLogin = lg.createLogin('./resources/template/login.ui','./resources/image/login_icon.png')
    wLogin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
