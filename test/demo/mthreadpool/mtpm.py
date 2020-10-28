#!python3
# -*- coding:utf-8 -*-

from demo.mthreadpool.singleton_decorator import Singleton

"""
 - ThreadPool Manager
"""


@Singleton(dp=True)
class MThreadPoolManager:
    def __init__(self): pass


if __name__ == '__main__':
    mtpm = MThreadPoolManager()
    mtpm2 = MThreadPoolManager()
