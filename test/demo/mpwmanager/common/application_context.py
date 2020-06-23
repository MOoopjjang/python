#!python3.7.3
# -*- coding:utf-8 -*-


from defines.singleton import Singleton
from mauthenticationmanager import MAuthenticationManager

def getInstance():
    @Singleton(tag='[ctx]', display=True)
    class ApplicationContext:
        def __init__(self):
            self._load_()

        def _load_(self):
            self._ctx_ = {}
            self._ctx_[MAuthenticationManager.__name__] = MAuthenticationManager()

        def getComponent(self, _cname=None):
            return self._ctx_[_cname]

    return ApplicationContext()


if __name__ == '__main__':
    apx = getInstance()
