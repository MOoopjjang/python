#!python3.7.3
# -*- coding:utf-8 -*-

import os


class ApplicationResource:
    repository_path = {}
    AUTH_BIN = None
    USER_BIN = None

    @staticmethod
    def initRepositoryPath( _file ):
        org_path = os.getcwd()
        if os.path.basename(_file) == 'main.py':
            os.chdir(os.getcwd())
            os.chdir('..')
        else:
            os.chdir(os.getcwd())

        AUTH_BIN = os.path.join(os.getcwd() , '.auth.bin')
        USER_BIN = os.path.join(os.getcwd() , '.user.bin')
        os.chdir(org_path)


