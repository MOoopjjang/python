#!python3
# -*- coding:utf -*-

'''
Singleton instance관리 decorator module
'''

SINGLETON_DICT = {}


def SingletonDecorator(tag='', dp=False):
    def onWrap(cls):
        def onDecorator(*args, **kargv):
            if cls not in SINGLETON_DICT:
                SINGLETON_DICT[cls] = cls(*args, **kargv)
            if dp:
                print(f'{cls.__name__} : args : {args} , kargv : {kargv}')
            return SINGLETON_DICT[cls]

        return onDecorator

    return onWrap
