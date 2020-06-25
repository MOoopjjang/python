#!python3
# -*- coding:utf-8 -*-


'''
- 인증기능 + 계정별 목록관리 기능 + 파일로 저장기능
- 클립보드 복사기능
- 관리자 기능
'''

import source.view.login as lg
from source.view.login import *
import source.defines.defines as df

import source.common.application_context as ctx

def init():
    df.initRepositoryPath(__file__)
    ctx.getInstance()



def main():
    init()

    app = QApplication(sys.argv)
    wLogin = lg.createLogin('./resources/template/login.ui','./resources/image/login_icon.png')
    wLogin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
