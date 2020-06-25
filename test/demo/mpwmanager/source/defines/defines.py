#!python3
#-*- coding:utf-8 -*-


RGX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

CERF_PATH = './cerf/cerf'

AUTH_BIN = None
USER_BIN = None


def initRepositoryPath( _file ):
    import os
    global AUTH_BIN
    global USER_BIN

    org_path = os.getcwd()
    if os.path.basename(_file) == 'main.py':
        os.chdir(os.getcwd())
        os.chdir('..')
    else:
        os.chdir(os.getcwd())

    AUTH_BIN = os.path.join(os.getcwd() , '.auth.bin')
    USER_BIN = os.path.join(os.getcwd() , '.user.bin')
    os.chdir(org_path)





