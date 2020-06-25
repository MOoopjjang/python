#!python3.7.3
# -*- coding:utf-8 -*-

import os
from source.defines.singleton import Singleton
import source.manager.mauthenticationmanager as mam
import source.manager.informationmanager as im
import source.manager.admin as ad

def getInstance():
    @Singleton(tag='[ctx]', display=True)
    class ApplicationContext():
        def __init__(self):
            self._load_()

        def __repr__( self ):
            l = ['module :{}'.format(k) for k in self._ctx_]
            return '@'.join(l)

        def _parsingBaseName_(self , _path):
            return os.path.basename(_path)

        def _load_(self):
            self._ctx_ = dict()
            self._ctx_[self._parsingBaseName_(mam.__file__)] = mam.getInstance()
            self._ctx_[self._parsingBaseName_(im.__file__)] = im.getInstance()
            self._ctx_[self._parsingBaseName_(ad.__file__)] = ad.getInstance()

        def getComponent(self, _cname=None):
            return self._ctx_[self._parsingBaseName_(_cname)]

    return ApplicationContext()


if __name__ == '__main__':
    apx = getInstance()
    print('injection Instance : {}'.format(apx))
