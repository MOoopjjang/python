#!python3
# -*- coding:utf -*-


'''
인증 정보를 저장하는 VO
 - email , token
'''

import src.common.common_util as cutil


class AuthInfo:
    def __init__(self, _email=None, _token=None, _refreshToken=None):
        if _email is None or _token is None:
            raise Exception("_email 과 _token값을 체크핫헤요.")
        self._email = _email
        self._token = _token
        self._refreshToken = _refreshToken

    def __str__(self):
        mlist = []
        cutil.getInstanceMemberInfo(mlist, self.__dict__)
        return '<>'.join(mlist)

    def getEmail(self): return self._email

    def getToken(self): return self._token

    def getRefreshToken(self): return self._refreshToken
