#!python3
# -*- coding:utf -*-


singleMap = {}


def Singleton(tag='', dp=False):
    def wrap(cls):
        def onDecorator(*args, **kwargs):
            if cls.__name__ not in singleMap:
                singleMap[cls.__name__] = cls(*args, **kwargs)

            if dp:
                print('{} || {} - args : {} , kwargs : {}'.format(tag , cls.__name__, args, kwargs))
            return singleMap[cls.__name__]
        return onDecorator
    return wrap
