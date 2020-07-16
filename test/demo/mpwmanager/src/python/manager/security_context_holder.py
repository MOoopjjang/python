#!python3
# -*- coding:utf-8 -*-


from datetime import datetime
from src.python.mod.authentication import Authentication
from src.python.defines.singleton import Singleton

'''
 - 로그인한 정보를 보관하고 있다
 - 로그인이후에는 SecurityContextHolder 객체를 통해 사용자 정보를 확인할수 있따.
'''

def getInstance():
    @Singleton(tag = '[SecurityContextHolder]' , display = True)
    class SecurityContextHolder:
        def __repr__(self):
            return '{} : {} : {}'.format(self._authentication.getEmail(),self._authentication.getAuthority(),self._logintime)

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
    holder = getInstance();
    holder.setAuthentication(auth)
    print('sch username : {}'.format(holder.getUsername()))

# sch2 = SecurityContextHolder(auth)
