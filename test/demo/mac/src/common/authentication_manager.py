#!python3
# -*- coding:utf -*-


'''
 - 인증된 정보를 관리
    * email , token pair로 저장
    * 정보 저장 ,  갱신 , 삭제


'''

from src.common.singleton_decorator import SingletonDecorator
from src.common.domain.auth_info import AuthInfo
import src.common.common_util as cutil


@SingletonDecorator(tag="[AM]", dp=True)
class AuthenticationManager:
    def __init__(self):
        self._auth = {}

    def __str__(self):
        mlist = []
        cutil.getInstanceMemberInfo(mlist, self.__dict__)
        return '<>'.join(mlist)

    def add(self, _email, _token):
        self._auth[_email] = AuthInfo(_email, _token)

    def remove(self, _email):
        if _email in self._auth:
            del self._auth[_email]

    def get(self, _email):
        return self._auth[_email]

    def print(self):
        i = 1
        for k,v in  self._auth.items():
            print(f'{i} {k} :: {v}')
            i+=1



if __name__ == '__main__':
    am = AuthenticationManager()
    am.add("xferlog@gmail.com", "11111")
    am.add("kknda@aaa.com", "22222")

    print(f'{am}')
