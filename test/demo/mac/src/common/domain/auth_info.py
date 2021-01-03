#!python3
# -*- coding:utf -*-


'''
인증 정보를 저장하는 VO
 - email , token
'''

import src.common.common_util as cutil

class AuthInfo:
    def __init__(self , _email = None , _token = None):
        if _email is None or _token is None:
            raise Exception("_email 과 _token값을 체크핫헤요.")
        self._email = _email
        self._token = _token

    def __str__(self):
        mlist = []
        cutil.getMemberInfo(mlist , self , '<>')
        return '<>'.join(mlist)
        # return cutil.getMemberInfo(self , '<>')

    def getEmail(self):return self._email
    def getToken(self):return self._token
