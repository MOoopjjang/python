#!python3
# -*- coding:utf-8 -*-

'''
 - user 등록 / 인증 기능제공
 - 등록된 모든 user 인증정보 제공
 - 계정정보를 MDataAccessManager를 통해 저장/삭제/편집을 할수 있다.
'''

import src.python.defines.defines as df
from src.python.mod.authentication import Authentication
from src.python.defines.singleton import Singleton
from src.python.manager.mdataaccessmanager import MDataAccessManager
import src.python.common.application_context as ctx


def getInstance():
    @Singleton('mAuthenticationManager', True)
    class MAuthenticationManager:
        def __init__(self):
            self._repositoryManager = MDataAccessManager().load(df.AUTH_BIN)

        def _checkMember_(self, email):
            return False if self._repositoryManager.findByOne(email) else True

        def _checkEmailSyntax_(self, email):
            import re

            rgx = re.compile(df.RGX_EMAIL)
            mo = rgx.search(email)
            return False if mo == None else True

        def createMember(self, email=None, pwd=None, authentication=None):
            '''
            새로운 사용자를 등록한다.
            '''
            if email is None or pwd is None:
                raise Exception('파라미터 오류입니다.')

            if self._checkMember_(email) == False:
                errmsg = '{} 는 이미등록된 사용자입니다.'.format(email)
                raise Exception(errmsg)

            if self._checkEmailSyntax_(email) == False:
                errmsg = '{} 는 email이 아닙니다.'.format(email)
                raise Exception(errmsg)

            # 등록
            self._repositoryManager.save(email, Authentication(email, pwd, authentication))

        def removeMember(self, _email):
            '''
            member를 등록해지한다.
            '''
            auth = self._repositoryManager.findByOne(_email)
            if auth != None:
                try:
                    self._repositoryManager.remove(_email)
                except:
                    raise Exception('{} 계정삭제중 에러가 발생했습니다.'.format(_email))

        def getMember(self, _email=None):
            '''
            계정정보를 반환한다.
            '''
            if _email is None: raise Exception('파리미터 오류입니다.')
            return self._repositoryManager.findByOne(_email)

        def getAllMembers(self):
            '''
            등록된 모든 사용자의 정보를 반환한다.
            '''
            return self._repositoryManager.findByAll()

        def certification(self, _email, _pwd):
            '''
            인증 진행
            '''
            auth = self._repositoryManager.findByOne(_email)
            if auth is None: return False

            if auth.matched(_pwd):
                print('인증되었습니다.')
                return True;
            return False

    return MAuthenticationManager()


if __name__ == '__main__':
    import os
    if os.path.exists(df.AUTH_BIN):
        os.unlink(df.AUTH_BIN)

    mm = getInstance()
    mm.createMember('xferlog@naver.com', '11111')
    mm.createMember('cccc@naver.com', '11111')
    mm.createMember('admin@naver.com', '2222', 'ADMIN')
    print('*' * 20)
    for m in mm.getAllMembers():
        print('{}'.format(m))

    # mc = getInstance()
