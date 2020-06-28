#!python3.7.3
# -*- coding:utf-8 -*-

import os
from src import python as m


def tst1():
    print('{}'.format(os.path.dirname(m.__file__)))
    os.chdir(os.path.dirname(m.__file__))
    os.chdir('..')
    p = os.getcwd()
    print('p : {}'.format(p))



if __name__ == '__main__':
    tst1()

