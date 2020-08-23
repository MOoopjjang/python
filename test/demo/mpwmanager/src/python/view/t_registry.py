#!python3.7.3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import src.python.common.application_context as ctx
from src.python.view.view_base import BaseView

def getLayout():

    form_class = uic.loadUiType(ctx.getInstance().getTemplatePath('registry_layout.ui'))[0]
    class RegistryLayout(QWidget , form_class , BaseView):
        def __init__(self):
            QWidget.__init__( self )
            self.setupUi(self)

        def getLayout( self ):
            return self.container_registry



    registryLayout = RegistryLayout()
    return registryLayout.getLayout()



