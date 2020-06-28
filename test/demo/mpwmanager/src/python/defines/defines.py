#!python3
#-*- coding:utf-8 -*-


import os , sys

RGX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

CERF_PATH = './cerf/cerf'

AUTH_BIN = None
USER_BIN = None

IMAGE_PATH = None
TEMPLATE_PATH = None


def initResourcePath():
    import src.resources.template as te
    import src.resources.image as img

    global IMAGE_PATH
    global TEMPLATE_PATH

    IMAGE_PATH = os.path.dirname(img.__file__)
    TEMPLATE_PATH = os.path.dirname(te.__file__)


def getImagePath(name):
    return os.path.join(IMAGE_PATH , name)

def getTemplatePah(name):
    import os
    return os.path.join(TEMPLATE_PATH , name)




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





