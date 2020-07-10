#!python3.7.3
# -*- coding:utf -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import src.python.common.application_context as ctx
from src.python.view.view_base import BaseView

from functools import partial

'''
Custom Alert Dialog
'''
def createDialog():
    form_class = uic.loadUiType(ctx.getInstance().getTemplatePath('custom_alert_popup.ui'))[0]
    class CustomAlertPopup(QDialog, form_class,BaseView):
        TEXT_STYLE = 'font-size:20px;'
        def __init__(self):
            QDialog.__init__(self)
            self.setupUi(self)


        def _click_( self , _listener):
            _listener('hi')
            self.close()


        def setText( self , _text):
            self.lbl_text.setText(_text)
            self._setStyle_((self.lbl_text,),_style=CustomAlertPopup.TEXT_STYLE)
            return self

        def setIConImage(self , _image_info ):
            iconImg = QPixmap()
            iconImg.load(_image_info['path'])
            iconImg = iconImg.scaledToWidth(_image_info['w'])
            iconImg = iconImg.scaledToHeight(_image_info['h'])
            self.lbl_alert_icon.setPixmap(iconImg)
            return self


        def setButtons(self , buttonDatas):
            if len(buttonDatas) > 3 or len(buttonDatas) == 0:
                raise Exception("최소 1 최대 3 개의 button만 만들수 있습니다.")

            layout = QHBoxLayout()
            for idx , button_info in enumerate( buttonDatas ):
                btn = QPushButton(button_info['text'],self)
                btn.setCheckable(True)
                btn.toggle()
                btn.clicked.connect(partial(self._click_ , button_info['listener']))
                layout.addWidget(btn)

            self.gb_button.setLayout(layout)
            return self



    return CustomAlertPopup()




if __name__ == '__main__':
    import src.python.defines.defines as df

    def func_ok():
        print('OK')

    def func_cancel():
        print('cancel')

    df.initRepositoryPath(__file__)
    app = QApplication(sys.argv)
    qd = createDialog()
    qd.setText('비밀번호가 일치하지 않습니다.')\
        .setIConImage({'path':ctx.getInstance().getImagePath("alert_icon.png"),"w":62,"h":52})\
        .setButtons([
            {'text':'OK','listener':func_ok}
            ,{'text': 'cancel', 'listener': func_cancel}
            ,{'text': 'test', 'listener': func_cancel}
        ])
    qd.show()
    sys.exit(app.exec_())
