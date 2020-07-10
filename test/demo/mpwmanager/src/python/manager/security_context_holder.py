#!python3
# -*- coding:utf-8 -*-


from datetime import datetime
from src.python.mod.authentication import Authentication

'''
 - 로그인한 정보를 보관하고 있다
 - 로그인이후에는 SecurityContextHolder 객체를 통해 사용자 정보를 확인할수 있따.
'''

def getInstance():
    class SecurityContextHolder:
        def __init__(self, _authentication=None):
            self._authentication = None

        def setAuthentication( self , _authentication  = None):
            self._authentication = _authentication
            self._logintime = datetime.now()

        def getUsername(self):
            return self._authentication.getEmail()

        def getPassword(self):
            return self._authentication.getPwd()

        def getAuthority(self):
            return self._authentication.getAuthority()

    return SecurityContextHolder()


if __name__ == '__main__':
    auth = Authentication('xferlog@naver.com', '1111')
    sch = SecurityContextHolder(auth)
    print('sch username : {}'.format(sch.getUsername()))

# sch2 = SecurityContextHolder(auth)
