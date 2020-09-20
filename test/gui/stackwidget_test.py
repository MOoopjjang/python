#!python3
# coding:utf-8

# 예제 내용
# * 스택 위젯의 기본 사용법
# * 여러 위젯을 한 위젯 공간에 선택될 수 있도록 한다.
# https://github.com/RavenKyu/OpenTutorials_PyQt/blob/master/QtFramework/QtWidgets/QStackedWidget/QStackedWidget_00_basic.py

import sys

from PyQt5.QtCore import QModelIndex
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QListView
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QWidget

from gui.widget_5 import Widget_5


class StWidgetForm(QGroupBox):
    '''
    위젯 베이스 클래스
    '''
    def __init__(self):
        QGroupBox.__init__(self)
        self.box = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(self.box)


class Widget_1(StWidgetForm):
    '''
    버튼그룹
    '''
    def __init__(self):
        super(Widget_1 , self).__init__()
        self.setTitle('Widget_1')
        self.box.addWidget(QPushButton('Test_1'))
        self.box.addWidget(QPushButton('Test_2'))
        self.box.addWidget(QPushButton('Test_3'))

class Widget_2(StWidgetForm):
    def __init__(self):
        super(Widget_2 , self).__init__()
        self.setTitle('Widget_2')
        self.box.addWidget(QLabel('Test Label'))

class Widget_3(StWidgetForm):
    def __init__(self):
        super(Widget_3 , self).__init__()
        self.setTitle('Widget_3')
        self.box.addWidget(QLabel('Test Label'))

class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.stk_w = QStackedWidget(self)
        self.init_widtet()

    def init_widtet(self):
        self.setWindowTitle("Hello World")
        widget_layout = QBoxLayout(QBoxLayout.LeftToRight)

        group = QGroupBox()
        box = QBoxLayout(QBoxLayout.TopToBottom)
        group.setLayout(box)
        group.setTitle("Buttons")
        widget_layout.addWidget(group)

        fruits = ["Buttons in GroupBox" , "TexBox in GroupBox" , "Label in GroupBox" , "cwkim custom1" ,"TextEdit"]
        view = QListView(self)
        model = QStandardItemModel()
        for f in fruits:
            model.appendRow(QStandardItem(f))
        view.setModel(model)
        box.addWidget(view)

        self.stk_w.addWidget(Widget_1())
        self.stk_w.addWidget(Widget_2())
        self.stk_w.addWidget(Widget_3())
        self.stk_w.addWidget(Widget_5())
        self.stk_w.addWidget(QTextEdit())

        widget_layout.addWidget(self.stk_w)
        self.setLayout(widget_layout)

        # 시그널 슬롯 연결
        view.clicked.connect(self.slot_clicked_item)


    @pyqtSlot(QModelIndex)
    def slot_clicked_item(self , QModelIndex):
         self.stk_w.setCurrentIndex(QModelIndex.row())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())









