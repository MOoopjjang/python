#!python3
# -*- coding:utf-8 -*-


from src.signin.sign_manager import SignManager
from src.common.am import AuthenticationManager


if __name__ == '__main__':
    sm = SignManager()
    sm.signup("aaa@bbb.com" , '1111' , 'cwkim'
              ,lambda d:{
                    AuthenticationManager().add(d['email'], d['token'])
                }
    ,lambda data:{

    })


