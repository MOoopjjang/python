#!python3
# -*- coding:utf-8 -*-


'''
- 인증기능 + 계정별 목록관리 기능 + 파일로 저장기능
- 클립보드 복사기능
- 관리자 기능
'''
import sys , os

from PyQt5.QtWidgets import QApplication
import src.python.defines.defines as df
import src.python.common.application_context as ctx
import src.python.view.login as lg



def init():
    # 저장경로 설정
    # df.initRepositoryPath(__file__)

    # ApplicationContext 생성
    ctx.getInstance()



def main():
    init()
    app = QApplication(sys.argv)
    wLogin = lg.createLogin(ctx.getInstance().getTemplatePath('main_dialog.ui'),ctx.getInstance().getImagePath('login_icon.png'))
    wLogin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
