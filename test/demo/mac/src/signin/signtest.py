#!python3
# -*- coding:utf-8 -*-


from src.signin.sign_manager import SignManager
from src.common.authentication_manager import AuthenticationManager


if __name__ == '__main__':
    def menu(menu_list):
        print('********** sign menu **********')
        for i,t in enumerate( menu_list ,start = 1 ):
            print(f'{i} . {t}')
        print('*******************************')
        v = input('select:')
        return v


    while True:
        v = menu(['signUp' , 'login' , 'refresh' , 'display'])
        if v in ['1' ,'2']:
            email = input('email:')
            pwd = input('password:')
            username = input('username:')
            if v == '1':SignManager().signup(email , pwd , username)
            else: SignManager().login(email ,pwd )
        elif v == '3':
            email = input('email:')
            SignManager().refresh(email)
        elif v == '4':
            AuthenticationManager().print()
        else:
            break


