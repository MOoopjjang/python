#!python3
#-*- coding:utf-8 -*-


import os , sys
import src.resources.file as store

RGX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

CERF_PATH = './cerf/cerf'

'''
file db 저장소 설정
'''
AUTH_BIN = os.path.join(os.path.dirname(store.__file__) , '.auth.bin')
USER_BIN = os.path.join(os.path.dirname(store.__file__) , '.user.bin')






