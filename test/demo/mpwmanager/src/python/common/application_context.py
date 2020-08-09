#!python3.7.3
# -*- coding:utf-8 -*-

'''
 - application에서 전역적으로 사용될 module들을 관리하는 객체
'''

import os
from src.python.defines.singleton import Singleton
import src.python.manager.mauthenticationmanager as mam
import src.python.manager.informationmanager as im
import src.python.manager.admin as ad
import src.python.manager.security_context_holder as sch



def getInstance():
    @Singleton(tag='[ctx]', display=True)
    class ApplicationContext():
        def __init__(self):
            self._load_()
            self._resource_load_()

        def __repr__( self ):
            l = ['module :{}'.format(k) for k in self._ctx_]
            return '@'.join(l)

        def _parsingBaseName_(self , _path):
            return os.path.basename(_path)

        '''
        전역적으로 사용될 module을 injection 한다.
        '''
        def _load_(self):
            self._ctx_ = dict()
            self._ctx_[self._parsingBaseName_(mam.__file__)] = mam.getInstance()
            self._ctx_[self._parsingBaseName_(im.__file__)] = im.getInstance()
            self._ctx_[self._parsingBaseName_(ad.__file__)] = ad.getInstance()
            self._ctx_[self._parsingBaseName_(sch.__file__)] = sch.getInstance()

        '''
        resource 경로 설정
         - template 경로
         - image 경로
        '''
        def _resource_load_( self ):
            import src.resources.template as te
            import src.resources.image as img

            self._resources_ = dict()
            self._resources_['template'] = os.path.dirname(te.__file__)
            self._resources_['image'] = os.path.dirname(img.__file__)

        '''
        등록된 module 객체를 반환한다.
        '''
        def getComponent(self, _cname=None):
            return self._ctx_.get(self._parsingBaseName_(_cname) , None )

        '''
        .ui template 경로를 반환한다.
        '''
        def getTemplatePath(self , _file_name):
            print('tempate : {}'.format(os.path.join(self._resources_['template'],_file_name)))
            return os.path.join(self._resources_['template'] , _file_name)

        '''
        image 경로를 반환한다.
        '''
        def getImagePath(self , _file_name ):
            return os.path.join(self._resources_['image'],_file_name)


    return ApplicationContext()


if __name__ == '__main__':
    apx = getInstance()
    print('injection Instance : {}'.format(apx))
